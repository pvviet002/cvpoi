/* =====================================================================
   taikhoan.js — ô tài khoản (Đăng nhập / tên + Đăng xuất) và dấu khoá trên
   các liên kết tới trang người xem chưa được mở.

   Tự tìm chỗ đặt: cuối mục lục trái (#cvnav, trang dùng nav.js) hoặc cuối
   thanh điều hướng trên (.cv-nav-in, trang do tools/dong-bo.py đồng bộ).
   nav.js tự nạp tệp này; trang đồng bộ nạp qua khối <!--cv-foot-->.

   Hỏi máy chủ qua /api/toi. Khi xem bằng python -m http.server (không có
   lớp đăng nhập) thì /api/toi không tồn tại và tệp này không làm gì.
   Dấu khoá chỉ là chỉ dẫn; việc chặn thật do middleware.js làm trên máy chủ.
   ===================================================================== */
(function(){
  'use strict';
  if (window.__cvTaiKhoan) return;
  window.__cvTaiKhoan = true;

  var CSS =
    '.cv-tk{display:flex;align-items:center;gap:8px;font-size:.82rem;line-height:1.3}' +
    '.cv-tk b{font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0}' +
    '.cv-tk a,.cv-tk button{flex:none;font:inherit;color:inherit;background:none;cursor:pointer;text-decoration:none;' +
      'border:1px solid rgba(127,127,127,.45);border-radius:8px;padding:5px 11px;opacity:.85;white-space:nowrap}' +
    '.cv-tk a:hover,.cv-tk button:hover{opacity:1;border-color:currentColor}' +
    '.cvnav .cv-tk{flex:none;padding:10px 14px;border-top:1px solid var(--border);justify-content:space-between}' +
    'body.cv-navcollapsed .cvnav .cv-tk{display:none}' +
    '.cv-nav-in .cv-tk{margin-left:12px}' +
    '.cv-nav-in .cv-tk b{max-width:160px}' +
    '@media (max-width:640px){.cv-nav-in .cv-tk{margin-left:auto}.cv-nav-in .cv-tk b{display:none}}' +
    '@media print{.cv-tk{display:none}}' +
    'a.cv-khoa::after{content:"";display:inline-block;width:.85em;height:.85em;margin-left:.4em;vertical-align:-.08em;' +
      'background:currentColor;opacity:.6;flex:none;' +
      '-webkit-mask:var(--cv-o-khoa) center/contain no-repeat;mask:var(--cv-o-khoa) center/contain no-repeat}' +
    ':root{--cv-o-khoa:url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 24 24\'%3E' +
      '%3Cpath d=\'M7 10V7a5 5 0 0 1 10 0v3h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2zm2 0h6V7a3 3 0 0 0-6 0z\'/%3E%3C/svg%3E")}';

  function chuanHoa(p){
    try { p = decodeURIComponent(p); } catch (e) {}
    p = p.replace(/\/{2,}/g, '/').toLowerCase();
    if (p.slice(-11) === '/index.html') p = p.slice(0, -10);
    return p;
  }

  /* Cùng quy tắc với timLuat trong middleware.js. */
  function timLuat(luat, p){
    var tot = null, dai = -1;
    for (var i = 0; i < luat.length; i++){
      var l = luat[i], d = l.duong, trung = (p === d || p + '/' === d);
      if (l.chinhxac){ if (trung) return l; continue; }
      if ((trung || p.indexOf(d) === 0) && d.length > dai){ tot = l; dai = d.length; }
    }
    return tot;
  }

  function danhDauKhoa(t){
    var as = document.querySelectorAll('a[href]');
    for (var i = 0; i < as.length; i++){
      var a = as[i];
      if (a.origin !== location.origin || a.closest('.cv-tk')) continue;
      var l = timLuat(t.luat, chuanHoa(a.pathname));
      var khoa = !!l && !l.duoc;
      a.classList.toggle('cv-khoa', khoa);
      if (khoa && !a.title) a.title = t.dangNhap ? 'Tài khoản của em chưa được mở trang này' : 'Cần đăng nhập';
    }
  }

  function dungO(t){
    var cho = document.getElementById('cvnav') || document.querySelector('.cv-nav-in');
    if (!cho) return;
    var o = document.createElement('div');
    o.className = 'cv-tk';
    if (t.dangNhap){
      var b = document.createElement('b');
      b.textContent = t.ten;
      b.title = t.ten + ' (' + t.taiKhoan + ')';
      var ra = document.createElement('button');
      ra.type = 'button';
      ra.textContent = 'Đăng xuất';
      ra.addEventListener('click', function(){
        fetch('/api/dang-xuat', { method: 'POST' }).then(function(){ location.reload(); });
      });
      o.appendChild(b); o.appendChild(ra);
    } else {
      var s = document.createElement('span');
      s.textContent = 'Chưa đăng nhập';
      s.style.opacity = '.7';
      var vao = document.createElement('a');
      vao.href = '/dang-nhap/?ve=' + encodeURIComponent(location.pathname + location.search);
      vao.textContent = 'Đăng nhập';
      if (cho.id === 'cvnav') o.appendChild(s);
      o.appendChild(vao);
    }
    cho.appendChild(o);
  }

  function chay(t){
    var st = document.createElement('style');
    st.textContent = CSS;
    document.head.appendChild(st);
    dungO(t);
    danhDauKhoa(t);
  }

  fetch('/api/toi', { cache: 'no-store' })
    .then(function(r){ return r.ok ? r.json() : null; })
    .then(function(t){
      if (!t || !t.luat) return;
      if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function(){ chay(t); });
      else chay(t);
    })
    .catch(function(){});
})();
