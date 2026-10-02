/* =====================================================================
   middleware.js — lớp kiểm tra đăng nhập. Vercel chạy tệp này TRÊN MÁY CHỦ
   trước khi trả bất kỳ trang nào, nên trang bị khoá không bao giờ rời máy
   chủ nếu người xem chưa đăng nhập hoặc không thuộc nhóm được phép.

   Dữ liệu:
     _auth/taikhoan.js  danh sách tài khoản (do tools/tai-khoan.py sinh)
     _auth/quyen.js     luật: thư mục nào dành cho nhóm nào (sửa tay)
   Khoá ký phiên: biến môi trường CV_SECRET đặt trong Vercel
     (Project → Settings → Environment Variables), dài ít nhất 32 ký tự.
     Thiếu khoá thì không ai đăng nhập được và mọi trang khoá vẫn đóng.

   Đường dẫn do tệp này tự trả lời (không có tệp tĩnh tương ứng):
     POST /api/dang-nhap   {ten, matkhau}  → đặt cookie phiên
     POST /api/dang-xuat                   → xoá cookie phiên
     GET  /api/toi                         → ai đang đăng nhập, được xem gì

   Chạy thử trên máy: node tools/chay-thu.mjs
   ===================================================================== */

import TAI_KHOAN from './_auth/taikhoan.js';
import LUAT from './_auth/quyen.js';

/* /assets/ không qua đây: chỉ là giao diện dùng chung, không có nội dung cần khoá. */
export const config = { matcher: '/((?!assets/).*)' };

const COOKIE = 'cv_phien';
const HAN_PHIEN = 30 * 24 * 3600;          /* giây */
const TOAN_QUYEN = 'giaovien';             /* nhóm xem được mọi trang */
const MUOI_GIA = '00000000000000000000000000000000';
const VONG_GIA = 100000;

/* Tệp nội bộ nằm trong repo nhưng không được lộ ra web. */
const CAM = ['/_auth/', '/tools/', '/middleware.js', '/readme.md', '/.gitignore',
             '/package.json', '/vercel.json'];

const enc = new TextEncoder();

/* ---------- tiện ích ---------- */

function tiep(){
  return new Response(null, { headers: { 'x-middleware-next': '1' } });
}

