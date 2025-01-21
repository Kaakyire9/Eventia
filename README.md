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







Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/40879804/91578d7d-dc67-46c1-9847-33ee283695c6/paste.txt
[2] https://www.cvent.com/uk
[3] https://www.eventbrite.co.uk