function pindah(bidang_id, len) {
  "use strict";
  var page = bidang_id;
  var pageCount = len;

  console.log(bidang_id);

  document.getElementById("btnPrev").onclick = function() {
    page = ((page + pageCount + 1) % pageCount) + 1;
    window.location.href='http://localhost/komputer/1c096d6e413c588e44cb9031d03b012f/'+page;
  };
  document.getElementById("btnNext").onclick = function() {
    page = (page % pageCount) + 1;
    window.location.href='http://localhost/komputer/1c096d6e413c588e44cb9031d03b012f/'+page;
  };

  console.log(page);
};