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
    const email = document.getElementById('email').value;
    const firstName = document.getElementById('first_name').value;
    const lastName = document.getElementById('last_name').value;
    const address = document.getElementById('address').value;
    const postcode = document.getElementById('postcode').value;
    const city = document.getElementById('city').value;
    const countyState = document.getElementById('county_state').value;
    const country = document.getElementById('country').value;

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
            'firstName': firstName,
            'lastName': lastName,
            'address': address,
            'postcode': postcode,
            'city': city,
            'countyState':countyState,
            'country':country,
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


// STRIPE

const stripe_public_key = document.getElementById('id_stripe_public_key').text.slice(1,-1);
const client_secret = document.getElementById('id_client_secret').text.slice(1,-1);
const stripe = Stripe('pk_test_51Hi6LFDDD97ZCNGjD6DE5mugRDYZlOFFUH4FuFcZFC97o4irRekvtKVj7bhspgsJQFKWdx246tIo3r6oqwz9qJIP00lGU38zXL');
const elements = stripe.elements();
const card = elements.create('card', {
    style: {
      base: {
        iconColor: '#c4f0ff',
        color: '#fff',
        fontWeight: 500,
        fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        ':-webkit-autofill': {
          color: '#fce883',
        },
        '::placeholder': {
          color: '#87BBFD',
        },
      },
      invalid: {
        iconColor: '#FFC7EE',
        color: '#FFC7EE',
      },
    },
  });
card.mount('#card-element');

const checkoutButton = document.getElementById('checkout-button');

checkoutButton.addEventListener('click', () => {
    // Create a new Checkout Session using the server-side endpoint you
    // created in step 3.
    fetch('/create-checkout-session', {
      method: 'POST',
    })
    .then(function(response) {
      return response.json();
    })
    .then(function(session) {
      return stripe.redirectToCheckout({ sessionId: session.id });
    })
    .then(function(result) {
      // If `redirectToCheckout` fails due to a browser or network
      // error, you should display the localized error message to your
      // customer using `error.message`.
      if (result.error) {
        alert(result.error.message);
      }
    })
    .catch(function(error) {
      console.error('Error:', error);
    });
  });



