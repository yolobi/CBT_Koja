function next(bidang_id, len, bidang) {
  "use strict";
  var page = bidang_id;
  var pageCount = len;

  page = ((page + pageCount + 1) % pageCount) + 1;
  window.location.href='http://localhost/'+bidang+'/1c096d6e413c588e44cb9031d03b012f/'+page;

};

function prev(bidang_id, len, bidang) {
  "use strict"
  var page = bidang_id;
  var pageCount = len;
  page = (page % pageCount) + 1;
  window.location.href='http://localhost/'+bidang+'/1c096d6e413c588e44cb9031d03b012f/'+page;
}

function navigasi(bidang_id, bidang){
  "use strict";
  var page = bidang_id;
  window.location.href='http://localhost/'+bidang+'/1c096d6e413c588e44cb9031d03b012f/'+page;

};

function essai(bidang){
  "use strict";
  window.location.href='http://localhost/'+bidang+'/essay';
};

function finish(bidang){
  "use strict"
  window.location.href='http://localhost/'+bidang+'/finish';
}