/* =====================================================================
   chay-thu.mjs — chạy thử site trên máy CÓ lớp đăng nhập, giống trên Vercel:
   mọi yêu cầu đi qua middleware.js trước, được cho qua mới trả tệp tĩnh.

       node tools/chay-thu.mjs          → http://127.0.0.1:8777/
       node tools/chay-thu.mjs 9000     → cổng khác

   (python -m http.server vẫn dùng được để xem nội dung, nhưng khi đó không
   có đăng nhập: mọi trang đều mở.)

   Khoá phiên ở đây là khoá thử, chỉ dùng trên máy; khoá thật nằm trong biến
   môi trường CV_SECRET của Vercel.
   ===================================================================== */

import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const GOC = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const CONG = Number(process.argv[2]) || 8777;

if (!process.env.CV_SECRET) process.env.CV_SECRET = 'khoa-thu-tren-may-khong-dung-cho-web-that';

const mw = await import(pathToFileURL(path.join(GOC, 'middleware.js')).href);
const KHOP = new RegExp('^' + mw.config.matcher + '$');

const KIEU = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8', '.mjs': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8', '.svg': 'image/svg+xml',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.gif': 'image/gif', '.ico': 'image/x-icon',
  '.pdf': 'application/pdf', '.txt': 'text/plain; charset=utf-8'
};

function traTep(res, duong){
  let p;
  try { p = decodeURIComponent(duong); } catch (e) { res.writeHead(400).end(); return; }
  let tep = path.join(GOC, p);
  if (!tep.startsWith(GOC)) { res.writeHead(403).end(); return; }
  if (fs.existsSync(tep) && fs.statSync(tep).isDirectory()){
    if (!p.endsWith('/')) { res.writeHead(308, { location: duong + '/' }).end(); return; }
    tep = path.join(tep, 'index.html');
  }
  if (!fs.existsSync(tep)) { res.writeHead(404, { 'content-type': 'text/plain; charset=utf-8' }).end('404'); return; }
  res.writeHead(200, {
    'content-type': KIEU[path.extname(tep).toLowerCase()] || 'application/octet-stream',
    'cache-control': 'public, max-age=0, must-revalidate'
  });
  fs.createReadStream(tep).pipe(res);
}

http.createServer(async (req, res) => {
  const url = new URL(req.url, 'http://' + req.headers.host);
  try {
    if (KHOP.test(url.pathname)){
      const than = [];
      for await (const m of req) than.push(m);
      const yeu_cau = new Request(url, {
        method: req.method,
        headers: req.headers,
        body: (req.method === 'GET' || req.method === 'HEAD') ? undefined : Buffer.concat(than)
      });
      const tl = await mw.default(yeu_cau);
      if (!tl.headers.get('x-middleware-next')){
        const h = {};
        tl.headers.forEach((v, k) => { if (k !== 'set-cookie') h[k] = v; });
        const ck = tl.headers.getSetCookie();
        if (ck.length) h['set-cookie'] = ck;
        res.writeHead(tl.status, h);
        res.end(Buffer.from(await tl.arrayBuffer()));
        return;
      }
    }
    traTep(res, url.pathname);
  } catch (e) {
    console.error(e);
    res.writeHead(500).end('500');
  }
}).listen(CONG, '127.0.0.1', () => {
  console.log('Chạy thử có đăng nhập: http://127.0.0.1:' + CONG + '/');
});
