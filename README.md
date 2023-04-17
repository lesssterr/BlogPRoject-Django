# BlogPRoject-Django
# How to run the project
Go to step by step on below command lines.
In Ubuntu by default in case of command python use python3. Or if you want to make available python command run on terminal command
$ sudo ln -s /usr/bin/python3 /usr/bin/python

$ git clone https://github.com/lesssterr/BlogPRoject-Django.git

open folder in vs code or any ide

In terminal $ python -m virtualenv env

In linux OS $ source env/bin/activate, and in Widnows OS PS > .\env\Scripts\activate. Pay attention, when your environment active in console you'll see the name of your virtual environment. 

$ pip install -r requirements.txt

$ python manage.py migrate

$ python manage.py createsuperuser
and fill username, email(optional) and password (keep type password even if you can't see it on your screen)

$ python manage.py runserver

Go on your browser to http://127.0.0.1:8000/