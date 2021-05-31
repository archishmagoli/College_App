# CollegeCompass 

### Description
CollegeCompass is a platform designed to help high school students navigate the college admissions process in an organized, less stressful way. The platform allows students to create checklists, add various colleges to their list, and access important mental health & financial aid resources. 

### Table of Contents
The folder ```CollegeCompass``` is the project folder in the repository. In this project, there are several application folders that constitute the project. 
1. ```contacts``` - includes default Django files. *These default Django files contain Python code that allows users to create, update, and delete contacts on the page.* Also includes (in the ```templates``` folder):
   1. ```contacts.html``` - allows users to see their list of contacts and mentors.

2. ```createaccount``` - includes default Django files. *These default Django files contain Python code that allows users to create an account on the platform.* Also includes (in the ```templates``` folder):
   1. ```second.html``` - contains code (including the title overlay) that is extended in ```signup.html```
   2. ```signup.html``` - contains code for the interface the user sees when signing up for an account on the platform. 

3. ```financialaid``` - includes default Django files. Also includes (in the ```templates``` folder):
   1. ```financialaid.html``` - has a list of financial aid resources for users to access. 

4. ```health``` - includes default Django files. *These default Django files contain Python code that allows users to input their mood for the day, maintain a list of health goals, and access external health resources.* Also includes (in the ```templates``` folder):
   1. ```health.html``` - contains code for the user interface when the user is accessing the Health Hub on the platform. 

5. ```index``` - includes default Django files. Also includes (in the ```templates``` folder):
   1. ```index.html``` - this is the first screen that users see when they access the platform. It includes buttons and links to login, register, and learn more about the application. 

6. ```mycalendar``` - includes default Django files. Also includes (in the ```templates``` folder):

7. ```mycolleges``` - includes default Django files. Also includes (in the ```templates``` folder):
   1. ```mycolleges.html``` - contains code for the interface the user will see when trying to add Safety, Reach, or Match schools to their college list on the page.

8. ```path2college``` - includes default Django files. Also includes (in the ```templates``` folder):
   1. ```path2college.html``` - user interface code; shows options for adding GPA, test scores, and other important information that would be important to know on the path to college. 

9. ```search``` - includes default Django files. Also includes (in the ```templates``` folder):
   1. ```search.html``` - this has not been programmed yet, but it will include a search bar for users to type into and to search items on the platform. 

10. ```static``` - includes:
   1. ```img``` folder - has a placeholder image for an image overlay. 
   2. Bootstrap files, including ```main.css```, ```main.css.map```, ```main.scss```, and ```package-lock.json```. 

11. ```survey``` - includes default Django files. Also includes (in the ```templates``` folder):
   1. ```survey.html``` - this has not been programmed yet, but it will include a set of questions for the user to answer to determine their purpose for using the app and other user information, including grade, intended major, etc. 

12. ```tasks``` - includes default Django files. *In these Django files, there are models used to create a form that allows users to create, modify, and delete items from a checklist.* Also includes (in the ```templates``` folder):
    1. ```checklist.html``` - Shows the checklist the user created. 
    2. ```delete.html``` - User is directed to this page if they decide to delete an item from their checklist. 
    3. ```update_task.html``` - User is directed to this page if they decide to modify an item from their checklist.

13. ```templates``` - includes the following folders/files:
    1. ```registration``` folder - includes ```first.html,``` which is a file that includes common HTML elements for other files. Also includes files like ```login.html```, ```password_reset_complete.html```, ```password_reset_confirm.html```, and two other files, which constitute the interface that users see when they are logging in or resetting their password.  
    2. ```layout.html``` - contains code for the navigation bar of the platform that is extended to most other pages in the application. 
    3. ```news.html``` - the first screen that logged-in users see on the platform; it shows recent published news articles regarding the college admissions process. 

14. ```manage.py``` - default Django Python file provided to run the Django project and start the development server. 

### Installation 
This project uses the *Django Web Framework*, so there are a few installation steps to run the project. 

#### How to Run the Project
* Open your command prompt and clone the repository with ```git clone https://github.com/archishmagoli/College_App/```. Then from the root of the repo:
* Install [pip](https://pip.pypa.io/en/stable/installing/) and [Django](https://docs.djangoproject.com/en/3.2/topics/install/). 
  * You may need to add a few environment variables to PATH after installing Django. 
* Run ```python manage.py runserver``` to start the server.
* Visit http://127.0.0.1:8000/ to access the project. 

### Credits
This project was created as part of the MetroHacks EmpowHer CS Competition. The main contributors to this platform are:
* Archishma Goli
* Ananya Radhakrishnan
* Sophiya Singh
* Salini Ambadapudi

