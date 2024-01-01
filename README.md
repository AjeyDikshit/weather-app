Steps to create a web app using Django

1. Create a folder.
2. Open the terminal and create a virtual environment using `python -m venv {name of venv}`.
3. Start the virtual environment `.venv\Scripts\activate` in PowerShell.
4. Install the required libraries, `pip install django`
5. Then to start a project type the following commands in the terminal/shell:
   - django-admin startproject <name of project> <destination of project> -->  Example: `django-admin startproject project1 .`
   - python manage.py startapp <name of app> -->  Example: `python manage.py startapp app1`
   - python manage.py migrate
   - python manage.py runserver
6. At this point your server will start running
7. Add your 'app' to project.settings file, inside the INSTALLED_APPS variable
8. Go to project.urls file, import include from django.urls --> your import statement would look like `from django.urls import path, include`
9. Inside the <strong>urlpatterns<strong> variable add a new variable,  `path('', include('<name if app>.urls'))`
10. At this point for an elementary application, you are not required to change anything in the project folder, and can only focus on the app folder
11. To create a webpage in Django, we need to follow 3 steps (they can be in any order):
      - Create a template
      - Create a URL
      - Create a view
12. A template is an HTML/CSS file that will be rendered to the user when the webpage is accessed, The URL will be required to call the particular webpage, and the view will be where we can perform some tasks and dynamically update the template.
13. Inside urls.py create a path say `path('home/', views.home, name='home')`, this will load the view.home function when 'home/' is requested.
14. In views.py file, we will create a function called home, and render the template that has been created. Oe thing to keep in mind is that all the views functions take in an argument "request" by default, and not mentioning it while writing code will result in an error.
