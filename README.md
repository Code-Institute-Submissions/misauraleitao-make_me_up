# Make.Me.Up

## Overview
 
Image will go here.

This is Make.Me.Up, Milestone 4. This is an online e-commerce store which allows users to purchase beauty products. 
The store conviently has a shopping cart where users can add products into it, save profile information and the user can have their own account.
This was all implemented using Django(a python framework).
Please note this project has been created for educational purposes.

## UX
### Stratagy

For the first core UX principle I took in consideration the audience that I am aiming to target and implementing features in order to allow this.
For the age group I am aiming to target people between the ages of 16-35 that love getting glamourous and all things makeup.
Taking this consideration I have followed a structured simple way to navigate and made sure I made my website responsive as people of that age group
tend to use their mobile phone to navigate the web.
I have also implemented a way for users to be able to sign up and create a profile so that they can save their details for future orders and also
they will be able to see their previous purchases.
I am also impleting the free delivery advert on bar so that customers can be prompt into making a larger purchase.

### User Stories

1. As a user I can easily navigate through the website as information is clear and straight forward.
2. As a user I can easily nagivate through to the products and pick what I want from the store and I am able to view the costs, and remove from the bag at ease.
3. As an admin user I can log in to the admin backend.
4. As an admin user I can approve or reject any email registrations and orders.
5. As an admin user I can sign in to add, remove and update items from the store.
6. As a user I can register or log in so that I can see my last orders, update my information.
7. As a user I can check if I am logged in or not and can choose whether to be logged in or logged out.
8. As a user I can individually search for products by typing in the search bar and by navigating by category on the nav bar.
9. As a user I can easily find descriptions of each product.
10. As a user I am able to make payments through the checkout.
11. As a user I am able to view an order confirmation at the end of purchase so that I know that the items have gone through.
12. As a user I am able to receive emails from the store for purchasing and signing up.
13. As a user I am able to view ratings of products on the labels.

### Scope

In order to achieve theese I have implemented:

A responsive navigation bar
Products page for all or for individual categories.
Product images, information and ratings displayed.
Secure admin login access for superuser.
Register/login/logout/profile pages.- allauth django
Updating and removing product management page for superusers.
Updating and removing products from basket options.
Send emails using Gmail SMTP

### Struture

This website has been designed taking in considaration of the age group and current trends. Although, I have kept it simple by not adding to much written information
so that it is more plesant to look at.
The website is made of 7 apps:

- Main project app 'make_me_up'
- Bag app - functionality for the shopping bag
- Checkout - functionality for completing an order
- Products - functionality for displaying the products
- Profile - functionality for the users profile












# Deployment
Heroku.
First, open up heroku.com and then login
Then, click on resources and provision a new Postgres database.
After, to use postgres i will go back to gitpod and install dj_database_url, and psycopg2.
I then, frooze the requirements needed to the txt file and went on to make_me_up settings.py and then import dj_database_url, and comment out the
database directory default configuration and create one for dj_database_url.
Go to settings and get the config vars and then paste them on the parse().
With all that done, now migrate and then loaddata for products and categories.
Then, create a superuser to log in with.
Now, the website database and app is finish.
Before I committed the code I made sure to uncomment what I previously commented out before on the databses at settings.py and remove the other one as I dont want
it to end up in the version control.
After this, i created an  if statement in settings.py
So that when the app is running on Heroku
where the database URL environment variable will be defined we connect to Postgres and otherwise, we connect to sequel light.
Then, I need to install gunicorn which will act as a webserver, and freezing it the requirements txt file.
Then, we create a procfile.
then, I need to allow it to settings.py allowed hosts, aswell as the localhost so it can be locally hosted too.
then press commit and push to deploy to heroku.
the application is now deployed to the heroku platform.

AWS.
First I created an account with AWS, then travel to aws management console and search for s3 scalable cloud. I will click that.