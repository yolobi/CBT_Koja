function insert_isian(bidang_id){

	const inpValue = document.getElementById("inpValue");
	console.log(inpValue);
	const key = bidang_id;
	const val = inpValue.value;

	localStorage.setItem(key, val);
	document.getElementById("inpValue").value = localStorage.getItem(key);
	console.log(localStorage.getItem(key));
	alert('jawaban tersimpan');
}

function insert_pg(bidang_id) {
	const key = bidang_id;
	var val;
	const inpValue = document.getElementsByName("opsi");
	for(var i = 0; i < inpValue.length; i++){
		if(inpValue[i].checked){
			val = i+1;
		}
	}
	localStorage.setItem(key, val);
	console.log(localStorage);
	alert('jawaban tersimpan');
}

function finish(len){
	document.addEventListener("DOMContentLoaded", function() {
      const formSubmitJawaban = document.getElementById("form-submit-jawaban")
      const totalJawaban = len; // ini ganti value nya sesuai total soal

      for(let i = 0; i < totalJawaban; i++) {
          let key = i+1 // sesuaikan key nya
          let inputHidden = document.createElement("input")
          inputHidden.setAttribute("type", "hidden")
          inputHidden.setAttribute("name", key)
          inputHidden.setAttribute("value", localStorage.getItem(key))
          formSubmitJawaban.appendChild(inputHidden)
      }
  })
}
/*document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("inpValue").value = localStorage.getItem("key")
})*/