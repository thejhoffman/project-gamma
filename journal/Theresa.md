## November 8, 2022

Designed wireframes in Excalidraw, specified MVP goals and strech goals along the way. Main goals are to have a random gift generator on the main page, a personalized gift generator for a logged in user, and date tracker. Strech goals include a calendar view of the events, email reminders sent out to app users when a date is nearing, and possibly an account to a social media and have everyone's birthdays on your calendar

## November 10, 2022

Designed API endpoints in Excalidraw as we didn't have a repo yet
I wrote the following endpoints: list of people, person detail, adding a person, list of occasions, deleting a person

## November 14, 2022

Today, I created 3 issues in Gitlab: generating a random gift suggestion in the home page, signing up for a user account, and viewing a personalized gift suggestion based on a person's interest after a user is logged in

More than likely, the team will be adding more issues as we work on the project

## November 15, 2022

Today, I suggested working on a different branch other than main to make sure that we always have a copy of a working code.

The team began discussing using MongoDB vs PostgreSQL, and we'll likely make a decision after the MongoDB lecture coming up. I found a database design tool called Luna Modeler that could potentially help if we decide to use PostgreSQL, as we were worried about the learning curve of learning SQL. It also helps create diagrams which can show a clear picture of the data structure and can help us spot errors, especially with normalization of tables.

## November 17, 2022

Yesterday I had difficulty with creating a user, but fortunately figured it out today with the help of James. I was able to create a user and save it on the database but I kept getting an error saying dict () had an invalid key and the password being saved was not the hashed_password. It turns out I was doing my queries incorrectly. After getting that fixed, the authentication, login, logout, and getting a token went easy. I shared my code to the team, had them test out everything on their ends to make sure everything is working and to discuss any changes that the code needs. We are having difficulties with email validation, and in the near future we'd like to have that working.

## November 21, 2022

Last Friday I created the API endpoints for occasions and relationships. Today I worked on the CRUD functionality for the Person model, alongside James. I also assisted in getting the Event model CRUD functionality working after Andrew and Jonathan had written out the queries and routers needed. There were just small details missing that made the functionality fail, but after that was taken care of all of our endpoints are now built. James took care of the authentication and login today, making sure all users are logged in before being able to access features that require a user account.

For remainder of the week, we need to figure out how to fetch data from the Etsy API. I also started looking into how the relationships of our data need to be structured - basically reviewing what needs to happen if we have a one-to-many relationship or many-to-many relationship. This seemed a lot easier in Django, but I'm not sure how to implement it in Postgres.
