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

## November 23, 2022

Today, the team and I started looking on how to obtain an Etsy API key. It turns out, we should've done it earlier, probably as soon as we determined that we wanted to work with the Etsy API. It's not as easy getting their API key (or Walmart, or Target, or any major shopping brands I looked at) as compared to Pexels. Requesting the key required filling out a form and providing more information (such as the callback URL) than I had anticipated.

Today I also began working on the front-end - more specifically the main page and the person form page. Getting started and creating the structure of the components were easy, but I still find it challenging to figure out which HTML id or class to tweak when I need something formatted a certain way. As always, google to the rescue with Bootstrap and CSS questions. I would really like to try tailwind but that might be more of a stretch goal at this point. I also began working with Hooks for the first time.

## November 28, 2022

Received the Etsy API key approval today, and so I began working on trying to understand how to query the Etsy API. The request relies on the api key being a part of your query, and the other query parameters are mostly optional. I had to figure out how to get the details and images of a product in one query, because as it turns out doing a get all listings query does not provide the image detail and we need that feature implemented for our site. After much research, I learned that I would need to add the "includes=MainImage" in the query as well if I want the image associated with the product. I successfully finished creating the etsy api query endpoint, as well as added it to the get one person instance and get all people instance.

## November 30, 2022

Yesterday I successfully finished working on having the main page generate random products from the Etsy API endpoint when it loads. Because the way our main page is structured, I also had to create nested columns - a first for me. Working more and more on the front-end helps me get more familiar with CSS, something I was very unfamiliar with in the beginning of this program. I also contributed on getting the sign up form to work, created the submit functionality and ensured that accounts being created are saved to the database.

Upon working on adding customizable query parameters for the main page functionality today, I realized that Etsy does not have a mature content filter. I tried to search through the docs but to no avail. Upon doing a google search, it turns out that even Etsy customers who use their site have problems with this as well. I suspect a filter may not be possible at this point. Also, their max_price filter is not working well. Setting it on values that don't end in 0 unfortunately breaks the filter. To fix it, I have to make sure the available price range options for users to choose are round numbers. Nonetheless, the functionalities of the main page are now almost done. Users should now able to successfully choose an occasion and/or price limit that will suit their needs. If they do choose to purchase the product, they are able to click on the card and a new window will open to that specific Etsy listing.
