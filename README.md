# Largesseance

- Andrew Collins
- James Hoffman
- Jonathan Roman
- Theresa Villa

Largesseance - "insert catch phrase here"

## Design
- [API design](docs/api-design.md)
- [Data model](docs/data-model.md)
- [Integrations](docs/integrations.md)

## Intended market

We are targeting consumers that need assistance with the process of gift-giving and tracking important events in their lives.

## Functionality

- Main page features a random gift generator based on Etsy's top selling products, as well as the ability to customize gift suggestions based on the occasion and the price limit. Visitors will be able to click on the product they are interested in purchasing and will be redirected to that product's listing in Etsy so they can purchase it.
- Logged in users will have the ability to:
  - Add a person on their account and provide the person's gender, age, interests, and their relationship with the user
  - Keep track of important events and link it to a person or multiple people
- On the dashboard, users are able to select a person they wish to view personalized gifts for
- The personalized gift suggestions are based on the demographics provided by the user and the closest occasion coming up.
- On the calendar, users are able to see the list of events they have created sorted according to date
- Uses are able to edit and delete persons and events previously created

## Project Initialization

To fully enjoy this application on your local machine, please make sure to follow these steps:

1. Clone the repository down to your local machine
2. CD into the new project directory
3. Run `docker volume create api-gft-data`
4. Run `docker compose build`
5. Run `docker compose up`
??? not sure how the user who clones this project would use the app without etsy api key
