<h2>Description</h2>  
<p>  
The idea of this project is to create a  
manageable electronic grade book for  
secondary and high schools all over the world.  
It can be both used by students and maintained  
and used by teachers and managers.  
</p>  
<p>  
The users, who log in to the  
website, are divided into four groups: student,  
teacher, manager and admin.  
</p>  
<p>  
Students can see the subjects they study,  
all unrated tasks they must do and all  
rated tasks. They cannot change any information  
on the site, as well as log in as a teacher  
or as a manager.  
</p>  
<p>  
Teachers can choose a class/grade and see all info  
about its students, tasks, given to them and  
their marks. Teachers can add, change or delete  
any task and mark.  
</p>  
<p>
Managers can see any information about students,  
teachers and disciplines. They can add, change  
and delete students, teachers and disciplines,  
but they cannot add, change or delete tasks  
and marks.
</p>  

 <p>
Admin is a superuser and can see any information  
and add, change and delete any data.  
  </p>
  
<h2>Technologies used</h2>  
<ul>  
<li>Python 3.9.1</li>  
<li>Django 3.1.7</li>  
<li>MySQL 8.0.20</li>  
<li>Windows PowerShell 5.1.19041.1237</li>  
<li>PyCharm 2021.2.1. (Community Edition)</li>  
<li>Git Bash 2.30.1.windows.1</li>  
</ul>  
  
<h2>How to install</h2>  

To clone the project from github, enter into the command line:  


    git clone https://github.com/smolin8033/Electronic-grade-book.git
    
   
   Install virtualenv:
   
   

    sudo pip install virtualenv

Enter into the cloned project's directory, where you can see the file 'manage.py'. Then, create a new virtual environment inside the project' folder and activate it:


    virtualenv newenv
    source newenv/bin/activate

Install Django, if it has not been installed before:


    pip install django

You can verify the installation by typing:


    django-admin --version

Create a new MySQL database, open the file 'settings.py' inside 'electronicgrade' folder. Input your database data here:


    DATABASES = {
    
	    'default': {
    
		    'ENGINE': 'django.db.backends.mysql',
    
		    'NAME': '',
    
		    'HOST': '',
    
		    'PORT': '',
    
		    'USER': '',
    
		    'PASSWORD': '',
    
	    }
    
    }

Make migrations of Django with your database by running:


    python manage.py makemigrations

Migrate:


    python manage.py migrate
Then your can start your django server:

    python manage.py runserver
Open the localhost in your browser to view the website. Now you can create a superuser (admin):

    python manage.py createsuperuser
Follow the instructions to create. When superuser is created, enter his/her login and password to enter the admin page. There, you can create users and give them permissions, so that new users (students, teacher and managers) also could log in to the website.