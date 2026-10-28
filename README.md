# Project 4: Potting Parlour
Potting Parlour is an e-commerce platform which allows users to buy plants and track key activities such as watering, light exposure, and owned plants. 

## Table of Contents 

- [Project Goals](#project-goals)
- [User Experience](#user-experience)
- [Design](#design)
- [Frameworks & Languages](#frameworks--languages)
- [Data Model](#data-model)
- [Security](#security)
- [Features](#features)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Code from External Sources](#code-from-external-sources)
- [Credits & Disclaimer](#credits-and-disclaimer)

## Project Goals
This web application will allow users to browse a shop selling various plants, purchase a plant and track activities relating to the plant once it has been purchased. A user can sign up to purchase plants and track additional activities, whilst store owners can add, edit and remove any listings on the site. 

### User Goals 
Users have the following goals: 
* Browse plants for sale 
* Purchase a plant 
* See order history 
* Track activities related to their purchases 

### Site Goals 
Site maners have the following goals: 
* Add, edit or remove plants for sale 

## User Experience 
This section shows the considerations for each type of user that would use the website and the experiences they would have.

### Target Audience 
The target audience for this site are users who want to purchase plants and track the activities to take care of them.

### Expectactions 
Users of the site can expect:
* Easy to use navigation
* Clear layout
* Links to everything described
* Responsiveness to view the site on any device

### User Stories
The following users and their user stories have been considered: 

| ID | User Type | User Persona | User Stories |
|:---|:---|:---|:---|
| User 1 | Visitor | A visitor is someone who is browsing the store but is not logged into an account. | <ul><li>As a visitor, I want to see a list of all plants available for sale so that I can purchase plants.</li><li>As a visitor, I want to see details of the plants for sale, such as image, price, description, watering frequency, light, humidity and pet safety, so that I can make an informed decision on the plants I would like to purchase.</li><li>As a visitor, I want to be able to search for products by name so that I can find a specific plant.</li><li>As a visitor, I want to be able to filter by price, watering frequency, light, humidity and pet safety, and sort the results, so that I can find specific plants.</li><li>As a visitor, I want to be able to add products to a basket so that I can buy them.</li><li>As a visitor, I want to change the quantity of items in my basket so that I can order multiple plants.</li><li>As a visitor, I want to see a running total of my basket so that I can track my current spend.</li><li>As a visitor, I want to sign up for an account so that I can have access to more features.</li><li>As a visitor, I want to be redirected sensibly if I try to access a protected page so that I understand what further authentication is needed.</li></ul> |
| User 2 | Shopper | A shopper is someone who is logged into the store and looking to buy a plant. | <ul><li>As a shopper, I want to buy plants securely so that I know my payment is secure.</li><li>As a shopper, I want notifications for any actions I take so that I am aware of my actions on the site.</li><li>As a shopper, I want a clear success page after purchase so that I know my order went through.</li><li>As a shopper, I want a clear message if my payment has failed so that I know what to do next.</li><li>As a shopper, I want my delivery details saved so that I can check out quicker in the future.</li><li>As a shopper, I want to see my order history so that I can look at previous orders.</li><li>As a shopper, I want a loading screen during checkout so that I know something is happening.</li><li>As a shopper, I want to edit my details so that I can keep my personal information up to date.</li></ul> |
| User 3 | Plant Owner | A plant owner is someone who has purchased a plant from the store through a logged-in account. | <ul><li>As a plant owner, I want a dashboard showing key details about my plants so that I can quickly understand their health.</li><li>As a plant owner, I want to mark a plant as watered so that I know when I last watered it.</li><li>As a plant owner, I want to add a nickname to my plant so that I can tell my plants apart.</li><li>As a plant owner, I want to see the plant history so that I understand what has happened to the plant.</li><li>As a plant owner, I want to see the ideal conditions for my plant so that I can take care of it.</li><li>As a plant owner, I want to remove a plant so that it does not clutter my dashboard if I no longer have it.</li></ul> |
| User 4 | Shop Owner | A shop owner is someone who manages the stock available in the store. | <ul><li>As a shop owner, I want to add entries so that I can manage my store.</li><li>As a shop owner, I want to edit entries so that I can manage my store.</li><li>As a shop owner, I want to remove entries so that I can manage my store.</li></ul> |

## Design 
This section shows the design choices I made as part of the design of this website, alongside wireframes to show the rough layout of each page before construction of the website. Through all these choices, I have considered the 5 planes of user experience to ensure a smooth and enjoyable experience for all users of the site.

### Fonts, Colours and Structure 
The colour theme of this site is as follows:

|Colour|Hex Code|Description   |
|:-----|:-------|:-------------|
|Dark green|`#2F4A3A`|Primary colour|
|Deep forest green|`#243B2D`|Hover colour|
|Sage green|`#5C7A66`|Secondary green for accents where necessary|
|Pale pink|`#F4DDD9`|Primarily backgrounds or contract|
|Dusty pink|`#E8C4BE`|Secondary pink for hovers|
|Tan|`#C9B08A`|Second background colour |
|Sand|`#EADFCB`|Secondary tan|
|Cream|`#FBF8F4`|When clear backgrounds are required|
|Charcoal green|`#1F2A24`|Body text|
|Grey green|`#5F6B64`|Secondary text|
|Stone|`#E3DCD2`|For dividers|
|Leaf green|`#3E8E5A`|Success messages|
|Amber|`#D9962B`|Warning messages|
|Brick red|`#C0443A`|Error messages|
|Steel blue|`#4A7C9B`|Infomation|

There are two fonts used through this site:

* Yeseva One for headings and key text
* Josefin Sans for blocks of text and information

The site will have the following pages:

### Wireframes 
This section shows the wireframes for each page created in this web application across mobile, tablet and desktop screens. 

[section for each wireframe]

## Frameworks and Languages 
This section highlights all the languages and frameworks used in this project. 

[list frameworks and languages used in project]

## Data Model
In this project, my application will utilise a PostgreSQL database provided by the Code Institute. I have created the following tables and provided a graphical representation of how they are connected. 

[ add entity relationship diagram and explanations of data tables]

## Security 

[ add all security measures taken ]

## Features
This section outlines key features on each page. 

[ add common and page specific features ]

## Testing 

[ add separate file for testing ]

## Bugs 
The following bugs occured during the design of this site: 

[ add bugs as found ]

## Deployment 
For the version control, deployment, file storage and hosting of this site I have used GitHub, AWS S3 and Heroku.

### Cloning the Repository 
To take your own version of this repository, you will have to use the following steps: 

1. Select the fork button in the top right corner of the repository and add to your own 
2. Clone the repository using the green 'Code' button 
3. Copy the repository URL to your clipboard
4. Open your terminal and run: git clone [REPOSITORY URL] 
5. Change into the project directory 

This should mean you have a local copy of the repository to edit. 

### Setting up a Bucket in AWS S3

[ to add once completed ]

### Deploying to Heroku
The live version of this site is hosted using Heroku. To deploy your own version of the application, you need to use the following steps: 

1. Set up a Heroku account and log in
2. Select 'New' in the top right and create new app
3. Name your app and choose the correct region before selecting create app 
4. Edit the config vars section within the settings tab with your unique SECRET_KEY, DATABASE_URL and any other unique variables you have includued in your project
5. In the deploy tab, choose GitHub as your deployment method 
6. Choose the correct repository and ensure the correct branch is selected (usually main)
7. Use the 'deploy branch' button in the manual deployments section and let this run
8. Use the open app button to launch the application

Please note, within your allowed hosts within settings.py of your application, you should have '.herokuapp.com' or else this will not deploy. 

## Code from External Sources 
The following packages have been used in this project, and are also listed in requirements.txt: 

[ any additional code from external sources ]

## Credits and Disclaimers
I have the following credits and disclaimers: 