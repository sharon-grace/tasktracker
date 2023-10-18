# tasktracker
Creating, viewing and updating the tasks assigned by the admin
# Task Tracker - Django Application

Task Tracker is a simple Django web application that allows users to manage tasks. Users can create, view, and mark tasks as completed or incomplete. 

Before you begin, ensure you have met the following requirements:

- Python 3 versions
- Pip, 

## Installation

1. Clone the project from the GitHub repository:
```bash
   git clone https://github.com/sharon-grace/tasktracker.git

2.Move to the project directory:
cd TaskTracker

3.Create a virtual environment
python -m venv venv

4.Activate the virtual environment:
venv\Scripts\activate

5.Install project dependencies:
pip install -r requirements.txt

6.Apply database migrations
python manage.py migrate

7.Running the Application
python manage.py runserver:http://localhost:8000/
to acess tasks:http://localhost:8000/tasks/

Admin Interface
to acess it give admin after runserver:http://localhost:8000/admin/.
create a superuser, if you have not created one:python manage.py createsuperuser

output
http://localhost:8000/tasks/
Click the "Toggle Status" button to mark tasks as completed or incomplete.











