
 
###########################################
######### Running the project #############
###########################################


###### Running local ###### 

on terminal 1 cmd: git clone xxx
on terminal 1 cmd: cd docker_template/django
on terminal 1 cmd: source venv/bin/activate
on terminal 1 cmd: pip install -r requirements.txt
on terminal 1 change debug to TRUE in settings.py in django
on terminal 1 cmd: python manage.py runserver

on terminal 2 cmd: sudo systemctl enable rabbitmq-server
on terminal 2 cmd: sudo systemctl start rabbitmq-server
on terminal 2 cmd: sudo systemctl status rabbitmq-server

on terminal 3 cmd: celery -A core worker -B -l INFO
(if you want to run both separately, the code is "celery -A core worker -l info --pool=solo" and "celery -A core beat -l info")

on terminal 4 cmd: python manage.py shell
on terminal 4 cmd: from task1.tasks import add
on terminal 4 cmd: add.delay(2,2)

on terminal 5 cmd: cd docker_template/flask
on terminal 5 cmd: source venv/bin/activate
on terminal 5 cmd: pip install -r requirements.txt
on terminal 5 cmd: flask run

on url: http://127.0.0.1:8000/reviews - test send of email


###### Running production ###### 

on terminal 1 cmd: git clone xxx
on terminal 1 cmd: cd docker_template

on terminal 1 change debug to FALSE in settings.py in django folder

on terminal 1 cmd: docker-compose build
on terminal 1 cmd: docker-compose up

on terminal 2 cmd: docker exec -it django_container sh
on terminal 2 cmd: python manage.py shell
on terminal 2 cmd: from task1.tasks import add
on terminal 2 cmd: add.delay(2,2)

on url: http://127.0.0.1:8000/reviews - test send of email






###########################################
######### Building from scratch ###########
###########################################


##########################################
##### Setting up django ##################
##########################################
# mkdir docker_template
# cd docker_template
# create docker-compose.yml in this directory
# mkdir django_app
# cd django_app
# python3 -m venv venv
# source venv/bin/activate
# pip install django (plus all the pkgs you need)
# django-admin startproject core .
# pip freeze > requirements.txt
# python manage.py runserver
# create dockerfile in this directory

###########################################
##### Running single dockerfile (django) ##
###########################################
# cd docker_template/django
# docker build --tag python-django1 .
# docker run --publish 8000:8000 python-django1
# docker exec -it fbdf9567f98a2cd08d2227fcfa787f2101dec138538941ead798b16614da20f5 /bin/bash

##########################################
##### Setting up flask ###################
##########################################
# mkdir docker_template
# cd docker_template
# create docker-compose.yml in this directory
# mkdir flask_app
# cd flask_app
# python3 -m venv venv
# source venv/bin/activate
# pip install flask (plus all the pkgs you need)
# pip freeze > requirements.txt
###### create app.py file with the neccessary code
# python app.py / flask run
# create dockerfile in this directory

##########################################
##### Running single dockerfile (Flask) ##
##########################################
# cd docker_template/flask
# docker build --tag python-flask1 .
# docker run --publish 5000:5000 python-flask1
# docker exec -it fbdf9567f98a2cd08d2227fcfa787f2101dec138538941ead798b16614da20f5 /bin/bash



##########################################
##### Running entire docker compose ######
##########################################
# cd docker_template
# docker-compose build
# docker-compose up
# docker exec -it name_of_container sh



##########################################
##### Packages ###########################
##########################################
#### important pkgs
# pip install psycopg2-binary
# pip install celery
# pip install django-celery-beat
# pip install python-dotenv

#### unneccessary pkgs
# pip install flower
# pip install django-celery-results

### original requirements.txt 
# Django>=3.0,<4.0
# psycopg2-binary>=2.8
# celery
# redis