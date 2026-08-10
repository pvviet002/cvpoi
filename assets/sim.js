/* =====================================================================
   sim.js — khung "phòng mô phỏng" tái dùng (kiểu visualgo).
   Nạp SAU chuan.js. Không phụ thuộc thư viện ngoài.

   Ý tưởng: khung lo phần CHUNG (giao diện, nút Chạy/Dừng/Bước/Tốc độ,
   tô sáng dòng mã giả đồng bộ, thông báo, đếm bước). Trang chỉ cung cấp
   phần RIÊNG của thuật toán: các thao tác sinh "khung hình" và hàm vẽ.

   Cách dùng:
     CVSim.create('#id', {
       title: 'Tên mô phỏng',
       input: {label:'Giá trị', type:'number', value:65},   // (tùy) một ô nhập dùng chung
       code: {                       // mã giả — mảng dòng; dòng bắt đầu bằng khoảng trắng = thụt vào
         search: ['nút ← gốc', 'khi nút ≠ NULL:', '  nếu ... → ...'],
         insert: [ ... ]
       },
       defaultCode: 'search', defaultOpLabel: 'Tìm kiếm',
       ops: [                        // mỗi thao tác là một nút
         {label:'Tìm kiếm', code:'search', run:function(val, api){ return framesArray; }},
         {label:'Chèn', variant:'alt', code:'insert', run:function(val, api){ return framesArray; }},
         {label:'Cây mẫu', variant:'ghost', run:function(val, api){ ...; return [idleFrame]; }}
       ],
       idle: {line:0, msg:'Chọn thao tác rồi bấm Chạy.'},
       draw: function(frame, canvasEl, api){ canvasEl.innerHTML = '<svg>...</svg>'; }
     });

   Mỗi "khung hình" (frame) là một object tùy ý, khung chỉ đọc 2 trường:
     frame.line : số (hoặc mảng số) — dòng mã giả cần tô sáng (đánh số từ 1)
     frame.msg  : chuỗi (cho phép HTML) — thông báo hiển thị dưới cùng
   Mọi trường khác do draw() của bạn tự hiểu.
   ===================================================================== */
