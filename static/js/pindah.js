function next(bidang_id, len) {
  "use strict";
  var page = bidang_id;
  var pageCount = len;

  page = ((page + pageCount + 1) % pageCount) + 1;
  window.location.href='http://localhost/komputer/1c096d6e413c588e44cb9031d03b012f/'+page;

};

function prev(bidang_id, len) {
  "use strict"
  var page = bidang_id;
  var pageCount = len;
  page = (page % pageCount) + 1;
  window.location.href='http://localhost/komputer/1c096d6e413c588e44cb9031d03b012f/'+page;
}

function navigasi(bidang_id){
  "use strict";
  var page = bidang_id;
  window.location.href='http://localhost/komputer/1c096d6e413c588e44cb9031d03b012f/'+page;

};

function essai(bidang){
  "use strict";
  window.location.href='http://localhost/komputer/1c096d6e413c588e44cb9031d03b012f/essai';
};

function clear(){
  var ele = document.getElementsByName("opsi");
  for(var i=0;i<ele.length;i++)
      ele[i].checked = false;
}