# taskker - a Todoist clone realized in Django and Vue.js

## Dependencies:
- Python (developed on 3.7.4)
- Pip 
- Node.js (developed on v13.6.0)
- Sass (npm install -g sass)
- Ruby (developed on 2.6.3p62)
- grunt-cli 


## Install and run:
- clone repository: cd <your project directory> && git clone https://github.com/calinbule/taskker.git
- inside the repository root directory create a virtual environment and activate it: vierualenv venv && source venv/bin/activate
- install the Python requirements: pip install -r requirements.txt
- navigate to the app directory and install the npm dependencies: cd app && npm instal
- start the Grunt server: grunt watch &
- migrate the database models: python manage.py makemigrations && python manage.py migrate
- create a superuser for the application: python manage.py createsuperuser (type in all the required information)
- run the Django development server: python manage.py runserver
- access the app at http://localhost:8000
  
## To implement:
- all tasks view
- per label view
- per priority view
- add task
- edit task
- check task
- delete task
- schedule task
- projects view
- add project
- edit project
- delete project
- all project view
- add label
- edit label
- delete label
- all labels view
- inbox (non scheduled tasks)
- today view
- upcoming view
- filters
- lateral menu bar with projects, labels, filters
- notifications
- add more options to settings menu
- search functionality
