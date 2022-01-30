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