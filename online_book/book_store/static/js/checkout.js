<!--  To check if cart exists  -->
        if (localStorage.getItem('cart') == null){
            var cart = {};
        }
        else{
            cart = JSON.parse(localStorage.getItem('cart'));
        }
        console.log(cart);


        <!--  Calculate cost and display order details  -->
        var cost = 0;
        if($.isEmptyObject(cart)){
            mystr=`<li class="list-group-item d-flex justify-content-between align-items-center" style='text-align: center;'>
                        Cart empty!!

                      </li>`
            $('#items').append(mystr);
        }
        else{
            for (item in cart){
                var price = cart[item][2]*cart[item][0];
                var name = cart[item][1];
                var quantity = cart[item][0];
                cost = cost+parseFloat(price);
                mystr=`<li class="list-group-item d-flex justify-content-between align-items-center">
                            ${name} <br>Price: ${price}
                            <span class="bi bi-primary bi-pill">Quantity: ${quantity}</span>
                          </li>`
                $('#items').append(mystr);
            }
        }
        mystr=`<li class="list-group-item d-flex justify-content-between align-items-center"><b>Total Cost:</b><span class="bi bi-primary bi-pill">Rs. ${cost}</span></li>`
        $('#items').append(mystr);