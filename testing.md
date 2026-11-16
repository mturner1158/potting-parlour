# Potting Parlour Test File
This section covers testing completed in relation to this project.

## Table of Contents
Please use the links below to navigate to a specific section:

* [User Story Testing](#user-story-testing)
* [Responsiveness Testing](#responsiveness-testing)
* [Lighthouse Testing](#lighthouse-testing)
* [HTML Testing](#html-testing)
* [CSS Testing](#css-testing)
* [JavaScript Testing](#javascript-tetsting)
* [Python Testing](#python-testing)
* [Django Testing](#django-testcase)

## User Story Testing
Testing was carried out against the deployed Heroku site to confirm the deployed version matches the tested development version. Each user story from the User Experience section is tested individually below.

### User 1: Visitor
A visitor is someone who is browsing the store but is not logged into an account.

|#|Story|Test Steps|Expected Results|Status|
|-|-----|----------|----------------|------|
|1.1|As a visitor, I want to see a list of all plants available for sale so that I can purchase plants.|Visit the plants page and view a list of all plants for sale|Plant page loads showing all plants where is_active=True|Pass|
|1.2|As a visitor, I want to see details of the plants for sale, such as image, price, description, watering frequency, light, humidity and pet safety, so that I can make an informed decision on the plants I would like to purchase.|Select a plant and see the details|Selecting a plant displays all details|Pass|
|1.3|As a visitor, I want to be able to search for products by name so that I can find a specific plant.|Use the search bar on the plants page to find a plant by name|Searching a plant by name will return that plant|Pass|
|1.4|As a visitor, I want to be able to filter by price, watering frequency, light, humidity and pet safety, and sort the results, so that I can find specific plants.|Uses the drop downs and tick boxes to filter the page and select apply filter|Selecting filters and selecting apply shows the appropriate plants|Pass|
|1.5|As a visitor, I want to be able to add products to a basket so that I can buy them.|Selecting a product and selecting add to basket|When selecting add to basket, the total goes up in the top right|Pass|
|1.6|As a visitor, I want to change the quantity of items in my basket so that I can order multiple plants.|Select basket in the top right and change the quantity input then click update|Changing the quantity and selecting update will update the sub total and grand total|Pass|
|1.7|As a visitor, I want to see a running total of my basket so that I can track my current spend.|Add plants to basket and see the total increase in the top left|Total in top left increases everytime the user adds something to basket|Pass|
|1.8|As a visitor, I want to sign up for an account so that I can have access to more features.|Selecting the login button will allow me to choose signup and make an account|Selecting log in details, navigating to sign up, entering details and verifying email creates an account|Pass|
|1.9|As a visitor, I want to be redirected sensibly if I try to access a protected page so that I understand what further authentication is needed.|Input a URL that requires a login|Redirected to the login page when an unathenticated user tries to access certain areas|Pass|
|1.10|As a visitor, I want to buy plants securely so that I know my payment is secure.||||
|1.11|As a visitor, I want notifications for any actions I take so that I am aware of my actions on the site.||||
|1.12|As a visitor, I want a clear success page after purchase so that I know my order went through.||||
|1.13|As a visitor, I want a clear message if my payment has failed so that I know what to do next.||||
|1.14|As a shopper, I want a loading screen during checkout so that I know something is happening.||||

### User 2: Shopper
A shopper is someone who is logged into the store and looking to buy a plant.

|#|Story|Test Steps|Expected Results|Status|
|-|-----|----------|----------------|------|

### User 3: Plant Owner
A plant owner is someone who has purchased a plant from the store through a logged-in account.

|#|Story|Test Steps|Expected Results|Status|
|-|-----|----------|----------------|------|

### User 4: Shop Owner
A shop owner is someone who manages the stock available in the store.

|#|Story|Test Steps|Expected Results|Status|
|-|-----|----------|----------------|------|

## Responsiveness Testing


## Lighthouse Testing


## HTML Testing


## CSS Testing


## JavaScript Tetsting


## Python Testing


## Django Testing
