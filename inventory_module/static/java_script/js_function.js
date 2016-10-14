/**
 * Created by dorabot on 10/14/16.
 */

function cancel_login(){

    document.getElementById("id_username").value = "";
    document.getElementById("id_password").value = "";
}

function getObj(id){
    return document.getElementById(id);
}

function checkBorrowQty(){

    var onhandQtyField = getObj("id_goods_onhand_qty");
    var borrowQtyField = getObj("id_goods_borrow_qty");

    var borrowQty = borrowQtyField.value;
    var onhandQty = onhandQtyField.value;

    if(borrowQty > onhandQty){
        warningText = "There is only " + onhandQty + " left! Not enough for you!";
        alert(warningText)
        borrowQtyField.select;
        return false;
    }
}