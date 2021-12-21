<!--       To check if cart exists        -->
        if (localStorage.getItem('cart') == null){
            var cart = {};
        }
        else{
            cart = JSON.parse(localStorage.getItem('cart'));
            updateCart(cart);
        }


        <!--    To check if the item already exists in the cart    -->
        $('.divpr').on('click', 'button.cart', function(){
            var idstr = this.id.toString();
            var cost=0;
            if (cart[idstr] !=undefined){
                quantity = cart[idstr][0] + 1;
            }
            else{
                quantity = 1;
                name=document.getElementById('name'+idstr).innerHTML;
                price = document.getElementById('price'+idstr).innerHTML.slice(8,);
                cart[idstr] = [quantity, name, price];
            }
            updateCart(cart);
        });


        <!--   Update contents in popover     -->
        $('#popcart').popover();
        updatePopover(cart);
        function updatePopover(cart){
            var popStr = "";
            popStr = popStr + "<h5> Books in shopping cart</h5>";
            var i = 1;
            for (var item in cart){
                popStr = popStr + "<b>" + i + "</b>. ";
                popStr = popStr + document.getElementById('name' + item).innerHTML.slice(0,19) + "Quantity: " + cart[item] + '<br>';
                i=i+1;
            }
            popStr = popStr + "<a href='checkout'><button class='btn btn-dark' id='checkout'>Checkout</button></a> <button class='btn btn-dark' onclick='clearCart()' id='clearCart'>Clear cart</button>"
            document.getElementById('popcart').setAttribute('data-content', popStr);
            $('#popcart').popover('show');
        }


        <!--    clear cart details    -->
        function clearCart(){
            cart = JSON.parse(localStorage.getItem('cart'));
            for (var item in cart){
                document.getElementById('div' +item).innerHTML ='<button id="'+ item +'" class="btn btn-dark cart" >Add to Cart</button>'
            }
            localStorage.clear();
            cart = {};
            updateCart(cart);
        }


        <!--    update cart when items added/ removed    -->
        function updateCart(cart){
            var sum=0;
            for (var item in cart){
                sum = sum+cart[item][0];
                document.getElementById('div'+item).innerHTML = "<button id='minus" + item+ "' class='btn btn-primary minus'>-</button> <span id='val" + item + "''>" + cart[item][0]+"</span><button id = 'plus" + item + "' class='btn btn-primary plus'>+</button>";
            }
            localStorage.setItem('cart', JSON.stringify(cart));
            document.getElementById('cart').innerHTML = sum;
            updatePopover(cart);
        }


        <!--   minus button function     -->
        $('.divpr').on("click", "button.minus", function(){
            a = this.id.slice(7, );
            cart['pr' +a][0] = cart['pr' +a][0] -1;
            cart['pr'+a][0] = Math.max(0, cart['pr'+a][0]);
            document.getElementById('valpr'+a).innerHTML = cart['pr'+a][0];
            updateCart(cart);
        });


        <!--   add button function     -->
        $('.divpr').on("click", "button.plus", function(){
            a = this.id.slice(6, );
            cart['pr' +a][0] = cart['pr' +a][0] +1;
            document.getElementById('valpr'+a).innerHTML = cart['pr'+a][0];
            updateCart(cart);
        });
