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
