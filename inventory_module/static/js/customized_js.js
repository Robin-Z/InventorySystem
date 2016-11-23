/**
 * Created by dorabot on 10/14/16.
 */

/* Removed cancel_login button on login page */
// function cancel_login(){
//
//     document.getElementById("id_username").value = "";
//     document.getElementById("id_password").value = "";
// }

// $(document).ready(function () {
//
//      alert('Here is the check borrow qty js function!');
//
// })

function getObj(id){
    return document.getElementById(id);
}

function checkBorrowQty(){

    var onhandQtyField = getObj("id_goods_onhand_qty");
    var borrowQtyField = getObj("id_goods_borrow_qty");

    var borrowQty = borrowQtyField.value;
    var onhandQty = onhandQtyField.value;

    if(borrowQty <= 0){
        alert("Invalid Good borrow qty: " + borrowQty);
        borrowQtyField.focus();
        return false;
    }

    if(borrowQty > onhandQty){
        alert("There is only " + onhandQty + " left! Not enough for you!");
        borrowQtyField.focus();
        return false;
    }
}

onload = function showLoginUserName() {
    // alert("in show login user name..")

    var ajaxRequest;
    try {
		//Opera 8.0+, Firefox, Safari
		ajaxRequest = new XMLHttpRequest();
	}catch(e) {
        //IE Browsers
        try {
            ajaxRequest = new ActiveXObject("Mssml2.XMLHTTP");
        } catch (e) {
            try {
                ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
            } catch (e) {
                //Something went wrong
                alert("Your browser broke!");
                return false;
            }
        }
    }

    var loginUser = getObj("login_user");
    if(ajaxRequest){
        ajaxRequest.open("GET", "/inventory_module/navagation/");
        ajaxRequest.responseType = "JSON";
        ajaxRequest.setRequestHeader("Content-Type", "application/json", true);

        ajaxRequest.onreadystatechange = function () {
            if(ajaxRequest.readyState == 4 && ajaxRequest.status == 200){

                var return_data = JSON.parse(ajaxRequest.responseText); // Convert JSON string to javascript object
                // var stringObj = JSON.stringify(return_data);   // Convert Javascript object to JSON string

                for(var obj in return_data){
                    loginUser.innerText = return_data[obj];
                }
            }
        }
        ajaxRequest.send(null);
    }
}
