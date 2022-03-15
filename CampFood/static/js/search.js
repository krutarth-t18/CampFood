function search_food() {
    let input = document.getElementById('searchbar').value
	input=input.toLowerCase();
	let myTable = document.getElementById('myTable');
    let tr = myTable.getElementsByTagName('tr');

	for (var i = 0; i < tr.length; i++) {
	    let td = tr[i].getElementsByTagName('td')[1];
        if(td){
            let value = td.textContent;
            if(value.toLowerCase().indexOf(input) > -1){
                tr[i].style.display = "";
            }
            else{
                tr[i].style.display = "none";
            }
        }
    }
}

//if (!x[i].innerHTML.toLowerCase().includes(input)) {
//		    x[i].style.display="none";
//		}
//		else {
//			    x[i].style.display="list-item";
//		}
