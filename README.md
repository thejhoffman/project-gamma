# Largesseance

- Andrew Collins
- James Hoffman
- Jonathan Roman
- Theresa Villa

Largesseance - "insert catch phrase here"
"INSERT LINK TO DEPLOYED APP HERE"

## Design
- [API design](docs/api-design.md)
- [Data model](docs/data-model.md)
- [Integrations](docs/integrations.md)

## Intended market

We are targeting consumers that need assistance with the process of gift-giving and tracking important events in their lives.

## Functionality

- This application relies on the Etsy API
- Main page features a random gift generator based on Etsy's top selling products, as well as the ability to customize gift suggestions based on the occasion and the price limit. Visitors will be able to click on the product they are interested in purchasing and will be redirected to that product's listing in Etsy so they can purchase it.
- Logged in users will have the ability to:
  - Add a person on their account and provide the person's gender, age, interests, and their relationship with the user
  - Keep track of important events and link it to a person or multiple people
- On the dashboard, users are able to select a person they wish to view personalized gifts for
- The personalized gift suggestions are based on the demographics provided by the user and the closest occasion coming up.
- On the calendar, users are able to see the list of events they have created sorted according to date
- Uses are able to edit and delete persons and events previously created

## Future functionality

- Send out email reminders to users when an event is coming up in a week and 2 weeks, along with suggested gift ideas
- Replace event list view with a calendar view
- Saved gifts functionality: enable users to "favorite" a gift they'd like to purchase in the future
- Query other shop APIs for products in addition to Etsy for more options

## Project Initialization

To fully enjoy this application on your local machine, please make sure to follow these steps:

1. Clone the repository down to your local machine
2. CD into the new project directory
3. Run `docker volume create api-gft-data`
4. Run `docker compose build`
5. Run `docker compose up`
6. Sign up for your own Etsy API key at `https://www.etsy.com/developers/register`
7. Once approved, insert the key in a .env file with the variable name "ETSY_API_KEY" to enjoy the functionality of our app!

## Unit Tests

- Andrew Collins - Gender
- James Hoffman - Age_range
- Jonathan Roman - Interests
- Theresa Villa - Occasions & Relationships
