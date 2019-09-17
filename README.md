Mensa Online - User & Admin interface
----
----

Version 1 - This version runs both servers locally.

Follow the following instructions to run the project in your computer.

Steps setup the project to work on your computer
----

Assumptions, we assume that you have the following programs installed in your computer:

- You have django already installed 
- You have nodejs already installed

Run vue js project
----

A. Go to mensa-online>mensa-vue, and run the following command:

> npm install

B. Install axios on mensa-vue folder:

>npm install axios

C. Run the Vue project: 

> npm run dev

Run django project
----

A. Install django-webpack-loader:

>pip install django-webpack-loader

B. Install rest framework:

>pip install djangorestframework

C. Install django-cors-headers to allow request done via Ajax:

>pip install django-cors-headers

D. Install crispy forms:

>pip3 install --user django-crispy-forms
>pip install image

E. Go to mensa-online folder and run the following command:

> python manage.py runserver
