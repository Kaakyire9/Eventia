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








## Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/40879804/91578d7d-dc67-46c1-9847-33ee283695c6/paste.txt

[2] https://www.cvent.com/uk

[3] https://www.eventbrite.co.uk

[4] https://color.adobe.com/

[5] https://fonts.google.com/specimen/Smooch+Sans

[6] https://github.com/users/Kaakyire9/projects/9/views/1