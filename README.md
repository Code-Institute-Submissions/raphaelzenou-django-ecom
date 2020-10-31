# Django Ecommerce

Mock up Ecommerce website built with: 
* Python, Django and PostgreSQL in the backend
* Javascript, HTML, CSS, Bootstrap in the frontend
 
## UX
* UX is extremely barebones at the moment and is not considered complete

## Features

### Existing Features

* Product catalog / Pages (TBD)
* Flexible session system enabling members to browse as guests and then merge their persistent cart with the session
* Authentication system including password reset and basic profile editing
* Dynamically refreshed cart where quantities can be amended in a convenient manner
* Checkout process

### Features Left to Implement

* Much more user friendly UI 
* Search bar
* Multi currencies
* Addresses stored in the User profile
* Stock Management
* Sales
* Stripe integration

## Technologies Used

**Overview**

* Backend: Python/Django and PostgreSQL (Database)
* Frontend: Javascript/JQuery, HTML, CSS, Bootstrap
* Payments processing: Stripe

**Packages and Other technologies**

* ElphantSQL - PostgreSQL as a Service - https://www.elephantsql.com/ 
* 'venv' for virtual environments
* 'dotenv' for managing environment variables https://pypi.org/project/python-dotenv/ 
* 'psycopg2' as PostgreSQL database adapter https://www.psycopg.org/docs/
* 'pillow' for image management
* 'django-heroku' and 'whitenoise' for deployment and static files management

**Conventions**

* This site had been made having DRY and PEP8 principles in mind
* However these have not been reviewed yet 

## Testing

* Basic end to end testing has been carried out but not documented yet

## Deployment

* Deployment has been carried out on Heroku and the website is available via this link : https://pupestore.herokuapp.com/

## Credits

### Content
* Content is very limited at this webiste has been made to test some basic django concepts via an ecommerce mock up

### Media

* Images have mostly been taken from pexels, unsplash or other websites providing images free for commercial use

### Acknowledgements

* Setting up PostgreSQL https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-16-04
* Building a better responsive menu than the default bootstrap https://bootstrap-menu.com/detail-offcanvas-collapse.html
* Code Institute's Ecommerce example: https://github.com/ckz8780/boutique_ado_v1   
* Django Ecommerce example https://github.com/divanov11
* Login / Logout Django : https://learndjango.com/tutorials/django-login-and-logout-tutorial
* Custom user model: https://testdriven.io/blog/django-custom-user-model/
* Password reset: https://www.ordinarycoders.com/blog/article/django-password-reset
* SMTP email configuration : https://medium.com/@_christopher/how-to-send-emails-with-python-django-through-google-smtp-server-for-free-22ea6ea0fb8e
* Heroku deployment issue with sessions: https://stackoverflow.com/questions/50346326/programmingerror-relation-django-session-does-not-exist/50346820


