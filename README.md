# Dop Training Web Application and Newsletter Subscribtion Microservice

This application contains two parts:
- A dog training application with an option for owners to create their dog a profile
- A newsletter subscription microservice that utilizes Django, Python, RabbitMQ, Docker, Celery, and the PostgreSQL Database.
- The newsletter microservice allows users to subscribe to newsletters and receive them via email.
# Requirements:

- Python 3+ version
- Django
- pip
- Pipenv
- Docker
- Celery
- RabbitMQ
- PostgreSQL Database
- Twilio - Sendgrid https://www.twilio.com/
# Installation 

- Clone from Github
- run npm install
- pipenv install celery
- pipenv install dotenv 
- pipenv install psycopg2-binary 
- pip install celery also works if pipenv does not
- You will have to have rabbitMQ, PostgreSQL, and Docker installed on your PC before you can begin
    - https://www.architect.io/blog/2021-01-19/rabbitmq-docker-tutorial/
    - https://www.postgresql.org/docs/current/tutorial.html

# Run the App
- After installation run `docker-compose up` to start RabbitMQ 
- Make migrations: `py manage.py makemigrations`
- Migrate: `py manage.py migrate` 
- Create a superuser: `python manage.py createsuperuser`
- Run the following: `python manage.py runserver` and open Django Admin here: http://127.0.0.1:8000/admin 
- Run celery with the following command:  `celery -A dog_site worker --loglevel=INFO`
- Run RabbitMQ and Celery in different terminals
- Run `py manage.py runserver`

# Using the Newsletter App
- To create a newsletter:
    - Create an html file with the title of your newsletter
    - <body> and <head> tags not necessary
    - Use <p> tags and create your newsletter 
    - Save the file anywhere for uploading to Django Admin
- Open Django Admin here: http://127.0.0.1:8000/admin 
- Navigate to Newsletters
- Then Add a newsletter by uploading your newsletter file
- Sending Newsletters:
    - While in Django Admin and inside Newsletters click the drop down and select: Send selected newsletters to subscribers
    - Check the newsletters to send and click go
    - The newsletter will be send to all subscribers
-To sign up as a subscriber:
    - Enter email address and click subscribe
    - An email will be sent to you and a confirmation link will be included
    - Click the link to confirm your email
-To unsubscribe:
    - To unsubscribe, click the unsubscribe link inside the newsletter email

# Citations
https://www.twilio.com/blog/build-email-newsletter-django-twilio-sendgrid


# Using the Dog Training Application - Pettiquette

- Navigate to localhost: 8000
- Explore the homepage
- Use the menu button to navigate to other pages
- Check out the Dog Training page
- Create a dog profile
- View profile on the dog profile page
# Citations:
Date: 3/1/2023
Copied / Adapted From:

https://fonts.google.com/

https://django-embed-video.readthedocs.io/en/latest/installation.html

https://www.djangoproject.com/

https://django-crispy-forms.readthedocs.io/en/latest/index.html

https://freefrontend.com/css-testimonials/#google_vignette

/* Icon set - http://ionicons.com/ */

https://codepen.io/arefeh_htmi/pen/bGpyKZd

https://fontawesome.com/icons/categories/social

https://djangocentral.com/uploading-images-with-django/