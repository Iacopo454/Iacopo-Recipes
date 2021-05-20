## Introduction Milestone 3- Iacopo Recipes book 
I am building my recipe book website which will also contains user recipes,
so the website will become a sharing recipe database website. 

## Index 
# UX
.
Overview
The purpose of this project is to design a website that user can enjoy to read and learn new simple recipes and also add their own ones. 
The website will be simple to use, from registering to adding a new recipe to the database. 
The website can be very helpful and inspirational to many different category of people, especially who struggle to find the time to prepare and cook complicated meals due to working reasons. 
The project is designed to be compatible with all devices, from computer to mobile and Highpads. 

# User Stories

I want the website to be easy to be used and looking good, so the user as I have already done, will be able to add a photo with the description of their recipe. 
The recipe are easy to search using the search bar and the user can also easily register and log in clickin on the relevant page from the top nav-bar. 

# Strategy

The primary goal is to provide a searchable database of recipes for website users, which is visually appealing, and easy to use.

# Scope

The website is simple and clean in desing, it consists of an Homepage with information about the website and a Main Image, and a simple top Nav-bar to navigate through the website pages and functionalities. 
I have searched similar websites and got influenced by them, please see below for credit. 

# Simple Structure

 The website is structured as follows:

Homepage:

Navbar at top, showing website title, and links to other pages
A main image of a classic Tiramisu' with a brief explanation of the purpose of the site.
Links to log in and regsiter.
Footer showing social media links for Instagram,Facebook and Twitter. 

Recipes:

A search feature at the top of the page.
Recipes displayed via "cards" or thumbnails, consisting of the recipe image/recipe title, in a grid format.

Recipe Details:
Will provide the recipe details such as ingredients, method, number of serving, and the author. 

Login/Sign Up:

The log in and sign up pages require the user to input username/password.

Profile:

Will allow users to add their own recipes, as well as edit any recipes already submitted.


# Surface

The websites tend to use simple colour schemes, with red darken-4 class taken from materialise often being used

# Feature
Existing

The website uses Materialize CSS features:

- Navbar (top navbar)
- Sidenav (to turn into sidenav on mobile)
- Cards (to display recipes)
- Forms (to add/edit recipes)
- Buttons (for links to other pages and add/edit/delete actions)
- Footer (bottom footer)

The website is linked to MongoDB database
Search facility to search recipes
Login/signup functionality to become a registered user
User profile page displaying users recipes only
Passwords are hashed so not shown on the database using the .gitignore file
Full CRUD functionality included
Custom 404/500 error pages

# Future implementations or contributions: 

The following features were considered during the build of the site, however due to time constraints, these were not included at the moment but could be added at a later date:

Ability to rate the favourite recipes. 
Pagination to ensure not too many recipes displayed in one page.
Displaying latest or featured recipes on homepage.

# Technologies used
Coding languages:

HTML5
CSS3
Javascript
Python (incl. Jinja)

Database:

MongoDB

Frameworks:

Materialize CSS
Flask
Jquery

Storing/editing/deploying Code:

Gitpod
Github
Heroku

Other:

Google Fonts
Font Awesome

# Deployment
The source code for this site is in GitHub. Heroku was used to deploy the site. MongoDB was used for the database.


MongoDB

The following collection was used for the recipes:

mongodb


GitHub

To clone the code from GitHub:

On GitHub, navigate to the main page of the repository.

Above the list of files, click Code:


To clone the repository using HTTPS, click HTTPS under "Clone".

Open Git Bash.

Change the current working directory to the location where you want the cloned directory.

Type git clone, and then paste the URL you copied earlier: $ git clone https://github.com/YOUR-USERNAME/Iacopo-Recipes

Press Enter to create your local clone.

Create your own env.py file to store variables, and ensure this is listed in your .gitignore file to keep these from being displayed publicly:

Import os
os.environ.setdefault("IP", "enter value")
os.environ.setdefault("PORT", "enter value")
os.environ.setdefault("SECRET_KEY", "enter value")
os.environ.setdefault("MONGO_URI", "enter value")
os.environ.setdefault("MONGO_DBNAME", "enter value")

# Deployment to Heroku

Setup files which Heroku needs in your terminal:

requirements.txt: tells Heroku which applications and dependencies are required to run our app.

Procfile: what Heroku looks for to know which file runs the app (use capital P for Procfile, and delete blank line at bottom of Procfile as may cause problems when running on Heroku).

setup files

Go to Heroku, once logged into your dashboard, click ‘Create new app’:
Create app name (must be unique, and generally use a 'dash' or 'minus' instead of spaces, and all lowercase letters):

app name

Choose region closest to you:

region

Then click ‘Create app’:

create app

Setup automatic deployment from your GitHub repository:

auto deploy

Make sure your GitHub profile is displayed:

profile

Then add your repository name:

repo name

Click ‘Search’:

search

Once it finds your repo, click 'Connect' to connect to this app:

connect

Click on ‘Settings’:

settings

Then click ‘Reveal Config Vars’

config

Then enter the variables (from the env.py) file to securely tell Heroku which variables are required:

IP
PORT
MONGO_DBNAME
MONGO_URI
SECRET_KEY
Push two new files (requirements.txt and Profile) to repository, in terminal, add/commit/push these:

push

Back in Heroku, can now safely ‘Enable Automatic Deployment’:

enable

Then ‘Deploy Branch’:

deploy

That should take a minute to build, once it's done, you'll see ‘Your app was successfully deployed.’ Click ‘View’ to launch your new app:

# Credits

Tutorials

I used the Code Institute Task Manger Mini-Project by Tim Nelson as the main basis of my own project.

Slack Community

I was able to resolve many issues encountered after searching on Slack in the Code Institute community.

All images are taken from Pixabay website. 
The website has been created for educational purposes only, it does not intend to be used for commercial purposes.

My Mentor:
Code Institute mentor:

Research:

I used the BBC website to search for the recipe descriptions and ingredients.

