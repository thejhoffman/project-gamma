# Largesseance
![Largesseance](/uploads/74c123505b864bd0aeeed79a0687b211/ezgif.com-gif-maker__3_.mp4)

- Andrew Collins
- James Hoffman
- Jonathan Roman
- Theresa Villa

Largesseance - "Personalized gifts for special occasions"
https://largesseance.gitlab.io/project-gamma/

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
3. Run `docker volume create api-gft-data` for database volume
4. Run `docker volume create pg-admin` for pg admin volume needed for database testing
5. Run `docker compose build` or for M1 `DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose build`
6. Run `docker compose up`
7. Sign up for your own Etsy API key at `https://www.etsy.com/developers/register`
8. Once approved, insert the key in a .env file with the variable name "ETSY_API_KEY" to enjoy the functionality of our app!

## Unit Tests

- Andrew Collins - Gender
- James Hoffman - Age_range
- Jonathan Roman - Interests
- Theresa Villa - Occasions & Relationships

## Wire Frame

- Here is our wire frame we had designed using Excalidraw to get a layout of the app.

![Screenshot_2022-12-09_at_9.31.42_AM](/uploads/55ea06d44aea3175f7ebc6f8e47b1699/Screenshot_2022-12-09_at_9.31.42_AM.png)![Screenshot_2022-12-09_at_9.26.48_AM](/uploads/07fba0f680aba7f4ffdf30825681f193/Screenshot_2022-12-09_at_9.26.48_AM.png)![Screenshot_2022-12-09_at_9.27.03_AM](/uploads/398269537a995334f055d287d8569d7f/Screenshot_2022-12-09_at_9.27.03_AM.png)![Screenshot_2022-12-09_at_9.27.35_AM](/uploads/4498b8e23a39601ebbd1e9a389c6c67c/Screenshot_2022-12-09_at_9.27.35_AM.png)![Screenshot_2022-12-09_at_9.27.47_AM](/uploads/7e7b805ee06462b9208ca730f23d5881/Screenshot_2022-12-09_at_9.27.47_AM.png)![Screenshot_2022-12-09_at_9.28.04_AM](/uploads/7c6fdd29ac556e059a812c2808215c2c/Screenshot_2022-12-09_at_9.28.04_AM.png)![Screenshot_2022-12-09_at_9.28.21_AM](/uploads/4a0e27d12aa7778b0d97f5b9eea6a245/Screenshot_2022-12-09_at_9.28.21_AM.png)![Screenshot_2022-12-09_at_9.28.32_AM](/uploads/c26192391f1ecdc89cd142c0fe7fa475/Screenshot_2022-12-09_at_9.28.32_AM.png)![Screenshot_2022-12-09_at_9.28.48_AM](/uploads/87ca74237a204dc77fb9c968db815d0e/Screenshot_2022-12-09_at_9.28.48_AM.png)
