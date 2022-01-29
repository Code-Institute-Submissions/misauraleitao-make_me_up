Deployment
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