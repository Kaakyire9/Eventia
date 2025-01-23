# Eventia

![eventia responsive screenshot](documentation/final_views/eventia_amiresponsive.png)

# Introduction
Eventia is a user-friendly event management application designed for anyone looking to create or explore events effortlessly. Developed as part of the Code Institute's Full-Stack Developer course, this project showcases proficiency in Django and Bootstrap frameworks, database management, and CRUD functionality. Eventia serves as a third milestone project in the course, built exclusively for educational purposes.

Experience the live site here: [Eventia](https://eventia-dfe1ce6afa74.herokuapp.com/)  

For Admin access with relevant sign-in information: [Eventia Admin](https://eventia-dfe1ce6afa74.herokuapp.com/admin/)

<hr>

## Table of Contents

- [Eventia](#eventia)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
- [UX - User Experience](#ux---user-experience)
  - [Design Inspiration](#design-inspiration)
    - [Colour Scheme](#colour-scheme)
    - [Font](#font)
- [Project Planning](#project-planning)
  - [Strategy Plane](#strategy-plane)
    - [Site Goals](#site-goals)
  - [Agile Methodologies - Project Management](#agile-methodologies---project-management)
    - [MoSCoW Prioritization](#moscow-prioritization)
    - [Sprints](#sprints)
  - [User Stories](#user-stories)
    - [Visitor User Stories](#visitor-user-stories)
    - [Epic - User Profile](#epic---user-profile)
    - [Epic - Articles](#epic---articles)
    - [Epic - Booking](#epic---booking)
    - [Epic - Photo Gallery](#epic---photo-gallery)
    - [Epic - Visit Us/Reviews](#epic---visit-usreviews)
  - [Scope Plane](#scope-plane)
  - [Structural Plane](#structural-plane)
  - [Skeleton \& Surface Planes](#skeleton--surface-planes)
    - [Wireframes](#wireframes)
    - [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
    - [Security](#security)
- [Features](#features)
  - [User View - Registered/Unregistered](#user-view---registeredunregistered)
  - [CRUD Functionality](#crud-functionality)
  - [Feature Showcase](#feature-showcase)
  - [Future Features](#future-features)
- [Technologies \& Languages Used](#technologies--languages-used)
  - [Libraries \& Frameworks](#libraries--frameworks)
  - [Tools \& Programs](#tools--programs)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project Setup](#django-project-setup)
  - [Cloudinary API](#cloudinary-api)
  - [Elephant SQL](#elephant-sql)
  - [Heroku deployment](#heroku-deployment)
  - [Clone project](#clone-project)
  - [Fork Project](#fork-project)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
    - [Additional reading/tutorials/books/blogs](#additional-readingtutorialsbooksblogs)
  - [Acknowledgements](#acknowledgements)

## Overview 

Eventia is a dynamic event management platform designed to connect event organizers and attendees in a seamless, interactive environment. Users are invited to:

- Join the Eventia community
- Create personalized profiles with display pictures
- Customize their experience with password management and theme preferences
- Discover and engage with upcoming events
- Interact with events through likes and comments
- Track event countdowns
- Request attendance to events

Organize and manage events (for event creators)
Eventia is fully responsive and accessible across all modern web browsers, ensuring a smooth user experience on various devices. The platform aims to foster a vibrant community of event enthusiasts and organizers, facilitating meaningful interactions and efficient event management.
Key features of Eventia include:
- User authentication and profile customization
- Event discovery and interaction (liking, commenting, attendance requests)
- Event creation and management for organizers
- Real-time event countdowns
- Attendance approval system for organizers
- Engagement tracking (likes, comments, attendee counts)

Eventia addresses the growing need for a centralized, user-friendly event management solution. It simplifies the process of organizing and attending events, while building a community of like-minded individuals. Future developments may include integrated payment systems, advanced search and filtering options, and enhanced social networking features to further connect users with shared interests.

# UX - User Experience

## Design Inspiration

![eventia main logo](documentation/final_views/eventia_logo1.png)
*Inspired by the Universal presence of microphones at various event & power of Gold color*

I drew inspiration from leading event management platforms like Cvent and Eventbrite when conceptualizing Eventia. These industry leaders, recommended by Perplexity AI, provided valuable insights into the essential features and user experience for a successful event management platform.

The name "Eventia" was chosen as a creative play on the word "Event," designed to be both memorable and indicative of the platform's purpose. It conveys a sense of excitement and professionalism, aligning perfectly with our mission to facilitate exceptional event experiences.

Collaborating with talented graphic designer Mr. Adofo Beckson, we developed a distinctive and meaningful logo for Eventia. The logo cleverly incorporates a microphone in place of the letter 'i', symbolizing the universal presence of microphones at various events. This design element not only adds visual interest but also reinforces the platform's connection to live events and public gatherings.

We chose a luxurious pure gold color scheme for the logo and key design elements. This color choice represents excellence, prestige, and the high-quality experience we aim to provide through Eventia. The golden hue also evokes a sense of celebration and success, which aligns well with the spirit of events hosted on our platform.

Eventia aims to combine the best features of established platforms with innovative solutions, creating a user-friendly, comprehensive event management experience for both organizers and attendees.

### Colour Scheme

For Eventia, we carefully selected a color palette that embodies professionalism, trust, and excitement. Our chosen colors are:
- Deep Blue ```#094174``` : Represents trust and professionalism 
- Teal ```#1A5F7A``` : Evokes a sense of balance and stability
- Gold ```#EBBA0A```: Symbolizes celebration and success
- Light Blue ```#C1D6DF```: Provides a calming contrast
This color scheme creates a harmonious blend that reflects Eventia's commitment to delivering exceptional event experiences. The deep blue and teal colors convey reliability and sophistication, while the gold accent adds a touch of luxury and celebration. The light blue offers a refreshing contrast, enhancing readability and user experience.
Importantly, our color palette has passed the Color Blind Safe check on [Adobe Color](https://color.adobe.com/), ensuring that Eventia's design is accessible to users with various forms of color vision deficiency. This commitment to accessibility aligns with our goal of creating an inclusive platform for all event organizers and attendees.

![eventia color pallete](documentation/final_views/eventia_color_pallete.jpeg)
*Colour Scheme pallete for Eventia website*

![eventia color pallete](documentation/final_views/eventia_color_conflict.png)
*Accessibility checks for Eventia website colour scheme*

### Font
For Eventia, two complementary [Google Fonts](https://fonts.google.com/) was carefully selected to enhance the user experience and reflect the platform's professional yet approachable nature:

#### Roboto Slab Designed by Christian Robertson for Google
*Main Body Font*
- Chosen for its excellent readability and modern slab-serif style
- Conveys a sense of reliability and professionalism, aligning with Eventia's commitment to delivering high-quality event management services.

![eventia main font Roboto](documentation/final_views/eventia_main_font_Roboto.png)

#### Smooch Sans Created by Fontsmiths and Sabrina Mariela Lopez
*Heading Font*
- Selected for its playful yet elegant sans-serif design
- Adds a touch of creativity and excitement, mirroring the diverse range of events hosted on Eventia

![eventia heading font Smooch](documentation/final_views/eventia_head_smooch_font.png)

The combination of Roboto Slab's sturdy structure and Smooch Sans' dynamic character creates a perfect balance between professionalism and creativity. This pairing reflects Eventia's dual focus on providing a reliable platform for event organizers while celebrating the unique and exciting nature of each event.

# Project Planning  

The goal of Eventia was to create a comprehensive event management platform that simplifies the process of organizing and attending events. The 'product' is a user-friendly interface for event creation, management, and attendance, while the 'users' are event organizers, attendees, and enthusiasts.

The aim was to develop an intuitive system that streamlines event planning and participation. Through careful planning and design, an opportunity was recognized to transform Eventia into more than just a booking platform – it became a vibrant community for event lovers.

A social element naturally evolved, allowing users to share experiences, like events, and engage in discussions through comments. This fosters a dynamic community of event-goers who can recommend events to others, share exciting upcoming gatherings, and attract more users to join the platform.

Following modern design trends, an elegant color scheme was incorporated, featuring deep blue, teal, and gold, complemented by intuitive icons and high-quality imagery. The result is an attractive, user-centric platform that not only facilitates event management but also creates a thriving ecosystem for event enthusiasts.
 
## Strategy Plane
- Create a user-friendly platform for event organizers and attendees.
- Utilize a professional color scheme of deep blue, teal, and gold to identify connected features, with ample white space for clarity and focus.
- Implement recognizable icons with custom designs to fit the event management theme.
- Provide an intuitive UI for efficient CRUD functionalities related to events and user interactions.
- Ensure consistent UX across mobile, tablet, and desktop devices.
- Develop a scalable platform to accommodate future features and business growth.

The goals for Eventia focus on creating a professional, easy-to-use event management system that caters to both organizers and attendees. The color scheme and design elements are chosen to convey trust and excitement, while the user interface is designed for efficiency across all devices. The platform's scalability allows for future enhancements to meet evolving user needs and expand the business.

## Agile Methodologies - Project Management
Eventia marks my third experience with Agile planning methods, and I've found that my proficiency and comfort with this approach have significantly improved. As someone who values thorough preparation and planning, I've come to appreciate the flexibility and efficiency that Agile methodologies offer.

For this project, I utilized the [Github Projects Board](https://github.com/users/Kaakyire9/projects/9/views/1) to plan and document all aspects of my work. This tool has proven invaluable in organizing tasks, tracking progress, and maintaining a clear overview of the project's development.

With each iteration of using Agile methodologies, I've refined my process and gained deeper insights into effective project management. This third experience has allowed me to implement lessons learned from previous projects, resulting in a more streamlined and efficient development process for Eventia.

The Github Projects Board has been instrumental in breaking down the project into manageable tasks, prioritizing features, and maintaining a steady workflow. It has also facilitated better collaboration and transparency throughout the development process.

As I continue to embrace Agile methodologies, I look forward to further enhancing my project management skills and delivering even more successful outcomes in future endeavors.

### MoSCoW Prioritization

I chose to follow the MoSCoW Prioritization method for Eventia, identifying and labelling my:

- **Must Haves**: the 'required', critical components of the project. Completing my 'Must Haves' helped me to reach the MVP (Minimum Viable Product) for this project early, allowing me to develop the project further than originally planned.
  
- **Should Haves**: the components that are valuable to the project but not absolutely 'vital' at the MVP stage. The 'Must Haves' must receive priority over the 'Should Haves'.
- **Could Haves**: these are the features that are a 'bonus' to the project, it would be nice to have them in this phase, but only if the most important issues have been completed first and time allows.
- **Won't Haves**: the features or components that either no longer fit the project's brief or are of very low priority for this release. 

### Sprints

I divided the available time before project submission into sprints, aiming to complete the MVP for Eventia by January 22, 2025. This timeline was set considering the project's complexity and my goal to have the core functionalities implemented well before the final submission date of January 28, 2025.

As this is my first project using database schemas and Django, I anticipated potential challenges and allocated extra time for troubleshooting and learning. The project commenced on January 9, 2025, at 8 AM, giving me approximately three weeks to develop, test, and refine the platform.

I organized my work into three main categories:
- Dev (Developer) Tasks
- User Stories
- Testing Tasks

These were converted into issues and fully labeled on my Github Projects Board. Adding comments to issues proved invaluable, allowing me to quickly record information, sources, and fixes for later reference in my README.

My sprints represent general timeframes of focus on specific areas. Given the nature of balancing project work with other commitments, some sprint timeframes overlapped as I worked on the project during every available moment.

Despite being my first experience with Django and database schemas, I've made significant progress. The learning curve has been steep, but rewarding. I've encountered and overcome various challenges, particularly in setting up the database and implementing complex features like the event management system.

As of today, January 22, 2025, I'm pleased to report that the project is on track. The core functionalities are in place, and I'm now focusing on refining the user interface and conducting thorough testing. This leaves me with a comfortable buffer before the final submission date to address any unforeseen issues and potentially add extra features if time permits.
This sprint-based approach has not only helped me manage the project effectively but has also deepened my understanding of Agile methodologies in practice.

|Sprint No.|	Sprint Content|	Start/Finish Dates|
|----------|----------------|-------------------|
| #1 |	Project Setup and Basic Models|	Jan 9, 2025 - Jan 12, 2025|
| #2 |	User Authentication and Profiles|	Jan 13, 2025 - Jan 15, 2025|
| #3 |	Event Creation and Management|	Jan 16, 2025 - Jan 18, 2025|
|#4|	Event Detail Page and Interactions|	Jan 19, 2025 - Jan 21, 2025|
|#5|	Comments and Likes Functionality|	Jan 22, 2025 - Jan 24, 2025|
|#6|	Attendance Request and Approval System|	Jan 25, 2025 - Jan 26, 2025|
|#7|	Final Testing and Bug Fixes|	Jan 27, 2025 - Jan 28, 2025|




## Libraries & Frameworks

- asgiref==3.8.1
- cloudinary==1.42.1
- dj-database-url==0.5.0
- Django==4.2.17
- django-allauth==0.57.2
- django-cloudinary-storage==0.3.0
- django-summernote==0.8.20.0
- django-widget-tweaks==1.5.0
- gunicorn==20.1.0
- oauthlib==3.2.2
- pillow==11.1.0
- psycopg2-binary==2.9.10
- PyJWT==2.10.1
- python3-openid==3.2.0
- requests-oauthlib==2.0.0
- sqlparse==0.5.3
- whitenoise==5.3.0

Further information is available in the [requirements.txt file](requirements.txt)

## Tools & Programs

- [GitHub Copilot](https://github.com/features/copilot) for providing AI-powered code suggestions and assistance.
- [Perplexity AI](https://www.perplexity.ai/) for breaking down Python concepts and Django documentation into more understandable chunks.
- [Convertio](https://convertio.co/) for file conversion to PNG, WEBP.
- [Tiny Png](https://tinypng.com/) for file size reduction.
- [Lucidchart](https://www.lucidchart.com/pages) for ERD (entity relationship diagram) creation.
- [Trello](https://www.trello.com) for intial project agile planning.

- [Pattern Monster](https://pattern.monster/) for the hero image pattern SVG.
- [Favicon](https://favicon.io/) for converting an icon into favicon.
- [LogoAI](https://www.logoai.com/) for design inspiration using my font and colour choices.

# Testing

- For all testing, please refer to the [TESTING.md](TESTING.md) file.

# Deployment
  
## Connecting to GitHub  

To begin this project from scratch, you must first create a new GitHub repository using the [Code Institute's Template](https://github.com/Code-Institute-Org/ci-full-template). This template provides the relevant tools to get you started. To use this template:

1. Log in to [GitHub](https://github.com/) or create a new account.
2. Navigate to the above CI Full Template.
3. Click '**Use this template**' -> '**Create a new repository**'.
4. Choose a new repository name and click '**Create repository from template**'.
5. In your new repository space, click the purple CodeAnywhere (if this is your IDE of choice) button to generate a new workspace.

## Django Project Setup

1. Install Django and supporting libraries: 
   
- ```pip3 install 'django<4' gunicorn```
- ```pip3 install dj_database_url psycopg2```
- ```pip3 install dj3-cloudinary-storage```  
  
2. Once you have installed any relevant dependencies or libraries, such as the ones listed above, it is important to create a **requirements.txt** file and add all installed libraries to it with the ```pip3 freeze --local > requirements.txt``` command in the terminal.  
3. Create a new Django project in the terminal ```django-admin startproject ems .```
4. Create a new app eg. ```python3 mangage.py startapp events```
5. Add this to list of **INSTALLED_APPS** in **settings.py** - 'events',
6. Create a superuser for the project to allow Admin access and enter credentials: ```python3 manage.py createsuperuser```
7. Migrate the changes with commands: ```python3 manage.py migrate```
8. An **env.py** file must be created to store all protected data such as the **DATABASE_URL** and **SECRET_KEY**. These may be called upon in your project's **settings.py** file along with your Database configurations. The **env.py** file must be added to your **gitignore** file so that your important, protected information is not pushed to public viewing on GitHub. For adding to **env.py**:

- ```import os```
- ```os.environ["DATABASE_URL"]="<copiedURLfrompostgresqlL>"```
- ```os.environ["SECRET_KEY"]="my_super^secret@key"```
  
For adding to **settings.py**:

- ```import os```
- ```import dj_database_url```
- ```if os.path.exists("env.py"):```
- ```import env```
- ```SECRET_KEY = os.environ.get('SECRET_KEY')``` (actual key hidden within env.py)  

9. Replace **DATABASES** with:

```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
```

10. Set up the templates directory in **settings.py**:
- Under ``BASE_DIR`` enter ``TEMPLATES_DIR = os.path.join(BASE_DIR, ‘templates’)``
- Update ``TEMPLATES = 'DIRS': [TEMPLATES_DIR]`` with:

```
os.path.join(BASE_DIR, 'templates'),
os.path.join(BASE_DIR, 'templates', 'allauth')
```

- Create the media, static and templates directories in top level of project file in IDE workspace.

11. A **Procfile** must be created within the project repo for Heroku deployment with the following placed within it: ```web: gunicorn ems.wsgi```
12. Make the necessary migrations again.

## Cloudinary API 

Cloudinary provides a cloud hosting solution for media storage. All users uploaded images in the FreeFid project are hosted here.

Set up a new account at [Cloudinary](https://cloudinary.com/) and add your Cloudinary API environment variable to your **env.py** and Heroku Config Vars.
In your project workspace: 

- Add Cloudinary libraries to INSTALLED_APPS in settings.py 
- In the order: 
```
   'cloudinary_storage',  
   'django.contrib.staticfiles',  
   'cloudinary',
```
- Add to **env.py** and link up with **settings.py**: ```os.environ["CLOUDINARY_URL"]="cloudinary://...."``` 
- Set Cloudinary as storage for media and static files in settings.py:
- ```STATIC_URL = '/static/'```
```
  STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'  
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]  
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')‌  
  MEDIA_URL = '/media/'  
  DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

## Elephant SQL

A new database instance can be created on [Elephant SQL](https://www.elephantsql.com/) for your project. 

- Choose a name and select the **Tiny Turtle** plan, which is free.
- Select your Region and the nearest Data Center to you. 
- From your user dashboard, retrieve the important 'postgres://....' value. Place the value within your **DATABASE_URL**  in your **env.py** file and follow the below instructions to place it in your Heroku Config Vars.


## Heroku deployment

To start the deployment process , please follow the below steps:

1. Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
2. Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
3. Enter an app name and choose your region. Click '**Create App**'. 
4. In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. The KEY:VALUE pairs that you will need are your: 
   
   - **CLOUDINARY_URL**: **cloudinary://....** 
   - **DATABASE_URL**:**postgres://...** 
   - **DISABLE_COLLECTSTATIC** of value '1' (N.B Remove this Config Var before deployment),
   -  **PORT**:**8000**
   -  **SECRET_KEY** and value  
  
5. Add the Heroku host name into **ALLOWED_HOSTS** in your projects **settings.py file** -> ```['800-nielmc-django-project-lxqprmm3qz.us2.codeanyapp.com', '.herokuapp.com', 'localhost', '127.0.0.1'].```
6. Once you are sure that you have set up the required files including your requirements.txt and Procfile, you have ensured that **DEBUG=False**, save your project, add the files, commit for initial deployment and push the data to GitHub.
7. Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
8. Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
9.  Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Manual' deployment method. Click '**Deploy Branch**'.
10. Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site. If you receive any errors, Heroku will display a reason in the app build log for you to investigate. **DISABLE_COLLECTSTATIC**  may be removed from the Config Vars once you have saved and pushed an image within your project, as can **PORT:8000**.

## Clone project

A local clone of this repository can be made on GitHub. Please follow the below steps:

1. Navigate to GitHub and log in.
2. The [Eventia Repository](https://github.com/Kaakyire9/Eventia) can be found at this location.
3. Above the repository file section, locate the '**Code**' button.
4. Click on this button and choose your clone method from HTTPS, SSH or GitHub CLI, copy the URL to your clipboard by clicking the '**Copy**' button.
5. Open your Git Bash Terminal.
6. Change the current working directory to the location you want the cloned directory to be made.
7. Type `git clone` and paste in the copied URL from step 4.
8. Press '**Enter**' for the local clone to be created.
9. Using the ``pip3 install -r requirements.txt`` command, the dependencies and libraries needed for FreeFido will be installed.
10. Set up your **env.py** file and from the above steps for Cloudinary and ElephantSQL, gather the Cloudinary API key and the Elephant SQL url for additon to your code.
11. Ensure that your **env.py** file is placed in your **.gitignore** file and follow the remaining steps in the above Django Project Setup section before pushing your code to GitHub.

## Fork Project

A copy of the original repository can be made through GitHub. Please follow the below steps to fork this repository:  

1. Navigate to GitHub and log in.  
2. Once logged in, navigate to this repository using this link [Eventia Repository](https://github.com/Kaakyire9/Eventia).
3. Above the repository file section and to the top, right of the page is the '**Fork**' button, click on this to make a fork of this repository.
4. You should now have access to a forked copy of this repository in your Github account.
5. Follow the above Django Project Steps if you wish to work on the project.








## Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/40879804/91578d7d-dc67-46c1-9847-33ee283695c6/paste.txt

[2] https://www.cvent.com/uk

[3] https://www.eventbrite.co.uk

[4] https://color.adobe.com/

[5] https://fonts.google.com/specimen/Smooch+Sans

[6] https://github.com/users/Kaakyire9/projects/9/views/1

## Acknowledgements

- [Favicon](https://favicon.io/) for converting an icon into favicon.
- [GitHub Copilot](https://github.com/features/copilot) for providing AI-powered code suggestions and assistance.