function json(ma, du_lieu, them){
  const h = new Headers({ 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' });
  if (them) for (const k in them) h.append(k, them[k]);
  return new Response(JSON.stringify(du_lieu), { status: ma, headers: h });
}

function vanBan(ma, noi_dung){
  return new Response(noi_dung, { status: ma, headers: { 'content-type': 'text/plain; charset=utf-8' } });
}

function hex(buf){
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
}

function tuHex(s){
  const a = new Uint8Array(s.length / 2);
  for (let i = 0; i < a.length; i++) a[i] = parseInt(s.substr(2 * i, 2), 16);
  return a;
}

/* So sánh không dừng sớm, để thời gian chạy không lộ số ký tự khớp. */
function bangNhau(a, b){
  if (a.length !== b.length) return false;
  let khac = 0;
  for (let i = 0; i < a.length; i++) khac |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return khac === 0;
}

/* Cùng công thức với tools/tai-khoan.py: PBKDF2-HMAC-SHA256, 32 byte. */
async function bamMatKhau(mat_khau, muoi_hex, vong){
  const khoa = await crypto.subtle.importKey('raw', enc.encode(mat_khau), 'PBKDF2', false, ['deriveBits']);
  const bit = await crypto.subtle.deriveBits(
    { name: 'PBKDF2', hash: 'SHA-256', salt: tuHex(muoi_hex), iterations: vong }, khoa, 256);
  return hex(bit);
}

async function ky(bi_mat, du_lieu){
  const khoa = await crypto.subtle.importKey('raw', enc.encode(bi_mat),
    { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  return hex(await crypto.subtle.sign('HMAC', khoa, enc.encode(du_lieu)));
}

function biMat(){
  const s = (typeof process !== 'undefined' && process.env && process.env.CV_SECRET) || '';
  return s.length >= 32 ? s : '';
}

function timTaiKhoan(ten){
  return Object.prototype.hasOwnProperty.call(TAI_KHOAN, ten) ? TAI_KHOAN[ten] : null;
}

/* ---------- phiên đăng nhập ---------- */

/* Cookie = <tên>|<16 ký tự đầu của mã băm mật khẩu>|<hạn>.<chữ ký>
   Nhóm KHÔNG nằm trong cookie mà đọc lại từ taikhoan.js mỗi lần, nên xoá tài
   khoản, đổi nhóm hay đặt lại mật khẩu có hiệu lực ngay sau lần deploy kế tiếp. */
async function taoCookie(ten, tk, bi_mat, https){
  const than = ten + '|' + tk.bam.slice(0, 16) + '|' + (Math.floor(Date.now() / 1000) + HAN_PHIEN);
  const gia_tri = encodeURIComponent(than) + '.' + await ky(bi_mat, than);
  return COOKIE + '=' + gia_tri + '; Path=/; Max-Age=' + HAN_PHIEN + '; HttpOnly; SameSite=Lax' +
    (https ? '; Secure' : '');
}

function xoaCookie(https){
  return COOKIE + '=; Path=/; Max-Age=0; HttpOnly; SameSite=Lax' + (https ? '; Secure' : '');
}

async function docPhien(request, bi_mat){
  if (!bi_mat) return null;
  const tho = request.headers.get('cookie') || '';
  const m = tho.match(new RegExp('(?:^|;\\s*)' + COOKIE + '=([^;]+)'));
  if (!m) return null;
  const cham = m[1].lastIndexOf('.');
  if (cham < 0) return null;
  let than;
  try { than = decodeURIComponent(m[1].slice(0, cham)); } catch (e) { return null; }
  if (!bangNhau(await ky(bi_mat, than), m[1].slice(cham + 1))) return null;
  const phan = than.split('|');
  if (phan.length !== 3) return null;
  if (!(Number(phan[2]) > Date.now() / 1000)) return null;
  const tk = timTaiKhoan(phan[0]);
  if (!tk || tk.bam.slice(0, 16) !== phan[1]) return null;
  return { ten: phan[0], tk: tk };
}

/* ---------- luật xem trang ---------- */

/* Đưa đường dẫn về một dạng duy nhất trước khi so luật, để không lách được
   bằng chữ hoa, mã hoá %, hai dấu gạch chéo hay đuôi index.html. */
function chuanHoa(pathname){
  let p;
  try { p = decodeURIComponent(pathname); } catch (e) { return null; }
  p = p.replace(/\\/g, '/').replace(/\/{2,}/g, '/').toLowerCase();
  if (/(^|\/)\.\.?(\/|$)/.test(p)) return null;
  if (p.endsWith('/index.html')) p = p.slice(0, -'index.html'.length);
  return p;
}

/* Luật "chinhxac" thắng; còn lại lấy luật có đường dẫn dài nhất khớp đầu. */
function timLuat(p){
  let tot = null, dai = -1;
  for (const l of LUAT){
    const d = l.duong.toLowerCase();
    const trung = p === d || p + '/' === d;
    if (l.chinhxac){
      if (trung) return l;
      continue;
    }
    if ((trung || p.startsWith(d)) && d.length > dai){ tot = l; dai = d.length; }
  }
  return tot;
}

function duocXem(luat, phien){
  if (!luat || luat.nhom.includes('mo')) return true;
  if (!phien) return false;
  const cua_toi = phien.tk.nhom;
  if (cua_toi.includes(TOAN_QUYEN) || luat.nhom.includes('*')) return true;
  return luat.nhom.some(n => cua_toi.includes(n));
}

/* ---------- ba đường dẫn /api ---------- */

function cungNguon(request){
  const o = request.headers.get('origin');
  if (!o) return true;
  try { return new URL(o).host === request.headers.get('host'); } catch (e) { return false; }
}

async function dangNhap(request, bi_mat, https){
  if (request.method !== 'POST') return json(405, { loi: 'Chỉ nhận POST.' });
  if (!cungNguon(request)) return json(403, { loi: 'Yêu cầu không hợp lệ.' });
  if (!bi_mat) return json(503, { loi: 'Máy chủ chưa đặt khoá phiên (CV_SECRET). Báo thầy Việt.' });
  if (!(request.headers.get('content-type') || '').includes('application/json'))
    return json(400, { loi: 'Yêu cầu không hợp lệ.' });
  let than;
  try { than = await request.json(); } catch (e) { return json(400, { loi: 'Yêu cầu không hợp lệ.' }); }
  const ten = String((than && than.ten) || '').trim().toLowerCase();
  const mat_khau = String((than && than.matkhau) || '');
  if (!ten || !mat_khau || ten.length > 64 || mat_khau.length > 200)
    return json(400, { loi: 'Nhập đủ tên đăng nhập và mật khẩu.' });

  /* Tên không tồn tại vẫn băm một lần, để thời gian trả lời không lộ tên nào có thật. */
  const tk = timTaiKhoan(ten);
  const bam = await bamMatKhau(mat_khau, tk ? tk.muoi : MUOI_GIA, tk ? tk.vong : VONG_GIA);
  if (!tk || !bangNhau(bam, tk.bam))
    return json(401, { loi: 'Sai tên đăng nhập hoặc mật khẩu.' });

  return json(200, { ten: tk.ten }, { 'set-cookie': await taoCookie(ten, tk, bi_mat, https) });
}

function dangXuat(request, https){
  if (request.method !== 'POST') return json(405, { loi: 'Chỉ nhận POST.' });
  if (!cungNguon(request)) return json(403, { loi: 'Yêu cầu không hợp lệ.' });
  return json(200, {}, { 'set-cookie': xoaCookie(https) });
}

function toi(phien){
  return json(200, {
    dangNhap: !!phien,
    taiKhoan: phien ? phien.ten : null,
    ten: phien ? phien.tk.ten : null,
    nhom: phien ? phien.tk.nhom : [],
    luat: LUAT.map(l => ({ duong: l.duong.toLowerCase(), chinhxac: !!l.chinhxac, duoc: duocXem(l, phien) }))
  });
}

/* ---------- điểm vào ---------- */

export default async function middleware(request){
  const url = new URL(request.url);
  const https = url.protocol === 'https:';
  const p = chuanHoa(url.pathname);
  if (p === null) return vanBan(400, 'Đường dẫn không hợp lệ.');
  if (CAM.some(c => p === c || p.startsWith(c)) || /\.(csv|py|mjs|md)$/.test(p))
    return vanBan(404, 'Không tìm thấy trang.');

  const bi_mat = biMat();

  if (p.startsWith('/api/')){
    if (p === '/api/dang-nhap') return dangNhap(request, bi_mat, https);
    if (p === '/api/dang-xuat') return dangXuat(request, https);
    if (p === '/api/toi') return toi(await docPhien(request, bi_mat));
    return json(404, { loi: 'Không có đường dẫn này.' });
  }

  const luat = timLuat(p);
  if (!luat || luat.nhom.includes('mo')) return tiep();

  const phien = await docPhien(request, bi_mat);
  if (duocXem(luat, phien)) return tiep();

  const dich = new URL('/dang-nhap/', url);
  dich.searchParams.set('ve', url.pathname + url.search);
  if (phien) dich.searchParams.set('loi', 'quyen');
  return new Response(null, { status: 302, headers: { location: dich.toString(), 'cache-control': 'no-store' } });
}
