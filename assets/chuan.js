/* =====================================================================
   chuan.js — nút đổi nền sáng/tối, tô màu cú pháp C++, nút Sao chép,
   làm nổi mục đang đọc ở thanh bên.

   TÁCH NGUYÊN VĂN từ ChuyenDe/_template/shell.html (khối <script>).
   KHÔNG sửa tay file này — xem chuan.css để biết lý do.
   ===================================================================== */

(function(){
  /* ---- nút đổi nền sáng / tối ---- */
  /* Đọc --is-dark qua getComputedStyle, KHÔNG hỏi matchMedia: matchMedia có thể
     lệch với CSS đang áp dụng ở lần tải đầu. */
  var root = document.documentElement, btn = document.getElementById('tg');
  function isDark(){
    return getComputedStyle(root).getPropertyValue('--is-dark').trim() === '1';
  }
  btn.addEventListener('click', function(){
    root.setAttribute('data-theme', isDark() ? 'light' : 'dark');
  });

  /* ---- tô màu cú pháp C++ (đơn giản, một lượt quét) ---- */
  var KW = 'int|bool|void|char|long|double|float|unsigned|const|static|struct|class|return|for|while|do|if|else|break|continue|using|namespace|true|false|sizeof|new|delete|inline|auto';
  var LIB = 'vector|pair|stack|queue|string|map|set|cin|cout|endl|make_pair|push_back|pop_back|reverse|sort|size|empty|top|front|push|pop|begin|end|first|second|swap|max|min|clear|main';
  var RE = new RegExp(
      '(\\/\\/[^\\n]*)'                       + '|' +   /* chú thích  */
      '(&quot;(?:[^&]|&(?!quot;))*&quot;)'     + '|' +   /* xâu ""     */
      '(&#39;(?:[^&]|&(?!#39;))*&#39;)'        + '|' +   /* ký tự ''   */
      '("(?:[^"\\\\\\n]|\\\\.)*")'             + '|' +   /* xâu ""     */
      "('(?:[^'\\\\\\n]|\\\\.)*')"             + '|' +   /* ký tự ''   */
      '(#[a-z]+)'                              + '|' +   /* tiền xử lý */
      '\\b(' + KW  + ')\\b'                    + '|' +
      '\\b(' + LIB + ')\\b'                    + '|' +
      '\\b(\\d+)\\b', 'g');
  var CLS = ['c','s','s','s','s','pp','k','f','n'];

  document.querySelectorAll('pre code').forEach(function(el){
    el.innerHTML = el.innerHTML.replace(RE, function(){
      for (var i = 1; i <= 9; i++)
        if (arguments[i] !== undefined)
          return '<span class="' + CLS[i-1] + '">' + arguments[i] + '</span>';
      return arguments[0];
    });
  });

  /* ---- nút sao chép mã nguồn ---- */
  document.querySelectorAll('.codewrap').forEach(function(w){
    var pre = w.querySelector('pre');
    if(!pre) return;
    var b = document.createElement('button');
    b.className = 'cp';
    b.textContent = 'Sao chép';
    b.addEventListener('click', function(){
      var txt = pre.innerText;
      var done = function(){ b.textContent = 'Đã chép'; setTimeout(function(){ b.textContent = 'Sao chép'; }, 1400); };
      if (navigator.clipboard && navigator.clipboard.writeText)
        navigator.clipboard.writeText(txt).then(done, done);
      else {
        var ta = document.createElement('textarea');
        ta.value = txt; document.body.appendChild(ta); ta.select();
        try { document.execCommand('copy'); } catch(e){}
        document.body.removeChild(ta); done();
      }
    });
    w.appendChild(b);
  });

  /* ---- thanh bên: làm nổi mục đang đọc ---- */
  /* Mốc: mục cuối cùng có mép trên đã trôi qua vạch 130px; chạm đáy trang thì
     luôn sáng mục cuối. Cập nhật bọc trong requestAnimationFrame. */
  var secs = Array.prototype.slice.call(document.querySelectorAll('h2[id]'));
  var links = {};
  Array.prototype.forEach.call(document.querySelectorAll('aside.side a'), function(a){
    links[a.getAttribute('href').slice(1)] = a;
  });
  var curSec = null;
  function highlight(){
    if (!secs.length) return;
    var id = secs[0].id;
    for (var k = 0; k < secs.length; k++)
      if (secs[k].getBoundingClientRect().top <= 130)
        id = secs[k].id;
    if (window.innerHeight + window.pageYOffset >= document.documentElement.scrollHeight - 2)
      id = secs[secs.length - 1].id;
    if (id === curSec) return;
    if (curSec && links[curSec]) links[curSec].className = '';
    if (links[id]) links[id].className = 'on';
    curSec = id;
  }
  var pending = false;
  function onScroll(){
    if (pending) return;
    pending = true;
    requestAnimationFrame(function(){ highlight(); pending = false; });
  }
  window.addEventListener('scroll', onScroll, {passive:true});
  window.addEventListener('resize', onScroll, {passive:true});
  highlight();
})();