(function(global){
  'use strict';

  function el(tag, cls, html){
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }

  function create(mount, cfg){
    var host = (typeof mount === 'string') ? document.querySelector(mount) : mount;
    if (!host) throw new Error('CVSim: không tìm thấy phần tử gắn "' + mount + '"');
    cfg = cfg || {};
    host.classList.add('sim');
    host.innerHTML = '';

    /* ---- giao diện ---- */
    var top = el('div', 'sim-top');
    top.appendChild(el('div', 'sim-title', cfg.title || ''));
    var opsBox = el('div', 'sim-ops');
    top.appendChild(opsBox);
    host.appendChild(top);

    var main = el('div', 'sim-main');
    var canvas = el('div', 'sim-canvas');
    var pc = el('div', 'sim-pc');
    pc.appendChild(el('div', 'sim-pc-h', 'Mã giả — <span class="op"></span>'));
    var pcLines = el('div', 'sim-pc-lines');
    pc.appendChild(pcLines);
    main.appendChild(canvas);
    main.appendChild(pc);
    host.appendChild(main);

    var ctrl = el('div', 'sim-ctrl');
    var bFirst = el('button', 'sim-ic', '&#9198;');       // ⏮
    var bPrev  = el('button', 'sim-ic', '&#9664;');       // ◀
    var bPlay  = el('button', 'sim-btn sim-play', '&#9654; Chạy');
    var bNext  = el('button', 'sim-ic', '&#9654;');       // ▶
    var spLab  = el('span', 'sim-sp', 'Tốc độ');
    var speed  = el('input', 'sim-speed');
    speed.type = 'range'; speed.min = '1'; speed.max = '5'; speed.value = '3';
    var prog   = el('span', 'sim-prog', 'Bước 0 / 0');
    [bFirst, bPrev, bPlay, bNext, spLab, speed, prog].forEach(function(x){ ctrl.appendChild(x); });
    host.appendChild(ctrl);

    var msg = el('div', 'sim-msg', '');
    host.appendChild(msg);

    var opSpan = pc.querySelector('.op');

    /* ---- mã giả ---- */
    var codeSets = cfg.code || {};
    if (Array.isArray(codeSets)) codeSets = { _default: codeSets };
    var curLines = [];
    function renderCode(key){
      var lines = codeSets[key] || codeSets._default || [];
      pcLines.innerHTML = lines.map(function(t, i){
        var indent = /^\s/.test(t) ? ' sim-in' : '';
        return '<div class="sim-ln' + indent + '" data-l="' + (i + 1) + '">' +
               '<span class="sim-n">' + (i + 1) + '</span>' + t.trim() + '</div>';
      }).join('');
      curLines = [].slice.call(pcLines.querySelectorAll('.sim-ln'));
    }

    /* ---- trạng thái chạy ---- */
    var frames = [ cfg.idle || { line: 0, msg: '' } ];
    var fi = 0, playing = false, timer = null;

    function interval(){ return 1600 - (speed.value - 1) * 310; }

    function paint(){
      var f = frames[fi];
      if (cfg.draw) cfg.draw(f, canvas, api);
      for (var i = 0; i < curLines.length; i++){
        var L = +curLines[i].getAttribute('data-l');
        var on = (f.line === L) || (Array.isArray(f.line) && f.line.indexOf(L) >= 0);
        curLines[i].classList.toggle('on', !!on);
      }
      msg.innerHTML = f.msg || '';
      prog.textContent = 'Bước ' + (fi + 1) + ' / ' + frames.length;
      bFirst.disabled = bPrev.disabled = (fi === 0);
      bNext.disabled = (fi >= frames.length - 1);
    }
    function show(i){ fi = Math.max(0, Math.min(frames.length - 1, i)); paint(); }
    function pause(){ playing = false; bPlay.innerHTML = '&#9654; Chạy'; clearTimeout(timer); }
    function tick(){
      if (!playing) return;
      if (fi >= frames.length - 1){ pause(); return; }
      fi++; paint(); timer = setTimeout(tick, interval());
    }
    function play(){
      if (frames.length <= 1) return;
      if (fi >= frames.length - 1){ fi = 0; paint(); }
      playing = true; bPlay.innerHTML = '&#9208; Dừng';
      timer = setTimeout(tick, interval());
    }

    bFirst.onclick = function(){ pause(); show(0); };
    bPrev.onclick  = function(){ pause(); show(fi - 1); };
    bNext.onclick  = function(){ pause(); show(fi + 1); };
    bPlay.onclick  = function(){ playing ? pause() : play(); };
    speed.oninput  = function(){ if (playing){ clearTimeout(timer); timer = setTimeout(tick, interval()); } };

    /* ---- API trả cho trang ---- */
    var api = {
      /* nạp danh sách khung hình mới; codeKey (tùy) đổi bộ mã giả + nhãn thao tác */
      load: function(fr, codeKey, opLabel){
        pause();
        frames = (fr && fr.length) ? fr : [ cfg.idle || { line: 0, msg: '' } ];
        fi = 0;
        if (codeKey != null){ renderCode(codeKey); opSpan.textContent = opLabel || ''; }
        paint();
      },
      redraw: paint,
      get index(){ return fi; },
      get length(){ return frames.length; }
    };

    /* ---- ô nhập dùng chung ---- */
    var input = null;
    if (cfg.input){
      var wrap = el('label', 'sim-op-in', (cfg.input.label ? cfg.input.label + ' ' : ''));
      input = el('input');
      input.type = cfg.input.type || 'number';
      if (cfg.input.value != null) input.value = cfg.input.value;
      if (cfg.input.min != null) input.min = cfg.input.min;
      if (cfg.input.max != null) input.max = cfg.input.max;
      wrap.appendChild(input);
      opsBox.appendChild(wrap);
    }

    /* ---- nút thao tác ---- */
    (cfg.ops || []).forEach(function(op){
      var b = el('button', 'sim-btn' + (op.variant ? (' sim-' + op.variant) : ''), op.label);
      b.onclick = function(){
        var val = input ? input.value : undefined;
        var res = op.run ? op.run(val, api) : null;
        if (res && res.length) api.load(res, op.code, op.label);
      };
      opsBox.appendChild(b);
    });

    /* ---- khởi tạo ---- */
    var firstKey = cfg.defaultCode ||
      (Array.isArray(cfg.code) ? '_default' : (cfg.code ? Object.keys(codeSets)[0] : '_default'));
    renderCode(firstKey);
    if (cfg.defaultOpLabel) opSpan.textContent = cfg.defaultOpLabel;
    paint();
    return api;
  }

  global.CVSim = { create: create };
})(window);
