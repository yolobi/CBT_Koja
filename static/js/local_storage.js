function insert_isian(bidang_id){

	const inpValue = document.getElementById("inpValue");
	console.log(inpValue);
	const key = bidang_id;
	const val = inpValue.value;

	localStorage.setItem(key, val);
	document.getElementById("inpValue").value = localStorage.getItem(key);
	console.log(localStorage.getItem(key));
	alert('jawaban tersimpan');
	location.reload();
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
	location.reload();
}

function hapus(bidang_id){
	const key = bidang_id;
	localStorage.removeItem(key);
	alert('jawaban terhapus');
	location.reload();
}