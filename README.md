# Project 4: Potting Parlour
Potting Parlour is an e-commerce platform which allows users to buy plants and track key activities such as watering, light exposure, and owned plants.

<img src="./media/potting-parlour.png">

You can access my site here: [Potting Parlour](https://potting-parlour-1a8970d57173.herokuapp.com/)

## Table of Contents

- [Project Goals](#project-goals)
- [User Experience](#user-experience)
- [Design](#design)
- [Frameworks & Languages](#frameworks-and-languages)
- [Data Model](#data-model)
- [Security](#security)
- [Features](#features)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Code from External Sources](#code-from-external-sources)
- [Credits & Disclaimer](#credits-and-disclaimers)

## Project Goals
This web application will allow users to browse a shop selling various plants, purchase a plant and track activities relating to the plant once it has been purchased. A user can sign up to purchase plants and track additional activities, whilst store owners can add, edit and remove any listings on the site.

### User Goals
Users have the following goals:
* Browse plants for sale
* Purchase a plant
* See order history
* Track activities related to their purchases

### Site Goals
Site managers have the following goals:
* Add, edit or remove plants for sale

## User Experience
This section shows the considerations for each type of user that would use the website and the experiences they would have.

### Target Audience
The target audience for this site are users who want to purchase plants and track the activities to take care of them.

### Expectations
Users of the site can expect:
* Easy to use navigation
* Clear layout
* Links to everything described
* Responsiveness to view the site on any device

### User Stories
The following users and their user stories have been considered:

| ID | User Type | User Persona | User Stories |
|:---|:---|:---|:---|
| User 1 | Visitor | A visitor is someone who is browsing the store but is not logged into an account. | <ul><li>As a visitor, I want to see a list of all plants available for sale so that I can purchase plants.</li><li>As a visitor, I want to see details of the plants for sale, such as image, price, description, watering frequency, light, humidity and pet safety, so that I can make an informed decision on the plants I would like to purchase.</li><li>As a visitor, I want to be able to search for products by name so that I can find a specific plant.</li><li>As a visitor, I want to be able to filter by price, watering frequency, light, humidity and pet safety, and sort the results, so that I can find specific plants.</li><li>As a visitor, I want to be able to add products to a basket so that I can buy them.</li><li>As a visitor, I want to change the quantity of items in my basket so that I can order multiple plants.</li><li>As a visitor, I want to see a running total of my basket so that I can track my current spend.</li><li>As a visitor, I want to sign up for an account so that I can have access to more features.</li><li>As a visitor, I want to be redirected sensibly if I try to access a protected page so that I understand what further authentication is needed.</li><li>As a visitor, I want to buy plants securely so that I know my payment is secure.</li><li>As a visitor, I want notifications for any actions I take so that I am aware of my actions on the site.</li><li>As a visitor, I want a clear success page after purchase so that I know my order went through.</li><li>As a visitor, I want a clear message if my payment has failed so that I know what to do next.</li><li>As a visitor, I want a loading screen during checkout so that I know something is happening.</li></ul> |
| User 2 | Shopper | A shopper is someone who is logged into the store and looking to buy a plant. | <ul><li>As a shopper, I want my delivery details saved so that I can check out quicker in the future.</li><li>As a shopper, I want to see my order history so that I can look at previous orders.</li><li>As a shopper, I want to edit my details so that I can keep my personal information up to date.</li></ul> |
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
|Pale pink|`#F4DDD9`|Primarily backgrounds or contrast|
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
|Steel blue|`#4A7C9B`|Information|

Using this [contrast evaluator](https://coolors.co/contrast-checker/3d3d3c-faf9f6), the background colour and text colour have a contrast score of 7.49 which is rated very good.

There are two fonts used through this site:

* Yeseva One for headings and key text
* Josefin Sans for blocks of text and information

The site will have the following pages:

* A home page
* A products page
* A product details page
* A login, sign up and sign out page
* A basket
* A checkout page
* A checkout confirmation
* An order history
* A tracking dashboard
* A tracking details page for a specific plant

There will also be notifications to reassure users an action has happened or they are notified of a blocked action.

### Wireframes
This section shows the wireframes for each page created in this web application across mobile, tablet and desktop screens.

#### Home
This is the landing page for the site.

<img src="./static/images/wireframe-home.png">

#### Plants
This page shows all the plants on sale on the site.

<img src="./static/images/wireframe-plants.png">

#### Plant Details
This page shows all the details for a chosen plant.

<img src="./static/images/wireframe-plant-detail.png">

#### Login / Signup / Signout
This page shows the general style of all authentication pages.

<img src="./static/images/wireframe-login.png">

#### Basket
This page shows how the basket will look once users add plants to purchase.

<img src="./static/images/wireframe-basket.png">

#### Checkout
This page shows how the checkout will look.

<img src="./static/images/wireframe-checkout.png">

#### Checkout Confirmation
This page shows how confirmation will look after submitting a payment.

<img src="./static/images/wireframe-confirmation.png">

#### Order History
This page shows previous orders for a logged in user.

<img src="./static/images/wireframe-history.png">

#### Tracking Dashboard
This page shows the orders and tracking details for a logged in user.

<img src="./static/images/wireframe-tracking.png">

#### Tracking Details
This page shows the tracking history of a specific plant for a logged in user.

<img src="./static/images/wireframe-tracking-details.png">

## Frameworks and Languages
This section highlights all the languages and frameworks used in this project.

The following languages were used:

* HTML
* CSS
* JavaScript
* Python

The following frameworks were used:

* Django Framework
* Bootstrap
* Google fonts
* Font Awesome
* Stripe payment intents and web parts

The application is deployed using Heroku with media stored in an AWS S3 bucket.

## Data Model
In this project, my application will utilise a PostgreSQL database provided by the Code Institute. I have created the following tables and provided a graphical representation of how they are connected.

<img src="./static/images/data-model.png">

|Table|Description|
|:----|:----------|
|User|Django user table for authentication|
|Profile|Additional data for profiles such as address and phone number for speedy checkout|
|Categories|Custom groupings to the plants on the site|
|Plant|All plants for sale and additional fields for care instructions|
|Order|The order details such as delivery address, costs and stripe pid|
|OrderLineItem|The specific plants bought in an order|
|OwnedPlant|A record of plants bought by a user and tracking fields to give a place to care for a plant|
|WateringLog|A record of each time a user marks a plant as watered and any notes associated with it at that time|

Relationships are shown by the lines joining the tables, with a 1 on each end meaning a one-to-one connection and a 1 and a cross on the end meaning a one-to-many connection.

## Security
This section outlines the measures taken to keep user data, payments and site content secure.

### Authentication and Authorisation
* Django Allauth handles registration, login and logout. Passwords are hashed by Django and never stored in plain text.
* Access control on protected pages: the tracker, profile and order history require login. Unauthenticated users are redirected to the login page with a message explaining why.
* Superuser-only actions: adding, editing and deleting plants is restricted to superusers. Standard users and visitors who try to access these URLs are redirected and shown an error toast.
* Ownership checks: users can only view and edit their own profile, orders and owned plants. Attempting to access another user's record returns a 404 / is denied.

### Payments
* Payments are processed by Stripe. Card details are entered into Stripe's secure form and are never stored on or passed through my server.
* A Stripe webhook with a signing secret verifies that payment events genuinely come from Stripe, so orders are still created if a user closes the browser mid-checkout and cannot be forged.
* Only the order number, delivery details and Stripe payment intent ID (PID) are stored in the database.

### Secrets and Environment Variables
* The secret key, database key, Stripe keys and AWS keys are stored in `env.py` locally and in Heroku Config Vars in production.
* `env.py` is listed in `.gitignore` so no credentials are committed to the repository.
* `DEBUG` is set to `False` in production, and `ALLOWED_HOSTS` is limited to the deployed domain and `.herokuapp.com`.

### Data Protection
* CSRF protection: all forms use Django's `{% csrf_token %}` and the CSRF middleware is enabled.
* SQL injection: all database access uses the Django ORM, which parameterises queries.
* Safe deletion: plants that have been purchased cannot be deleted and are marked inactive instead. This protects order history and data integrity.
* The PostgreSQL database and AWS S3 bucket are accessed by dedicated credentials. The S3 IAM user is limited to the project bucket only.

### Update: Secret Key Remediation
In an early commit, the Django default secret key was committed but before this was deployed using Heroku this was rotated and secured in the `env.py` file  which was included in a `.gitignore` and congig vars in Heroku, meaning there is no security impact due to the key being retired.

## Features
This section outlines key features on each page.

### Common Features
These features appear across all pages.

#### Navigation Bar
The navigation bar is featured on all pages and aims to apply consistent styling and position for all users, built with responsive design. The navigation bar displays different options based on a users authentication.

* For no authentication, users will see login, tracking and a basket
* For a standard user, users will see profile, tracking and a basket
* For a super user, users will see add products, profile, tracking and basket

<img src="./media/features/nav-bar.png">

#### Toasts
For any messages on the site, a pop up will appear in the top right corner with the message. This is also coloured depending on whether it is a successful action, a warning, an error or just information. These all have the same layout as pictured below.

<img src="./media/features/toasts.png">

#### Footer
The footer features links to key social media sites and is the same for all user types.

<img src="./media/features/footer.png">

### Page-Specific Details
The following sections highlight the key features on each page and how this differs depending on authentication.

#### Home
The home page has the same layout for all users, with the login button changing to a logout button if authenticated. This allows users to navigate to the plants available for sale or popular filtered selections such as shady, pet safe and low effort plants.

<img src="./media/features/index.png">

#### Plants
The plants page is the same for all users. The top of the page is made of a title, search bar and filtering options. Below that are tiles for each plant showing key information and selecting the picture or the arrow icon will take you to further details.

<img src="./media/features/plants.png">

#### Plant Details
The plants detail page shows all the information available for a plant. This has different buttons depending on the user:

* For unauthenticated users and standard users, there are options to add to basket and return to the previous page
* For super users, there are additional options to edit and delete the plant

<img src="./media/features/details.png">

#### Plant Edit
The Plant Add / Edit page is only accessible to super users and allows users to add new plants, edit existing plants or delete records. A super user cannot delete a record if someone has already bought that plant. Instead a super user would mark this as inactive so it does not appear on the site anymore but the records are retained for order history.

<img src="./media/features/add-plants.png">

#### Basket
The basket is the same for all users and shows what a user has added to their basket, including quantity of each plant, the price of an individual plant, the sub-total for that plant, the sub-total for all plants, the delivery fee (or lack of if meeting free delivery threshold) and the total price.

<img src="./media/features/basket.png">

#### Checkout
The checkout can be accessed by all users to input their details and buy the items in their basket. This has an input form on the left and the order details on the right with a large checkout button at the bottom. There is also a loading overlay to ensure users are aware their payment is underway.

<img src="./media/features/checkout.png">

#### Checkout Success
The checkout success is seen once a payment has been successful and shows the details of the order including the plants purchases and the delivery details.

<img src="./media/features/checkout-success.png">

#### Profile
Authenticated users can update their details in the profile tab. These details are saved for faster checkout on another purchase and will automatically fill out the checkout form on the users next purchase. The user also accesses their order history here and selecting an order number will take them to the checkout success page of that particular order.

<img src="./media/features/profile.png">

#### Tracker
Authenticated users will see the tracking dashboard for plants they have purchased. Here they can see the total plants they've purchased, the number of plants that need to be watered and details on each plant for any nicknames they have been given, when they were last watered and the option for more details.

<img src="./media/features/tracker.png">

#### Tracker Details
Authenticated users can see further details of the plant they have purchased. All details such as light, pet safety, humidity and care difficulty are recorded. There is a watering section telling users the watering frequency, when they bought the plant, the last watered date and the next watering date, alongside buttons to update the watering date to today or remove the plant if they no longer want to track it.

<img src="./media/features/tracker-details-1.png">

Further down the page, there is a form to add a nickname and any particular notes about the plant and a table displaying the watering history.

<img src="./media/features/tracker-details-2.png">

#### Authentication
Authentication pages (such as sign up, login, logout etc.) used allauth's base templates and features with modified styling to match my site design.

## Testing
I have tested my project through a combination of manual testing of user stories, Django testing and code-specific validators. Testing has been moved to a [testing file](./testing.md) and is ordered appropriately. Any bugs recorded throughout testing are captured in the bugs section.

## Bugs
The following bugs occurred during the design of this site:

|#|Bug|Fix|
|:-|:----|:----|
|1|Footer not sticking to bottom of page|Height tag in css was causing it and has been removed|
|2|Filters on plant page showing {{ label }}|html line breakage from using the VS code formatter causing errors|
|3|Friendly names not coming through for categories in filters|wrong name selected in django template|
|4|Unable to log into django admin once profile model was created|had to create new superuser and manually update the fields|
|5|Order models not showing up in admin|had to add them to checkout admin app|
|6|Checkout css not loading properly|wrong file path meant this was not linked|
|7|Crispy form not loading for profile.html|forgot to add the django tag at the top of the page|
|8|Add plant url not working|order of the plant urls was not aligned properly|
|9|Delete plant button not showing up on plant_form.html|missed plant in the context|
|10|Plants not showing for users in the tracker|context was not rendering properly in the view leading to Django not picking up the data|
|11|Completing an order as an auntenticated user made the view 404|last_order_number variable was not being set in the checkout but being called in checkout success|
|12|The basket page was not responsive|I had a position:absolute tab in my css which was causing the error and had to be replaced with position:relative|
|13|Inactive plants were showing in the view|I had missed a filter when creating the plant object in my view|

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

### Setting up Environment Variables
To host this project locally, you need to set up an env.py file to store your variables. In this project, you will need to define the following variables:

* Secret key - a unique key for your project
* Database key - a unique URL for your database
* Stripe Public Key - the public key for your stripe account
* Stripe Private Key - the private key for your stripe account
* Stripe WH Key - the webhook handler key for your stripe account

You will also need keys from your AWS bucket but these can be stored directly in Heroku. Please note, you <strong>must</strong> ensure this file is in your `.gitignore` so people will not find your project secrets and exploit them.

### Setting up a Bucket in AWS S3
The host your static files online, you need to undertake the following steps to set up an AWS S3 bucket.

#### Part 1: Creating an account
Firstly, you need to create an AWS account and set up a bucket:

1. Head to the [AWS site](https://aws.amazon.com/) and create an account
2. Navigate to the S3 section of AWS
3. Select create bucket
4. Enter a bucket name, enable ACLs, select 'Bucket Owner prefered', deselect 'block all public access' and acknowledge this and then scroll down to create bucket
5. Once created, select the bucket name to view the bucket details
6. Select properties
7. Scoll down to 'static website hosting' and select 'Edit'
8. Click enable, then enter 'index.html' in the index document input and 'error.html' in the error document input before saving changes
9. Next we have to change the CORS configuration. Head to permissions and scroll down to the Cross-origin resource sharing (CORS) section
10. Select 'edit'
11. Add the following code and save changes

```[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```

12. Now we add a bucket policy. Select the permissions tab, scroll to bucket policy and select 'Edit'
13. Add the following code, where [your chosen id] is an id you can create and [your arn] is the bucket arn that can be copied from above the editor

```{
    "Version": "2012-10-17",
    "Id": "[your chosen id]",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "[your arn]/*"
        }
    ]
}
```

14. Save the policy
15. On the permissions tab, scroll to Access control list and select 'Edit'
16. On the 'Edit Access control list' page, click 'list' in everyone and confirm you understand the changes before selecting save changes

#### Part 2: Creating Groups, Policies and Users
Now you have a bucket set up, you need to create a group, policy and user to access the files. We do this in the following steps:

1. Search IAM in the search bar and select IAM
2. Select 'User Groups' on the left-hand menu. Please note you may need to elevate your account for this.
3. Select create group
4. Enter a group name and select create user group
5. Select policies in the left-hand menu
6. Select create policy
7. Select the JSON tab
8. Select the Actions drop down
9. Select 'Import Policy'
10. Search for S3 and select 'AmazonS3FullAccess' before selecting 'Import Policy'
11. Copy your bucket ARN, and in the policy editor include the following code, replacing [your arn] with your copied bucket ARN

```{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": [
                "[your arn]",
                "[your arn]/*"
            ]
        }
    ]
}
```

12. Scroll down and select next
13. Give your policy a name and description
14. Select Create policy
15. Select User Group from the left-hand menu
16. Select your group
17. Select the permissions tab, click add permissions and select 'attach policies'
18. Search for your policy, select the checkbox next to it and click 'attach policies'
19. Select users from the left-hand menu
20. Select 'create user'
21. Enter a user name and select next
22. Select the group your previously created and select next
23. Scroll down and select 'Create User'

Now we have this setup, we need to generate our access keys. We do this by:

1. Selecting our new user
2. Selecting security credentials
3. Scroll down to the Access Keys section and select 'Create Access Key'
4. Select 'Application running outside of AWS' and select next
5. Select 'Create Access Key'
6. Scroll down and click 'Download .csv file'
7. Once saved, click done

Now you have the .csv file, you can open this in a text editor to view your AWS access key ID and AWS secret Access key. You will need both of these for your Heroku deployment so ensure you save them.

### Setting up Stripe
Stripe is used for the payments on this site. You can set up your own stripe account and connect to the project using the following:

#### API keys
1. Create a [Stripe account](https://stripe.com/gb) and log in.
2. In the dashboard, copy the publishable and secret keys.
3. Add them to `env.py` or Heroku config vars locally (STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY)

#### Webhooks: production
1. In the dashboard, open Webhooks > Add endpoint.
2. Select create destination
3. Select the events payment_intent.succeeded and payment_intent.payment_failed.
4. Set the endpoint URL to `https://<your-app>.herokuapp.com/checkout/wh/`.
4. After saving, copy the endpoint's signing secret and set it as the `STRIPE_WH_SECRET` config var on Heroku.
5. Test mode and live mode have separate keys and separate endpoints. Repeat these steps in live mode before taking real payments.

#### Verifying the setup
1. Make a test purchase with card `4242 4242 4242 4242` (any future expiry, any CVC).
   The order should appear and the success page should show its order number.
2. Use card `4000 0000 0000 0002` to check a declined payment creates no order.
3. In the webhooks menu, open the endpoint and check recent deliveries show `200`. You can resend an event from there to confirm that repeated delivery doesn't create a second order.

### Deploying to Heroku
The live version of this site is hosted using Heroku. To deploy your own version of the application, you need to use the following steps:

1. Set up a Heroku account and log in
2. Select 'New' in the top right and create new app
3. Name your app and choose the correct region before selecting create app
4. Edit the config vars section within the settings tab with your unique SECRET_KEY, DATABASE_KEY, STRIPE KEYS, AWS KEYS and any other unique variables you have included in your project
5. In the deploy tab, choose GitHub as your deployment method
6. Choose the correct repository and ensure the correct branch is selected (usually main)
7. Use the 'deploy branch' button in the manual deployments section and let this run. You can also set this to automatic deployment so anytime you push to main in your repository it automatically deploys the most recent commit
8. Use the open app button to launch the application

Please note, within your allowed hosts within settings.py of your application, you should have '.herokuapp.com' or else this will not deploy.

## Code from External Sources
The following packages used in this project can be found in [requirements.txt](./requirements.txt) and the following code snippets have been used:

1. I used the increase and decrease buttons on the product detail page of Bouqiue Ado as a starter and amended them to suit my styling and needs.
2. Toast html files were from Bootstrap with custom classes and text
3. Messaging levels were used from the boutique ado project

## Credits and Disclaimers
I have the following credits and disclaimers:

* Friends for being testers for the application
* All plant descriptions and details are AI generated to populate the site
