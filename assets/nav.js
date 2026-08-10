/* =====================================================================
   nav.js — dựng sidebar phân cấp + breadcrumb từ CVSITEMAP (assets/sitemap.js).
   Nạp SAU sitemap.js. Không phụ thuộc thư viện ngoài.

   Trang cần có sẵn: <aside class="cvnav" id="cvnav"></aside> và (tùy)
   <div class="cvcrumb" id="cvcrumb"></div>, thân là <body class="cv-shell" data-nav="<slug>">.
   Gọi: CVNav.mount({current:'<slug hoặc ch{N}>'})  (nếu bỏ trống sẽ đọc data-nav).
   ===================================================================== */
(function(global){
  'use strict';

  function pageHref(p){ return p.href || ('/' + p.slug + '/'); }

  function locate(map, cur){
    for (var i = 0; i < map.parts.length; i++){
      var pt = map.parts[i];
      for (var j = 0; j < pt.chapters.length; j++){
        var ch = pt.chapters[j];
        if (('ch' + ch.n) === cur) return { part: pt, ch: ch, page: null };
        if (ch.pages) for (var k = 0; k < ch.pages.length; k++){
          if (ch.pages[k].slug === cur) return { part: pt, ch: ch, page: ch.pages[k] };
        }
      }
    }
    return null;
  }

  function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

  function mount(opts){
    opts = opts || {};
    var map = global.CVSITEMAP;
    if (!map) throw new Error('CVNav: thiếu CVSITEMAP (nạp assets/sitemap.js trước)');
    var cur = opts.current || document.body.getAttribute('data-nav') || '';
    var loc = locate(map, cur);
    var navEl = document.getElementById('cvnav');
    var crumbEl = document.getElementById('cvcrumb');
    if (!navEl) throw new Error('CVNav: thiếu <aside id="cvnav">');

    /* khôi phục trạng thái thu gọn mục lục (nhớ giữa các trang) */
    try { if (localStorage.getItem('cvNavCollapsed') === '1') document.body.classList.add('cv-navcollapsed'); } catch (e) {}

    /* ---- sidebar ---- */
    var brand =
      '<div class="cv-brand"><div class="cv-logo">CP</div><div>' +
      '<b>' + esc(opts.brand || 'Lý thuyết CP') + '</b>' +
      '<span>' + esc(opts.sub || 'CPH · Cẩm nang thi đấu') + '</span></div></div>' +
      '<div class="cv-filter"><input id="cvnavq" type="text" placeholder="Lọc chương…" autocomplete="off"></div>';

    var body = map.parts.map(function(pt){
      var isCurPart = loc && loc.part === pt;
      var open = isCurPart || pt.open;
      var chs = pt.chapters.map(function(ch){
        var has = ch.pages && ch.pages.length;
        var isCurCh = loc && loc.ch === ch;
        var head = '<button class="cv-chh"><span class="cv-cn">' + ch.n + '</span>' + esc(ch.title) +
          (has ? '<span class="cv-tw">&#9662;</span>' : '<span class="cv-soon">Sắp có</span>') + '</button>';
        var secs = '';
        if (has){
          secs = '<div class="cv-secs">' + ch.pages.map(function(p){
            var on = loc && loc.page === p;
            return '<a href="' + pageHref(p) + '"' + (on ? ' class="on"' : '') + '>' + esc(p.title) + '</a>';
          }).join('') + '</div>';
        }
        var cls = 'cv-ch' + (has ? '' : ' gap') + (isCurCh ? ' cur open' : '');
        var data = (ch.title + ' chương ' + ch.n).toLowerCase();
        return '<div class="' + cls + '" data-t="' + esc(data) + '">' + head + secs + '</div>';
      }).join('');
      return '<div class="cv-part' + (open ? ' open' : '') + '">' +
        '<button class="cv-ph"><span class="cv-tw">&#9662;</span>' + esc(pt.label) + '</button>' +
        '<div class="cv-chs">' + chs + '</div></div>';
    }).join('');

    var collapseBtn = '<button class="cv-collapse" id="cvcollapse" type="button" ' +
      'title="Thu gọn mục lục" aria-label="Thu gọn hoặc mở mục lục" aria-expanded="true"></button>';
    navEl.innerHTML =
      '<div class="cv-top">' + collapseBtn + brand + '</div>' +
      '<div class="cv-scroll">' + body + '</div>';

    /* ---- breadcrumb ---- */
    if (crumbEl){
      var c = '';
      if (loc){
        c += '<span>' + esc(loc.part.label) + '</span><span class="sep">&rsaquo;</span>' +
             '<span>Chương ' + loc.ch.n + ' · ' + esc(loc.ch.title) + '</span>';
        if (loc.page) c += '<span class="sep">&rsaquo;</span><b>' + esc(loc.page.title) + '</b>';
      }
      crumbEl.innerHTML =
        '<button class="cv-menu" id="cvmenu">&#9776; Mục lục</button>' +
        '<div class="cv-crumbtext">' + c + '</div><div class="grow"></div>';
    }

    /* ---- tương tác ---- */
    navEl.addEventListener('click', function(e){
      var ph = e.target.closest('.cv-ph');
      if (ph){ ph.parentElement.classList.toggle('open'); return; }
      var chh = e.target.closest('.cv-chh');
      if (chh){ var ch = chh.parentElement; if (ch.querySelector('.cv-secs')) ch.classList.toggle('open'); }
    });
    var q = document.getElementById('cvnavq');
    if (q) q.addEventListener('input', function(){
      var s = q.value.trim().toLowerCase();
      var chsAll = navEl.querySelectorAll('.cv-ch');
      for (var i = 0; i < chsAll.length; i++){
        var ok = !s || chsAll[i].getAttribute('data-t').indexOf(s) >= 0;
        chsAll[i].classList.toggle('cv-hidden', !ok);
        if (ok && s){ chsAll[i].classList.add('open'); chsAll[i].closest('.cv-part').classList.add('open'); }
      }
    });
    var mb = document.getElementById('cvmenu');
    if (mb) mb.addEventListener('click', function(){ document.body.classList.toggle('cv-navopen'); });
    var cb = document.getElementById('cvcollapse');
    function updCb(){
      if (!cb) return;
      var col = document.body.classList.contains('cv-navcollapsed');
      cb.innerHTML = col ? '&#187;' : '&#171;';           /* » mở  ·  « thu gọn */
      cb.setAttribute('aria-expanded', String(!col));
      cb.title = col ? 'Mở mục lục' : 'Thu gọn mục lục';
    }
    updCb();
    if (cb) cb.addEventListener('click', function(){
      var col = document.body.classList.toggle('cv-navcollapsed');
      try { localStorage.setItem('cvNavCollapsed', col ? '1' : '0'); } catch (e) {}
      updCb();
    });

    /* đưa mục hiện tại vào tầm nhìn của sidebar */
    var onEl = navEl.querySelector('.cv-secs a.on') || navEl.querySelector('.cv-ch.cur');
    if (onEl && onEl.scrollIntoView) try { onEl.scrollIntoView({ block:'center' }); } catch(e){}
  }

  global.CVNav = { mount: mount };
})(window);
