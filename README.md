Mensa Online
----

Mensa Online is a web-based service for “Mensa Restaurant” based in Kamp-Lintfort target towards Hochschule RheinWaal University. This system is designed to be compatible with all the available mobile devices to provide service facility to restaurant and the customers as well. The service that is provided through our web-application for user is being able to view menu, pre-ordering, checking wallet, making payment, recharging wallet and redeeming cards. The Administrator of the restaurant can manage order, manage menu, manage invoice and account of user and generate report as well. In this project, we have targeted shortcomings of the similar applications for different universities and based on our research, we have developed an alternative system with new features. This project is developed using HTML/CSS, Vue.js JavaScript, PostgreSQL and Django Framework.

### Architecture

Version 1 - This version runs both servers locally. Follow the following instructions to run the project in your computer.

### Final Report

Click in the following link to see the documentation (Project report).

http://fasc.info/projects3b

### Steps setup the project to work on your computer

Assumptions, we assume that you have the following programs installed in your computer:

- You have django already installed 
- You have nodejs already installed

#### Run vue js project

A. Go to mensa-online>mensa-vue, and run the following command:

> npm install

B. Install axios on mensa-vue folder:

>npm install axios

C. Run the Vue project: 

> npm run dev

#### Run django project

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
