function next(bidang_id, len, bidang) {
  "use strict";
  var page = bidang_id;
  var pageCount = len;

  page = ((page + pageCount + 1) % pageCount) + 1;
//  window.location.href='http://koja-olimpiade.com/'+bidang+'/xxx/'+page;
  window.location.href='http://koja-olimpiade.com/'+bidang+'/xxx/'+page;
};

function prev(bidang_id, len, bidang) {
  "use strict"
  var page = bidang_id;
  var pageCount = len;
  page = (page % pageCount) + 1;
//  window.location.href='http://koja-olimpiade.com/'+bidang+'/xxx/'+page;
window.location.href='http://koja-olimpiade.com/'+bidang+'/xxx/'+page;
}

function navigasi(bidang_id, bidang){
  "use strict";
  var page = bidang_id;
//  window.location.href='http://koja-olimpiade.com/'+bidang+'/xxx/'+page;
window.location.href='http://koja-olimpiade.com/'+bidang+'/xxx/'+page;
};

function essai(bidang){
  "use strict";
//  window.location.href='http://koja-olimpiade.com/'+bidang+'/essay';
window.location.href='http://koja-olimpiade.com/'+bidang+'/essay';
};

function selesai(bidang){
  "use strict"
//  window.location.href='http://koja-olimpiade.com/'+bidang+'/finish';
window.location.href='http://koja-olimpiade.com/'+bidang+'/finish';
}