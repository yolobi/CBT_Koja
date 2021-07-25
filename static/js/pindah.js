function next(bidang_id, len, bidang) {
  "use strict";
  var page = bidang_id;
  var pageCount = len;
  if(page < pageCount){
    page = page + 1;
  }
//  window.location.href='http://koja-olimpiade.com/'+bidang+'/1c096d6e413c588e44cb9031d03b012f/'+page;
  window.location.href='http://koja-olimpiade.com/'+bidang+'/1c096d6e413c588e44cb9031d03b012f/'+page;
};

function prev(bidang_id, len, bidang) {
  "use strict"
  var page = bidang_id;
  var pageCount = len;
  if(bidang_id > 1){
    page = page - 1;
  }
//  window.location.href='http://koja-olimpiade.com/'+bidang+'/1c096d6e413c588e44cb9031d03b012f/'+page;
window.location.href='http://koja-olimpiade.com/'+bidang+'/1c096d6e413c588e44cb9031d03b012f/'+page;
}

function navigasi(bidang_id, bidang){
  "use strict";
  var page = bidang_id;
//  window.location.href='http://koja-olimpiade.com/'+bidang+'/1c096d6e413c588e44cb9031d03b012f/'+page;
window.location.href='http://koja-olimpiade.com/'+bidang+'/1c096d6e413c588e44cb9031d03b012f/'+page;
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