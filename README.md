# Django-School-Management
A fullstack school management project in django, bootstrap-4 and javascript.

# Installation:
1. go to the project folder
2. run `pip install -r requirements.txt`
3. create `.env` file and give credentials following `.env.example` template
4. See additional resources section to setup/get more info.
5. run `python manage.py migrate`
6. then `python manage.py runserver`
for testing, create a superuser too.

# Celery-redis setup:
1. Celery is installed, install redis as well. <br>
2. for linux users: 
- run redis server with `redis-server` command.
3. for windows users:
- Download redis (https://github.com/microsoftarchive/redis/releases/tag/win-3.0.504)
- Run redis-server.exe and redis-cli.exe.

And finally, while django server is running, run this command on another terminal <br>
`celery -A config worker -l INFO`

# Working Components:
* Create application for admission manually (it will save candidate as offline admission candidate)
* Online application for admission (payment and admission process handled automatically)
* Handle payment, admission, rejection, update candidate's status after communication
* Assign student to an academic batch, class
* Manage counseling (admission) dashboard with data visualization (download/view pdf reports)
* CRUD departments, subjects, teachers, academic session, term; import subjects from csv file
* Teacher list view, students list view, designation CRUD
* Create users, users list, view user groups and permissions