// MOBILE MENU
// menu hamburger
document.querySelector(".navbar-toggler").addEventListener("click", (e) => {
    document.querySelector(".navbar-collapse").classList.toggle("show");
    document.querySelector('body').classList.toggle("offcanvas-active");
});

// close button 
document.querySelector(".btn-close").addEventListener("click", (e) => {
    document.querySelector(".navbar-collapse").classList.remove("show");
    document.querySelector('body').classList.remove("offcanvas-active");
});

// CSRF TOKEN
// https://docs.djangoproject.com/en/3.1/ref/csrf/

function getCSRFToken(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCSRFToken('csrftoken');

//CART

const cartButtons = document.querySelectorAll(".cart-action");
cartButtons.forEach((button) => {
    button.addEventListener('click', () => {
        const productId = button.dataset.productid;
        const cartAction = button.dataset.cartaction;
        const pageUrl = button.dataset.pageurl;
        const pageName = button.dataset.pagename;

        if (user === 'AnonymousUser' || isUserAuthenticated === 'False') {
            updateCart(productId, cartAction, pageUrl, pageName);

        } else if (isUserAuthenticated === 'True'){
            updateCart(productId, cartAction, pageUrl, pageName);
        }
    });
});

// const updateCartGuest = (productId, cartAction, pageUrl, pageName) => {

//     var cart = {quantity:99};
//     sessionStorage.setItem('cart', JSON.stringify(cart));
//     // var obj = JSON.parse(sessionStorage.cart);
//     console.log(sessionStorage.cart);
// }

const updateCart = (productId, cartAction, pageUrl, pageName) => {
    fetch('/orders/update_cart/', 
    {
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'cartAction': cartAction,
            'pageUrl': pageUrl,
            'pageName': pageName,
        })
    }).then(response => {
        return response.json();
    }).then(data => {
        location.reload()
    });
};

// MESSAGES ON RELOAD
const messages = document.querySelector(".messages")

if (messages) {
    window.scrollTo({ top: 0, behavior: 'smooth' });
} 

// CHECKOUT


const checkoutForm = document.getElementById( "checkoutForm" );

// ...and take over its submit event.
checkoutForm.addEventListener( "submit", event => {
  event.preventDefault();
  checkoutSuccess();
} );

const checkoutSuccess = () => {
    alert('yallah')
    var email = document.getElementById('email').value;

    fetch('/checkout/process/', 
    {
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'email': email,
        })
    })
    .then(response => {
        window.location = window.location.href + 'success/'
        // return response.json();
    }).catchj(errror => {
        window.location = window.location.href + 'failure/'
    });
    // .then(data => {
    // });
    };


