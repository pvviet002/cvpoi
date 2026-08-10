/* =====================================================================
   sitemap.js — "xương sống" của site theo CPH-Book (nguồn sự thật duy nhất
   cho điều hướng). nav.js đọc tệp này để dựng sidebar + breadcrumb.

   Cấu trúc: parts[] → chapters[] → (tùy) pages[].
     part:    {id, label, open?}
     chapter: {n, title, pages?}         // không có pages ⇒ hiện "Sắp có"
     page:    {slug, title, href?}       // href mặc định = "/<slug>/"

   Thuật ngữ theo ~/.claude/refs/thuat-ngu.md (vd Ch8 "chi phí bình quân",
   Ch17 "liên thông hai chiều").
   ===================================================================== */
window.CVSITEMAP = {
  parts: [
    { id:'p1', label:'Phần 1 · Các kỹ thuật cơ bản', open:true, chapters:[
      { n:0, title:'Ngôn ngữ lập trình C++', pages:[
        { slug:'io', title:'Nhập xuất dữ liệu' },
        { slug:'ifelse', title:'Rẽ nhánh' },
        { slug:'for-loop', title:'Vòng lặp' },
        { slug:'array-1d', title:'Mảng một chiều' },
        { slug:'array-2d', title:'Mảng hai chiều' },
        { slug:'string', title:'Xâu ký tự' }
      ]},
      { n:1, title:'Giới thiệu', pages:[ { slug:'introduction', title:'Giới thiệu' } ] },
      { n:2, title:'Độ phức tạp thời gian', pages:[ { slug:'time-complexity', title:'Độ phức tạp thời gian' } ] },
      { n:3, title:'Sắp xếp', pages:[ { slug:'binary-search', title:'Tìm kiếm nhị phân' } ] },
      { n:4, title:'Cấu trúc dữ liệu', pages:[
        { slug:'data-structures', title:'Cấu trúc dữ liệu (STL)' },
        { slug:'bst', title:'Cây tìm kiếm nhị phân' }
      ]},
      { n:5, title:'Tìm kiếm hoàn chỉnh', pages:[ { slug:'complete-search', title:'Tìm kiếm hoàn chỉnh' } ] },
      { n:6, title:'Giải thuật tham lam', pages:[ { slug:'huffman', title:'Thuật toán Huffman' } ] },
      { n:7, title:'Quy hoạch động', pages:[
        { slug:'dp', title:'Quy hoạch động trên đoạn' },
        { slug:'digit-dp', title:'Quy hoạch động chữ số', href:'/dp/digit-dp/' }
      ]},
      { n:8, title:'Phân tích chi phí bình quân', pages:[ { slug:'monotonic-stack', title:'Ngăn xếp tăng/giảm dần' } ] },
      { n:9, title:'Truy vấn phạm vi', pages:[
        { slug:'prefix-sum', title:'Tổng tiền tố' },
        { slug:'sqrt-decomposition', title:'Chia căn' },
        { slug:'segment-tree', title:'Segment tree' }
      ]},
      { n:10, title:'Xử lý bit', pages:[ { slug:'bit-manipulation', title:'Xử lý bit' } ] }
    ]},
    { id:'p2', label:'Phần 2 · Thuật toán đồ thị', chapters:[
      { n:11, title:'Đồ thị: khái niệm cơ bản', pages:[ { slug:'graph-basic', title:'Đồ thị cơ bản' } ] },
      { n:12, title:'Duyệt đồ thị', pages:[ { slug:'flood-fill', title:'Loang (flood fill)' } ] },
      { n:13, title:'Đường đi ngắn nhất', pages:[ { slug:'shortest-path', title:'Đường đi ngắn nhất' } ] },
      { n:14, title:'Thuật toán trên cây', pages:[ { slug:'tree', title:'Cây & tổ tiên chung gần nhất' } ] },
      { n:15, title:'Cây khung', pages:[ { slug:'dsu', title:'Các tập rời rạc (DSU)' } ] },
      { n:16, title:'Đồ thị có hướng', pages:[ { slug:'directed-graphs', title:'Đồ thị có hướng' } ] },
      { n:17, title:'Liên thông hai chiều', pages:[ { slug:'strong-connectivity', title:'Liên thông hai chiều' } ] },
      { n:18, title:'Truy vấn trên cây', pages:[ { slug:'euler-tour', title:'Euler tour trên cây', href:'/tree/euler-tour/' } ] },
      { n:19, title:'Đường đi và chu trình', pages:[ { slug:'euler-circuit', title:'Chu trình Euler' } ] },
      { n:20, title:'Luồng và lát cắt', pages:[ { slug:'max-flow', title:'Luồng và lát cắt' } ] }
    ]},
    { id:'p3', label:'Phần 3 · Chủ đề nâng cao', chapters:[
      { n:21, title:'Lý thuyết số', pages:[
        { slug:'number-theory', title:'Số học' },
        { slug:'sieve', title:'Sàng nguyên tố' }
      ]},
      { n:22, title:'Tổ hợp', pages:[
        { slug:'combinatoric', title:'Tổ hợp' },
        { slug:'in-exclusive', title:'Bao hàm — loại trừ' }
      ]},
      { n:23, title:'Ma trận', pages:[ { slug:'matrices', title:'Ma trận' } ] },
      { n:24, title:'Xác suất', pages:[ { slug:'probability', title:'Xác suất' } ] },
      { n:25, title:'Lý thuyết trò chơi', pages:[ { slug:'game-theory', title:'Lý thuyết trò chơi' } ] },
      { n:26, title:'Thuật toán trên chuỗi', pages:[ { slug:'string-algorithms', title:'Thuật toán trên chuỗi' } ] },
      { n:27, title:'Thuật toán căn bậc hai', pages:[ { slug:'sqrt-algorithms', title:'Thuật toán căn bậc hai' } ] },
      { n:28, title:'Cây phân đoạn (nâng cao)', pages:[ { slug:'segment-tree-advanced', title:'Cây phân đoạn (nâng cao)' } ] },
      { n:29, title:'Hình học', pages:[ { slug:'geometry', title:'Hình học' } ] },
      { n:30, title:'Thuật toán đường quét', pages:[ { slug:'sweep-line', title:'Thuật toán đường quét' } ] }
    ]}
  ]
};
