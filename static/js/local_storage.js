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

function insert_bs(bidang_id) {
	const key = bidang_id;
	console.log(key);
	var val;
	var inpValue = document.getElementsByName("opsi1");
	for(var i = 0; i < inpValue.length; i++){
		if(inpValue[i].checked){
			val = i;
		}
	}
	localStorage.setItem("a"+key, val);
	inpValue = document.getElementsByName("opsi2");
	for(var i = 0; i < inpValue.length; i++){
		if(inpValue[i].checked){
			val = i;
		}
	}
	localStorage.setItem("b"+key, val);
	inpValue = document.getElementsByName("opsi3");
	for(var i = 0; i < inpValue.length; i++){
		if(inpValue[i].checked){
			val = i;
		}
	}
	localStorage.setItem("c"+key, val);
	inpValue = document.getElementsByName("opsi4");
	for(var i = 0; i < inpValue.length; i++){
		if(inpValue[i].checked){
			val = i;
		}
	}
	localStorage.setItem("d"+key, val);
	console.log(localStorage);
	alert('jawaban tersimpan');
	location.reload();
}

function cek(bidang_id){
	const key = localStorage.getItem(bidang_id);
	console.log("opsi_"+key);
	document.getElementById("opsi_"+key).checked = true;
}

function cekbio(bidang_id){
	var key = localStorage.getItem("a"+bidang_id);
	console.log("opsi_"+key);
	document.getElementById("a_"+key).checked = true;

	key = localStorage.getItem("b"+bidang_id);
	console.log("opsi_"+key);
	document.getElementById("b_"+key).checked = true;

	key = localStorage.getItem("c"+bidang_id);
	console.log("opsi_"+key);
	document.getElementById("c_"+key).checked = true;

	key = localStorage.getItem("d"+bidang_id);
	console.log("opsi_"+key);
	document.getElementById("d_"+key).checked = true;
}

function show(bidang_id){
	localStorage.getItem(bidang_id);
	document.getElementById("inpValue").value = localStorage.getItem(bidang_id);
}

function hapus(bidang_id){
	const key = bidang_id;
	localStorage.removeItem(key);
	alert('jawaban terhapus');
	location.reload();
}