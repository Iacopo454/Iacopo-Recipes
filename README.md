## Milestone 3- Iacopo Recipes book 
I am building my recipe book website which will also contains user recipes and so this will be a sharing recipe database website. 

## Index 
# UX
.
Overview

The aim of the project is to design a recipe website containing a database of quick, easy family meals. The website is designed to cater to those specifically looking for recipes which fit this criteria, for example busy parents who don't have time or energy to think about dinner, or prepare complicated meals for their family! As this website will contain an active database, there will be an option for users to signup to add their own recipes. The website is designed to be suitable for use on all devices, from desktop to mobile.


# User Stories

I want the website to be intuitive, so I can get an impression of what it does from first glance.
I want the website to be visually appealing and well presented.
I want the recipe listing feature to be searchable, so I can search for specific recipes I may be interested in.
I want an easy way to login or signup to the website.
I want it to be easy to add/edit a recipe

# Strategy

The primary goal is to provide a searchable database of recipes for website users, which is visually appealing, and easy to use.

Scope

The overall look and feel of the website was influenced by researching similar websites (credits at end):

These are simple/clean in design.
Recipes are displayed in a grid of "cards" consisting of an image and recipe title, clicking on a recipe card takes you to the recipe details page.
There is a facility to search recipes.
There is a facility to login/register to the site, which then takes you to your profile page.
With this in mind, my website will include:

A homepage with some details about the website, some featured recipes, and links to sign in or register (included to give an overview of the site, and make it intuitive for the user).
A searchable recipes page, which will display the recipes in a "card" or grid format.
Clicking on the recipe "card" will bring up that particular recipe's details page, including the ingredients/method.
A login/sign up page.
Once logged in, the user will be directed to their user profile page, which will give the user options to add/edit their own recipes.
Structure

In line with the features identified in the scope section, the website will be structured as follows:

Homepage:

Navbar at top, showing website title/logo, and links to other pages (fixed/featured on all pages for familiarity/ease of use).
Hero image with text explaining the purpose of the site.
Links to log in or sign in.
Footer showing social media links (fixed/featured on all pages for familiarity/ease of use).
This page has been included/designed in this way to give the user an effective snapshot of the site, you can see all the main features of the site from looking at this page:
Introductory text and hero image "explain" the sites purpose.
The sign in/log in links show that this is a interactive/sharing site, the accompanying text will encourage the user to do so.
Recipes:

A search feature at the top of the page.
Recipes displayed via "cards" or thumbnails, consisting of the recipe image/recipe title, in a grid format.
Recipe Details:

Will include all recipe details including ingredients, method, added by, prep time, servings.
Login/Sign Up:

The log in and sign up pages will be the same, requiring the user to input username/password.
Profile:

Will include the facility to add users own recipes, as well as edit any recipes already submitted.

# Skeleton

Wireframes - includes sitemap and database schema

# Surface

The colour scheme will be influenced from the research detailed in the scope section above.
The websites tend to use simple colour schemes, with green/teal often being used.
Green is associated with being peaceful and healthy, which is perfect for this site, so this colour will be used in my site for any main features. Source: CrazyEgg
A clear, easy to read, friendly style of font was wanted, I decided on a combination of Open Sans/Roboto (Google Fonts) as I thought these fonts meet these particular requirements.

# Feature
Existing

The website uses Materialize CSS features:

Navbar (top navbar)
Sidenav (to turn into sidenav on mobile)
Cards (to display recipes)
Forms (to add/edit recipes)
Buttons (for links to other pages and add/edit/delete actions)
Footer (bottom footer)
Tooltip (to display message on delete button)
Chips (to display some recipe info)
In addition the following features are used:

Site linked to MongoDB database
Search facility to search recipes
Login/signup functionality to become a registered user
User profile page displaying users recipes only
Passwords are hashed so not shown on the database
Full CRUD functionality included
Custom 404/500 error pages

Left to Implement

The following features were considered during the build of the site, however due to time constraints, these were not included in this version, but could be added at a later date:

Ability to rate/mark a recipe as a favourite.
Introducing recipe categories e.g. vegetarian/quick/easy etc, which can then be filtered.
Pagination to ensure not too many recipes displayed on 1 page.
Displaying latest or featured recipes on homepage.
See unresolved bugs section in Testing for further features left to implement.

# Technologies used
Languages:

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

Type git clone, and then paste the URL you copied earlier: $ git clone https://github.com/YOUR-USERNAME/MS3_EasyDinner.git

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

I was able to resolve many issues encountered after searching on Slack in the Code Institute community, the following in particular have posted content which I found useful:

Ed Bradley
Igor Basuga
Daniel Hayes
Malia Havlicek
Heather Olcot
Antonio Augello
I would also like to thank the Slack peer-code-review community for reviewing my project.

Student Projects

Self Isolution
Wean Cuisine
McTastic Recipes
Images

Hero image on homepage from Pixabay.

Recipe images from Hello Fresh.

(Website created for educational purposes only, not intended to be used for commercial purposes)

Mentor

Code Institute mentor Akshat Garg.

Research

I used the following websites as a reference in the design process:

Hello Fresh
Delicious Magazine
