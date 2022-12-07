## Week 1
### 11/14/2022
Last week was spend working as team to define the wire frame of our application. The general functionally and stretch goals were defined.

Current stretch goals are:
* Saving Gifts as favorites for later
* Email Notifications on upcoming events
* Calendar view included with list of events

Link to our current working excalidraw:
[Largesseance](https://excalidraw.com/#room=7e097e63c1fb339686de,p3bUaSu65jLaPaDdIrvEag)

I spent some time translating our API endpoints from the excalidraw into the markdown file located at `\docs\api-design.md`

I also spent time trying to configure and deploy the project to meet the deliverables listed in the README. After some troubleshooting, I was able to get the deployment to work. I was running into pipeline failed error when attempting to deploy via GitLab. The fixed was to validate my account on Gitlab so that I was able to use their free runners.

### 11/15/2022
Today was spent on updating the docker compose yaml file to include the postgres database. `.env` file was also setup for environment variables to be used for passwords and API keys.

### 11/16/2022
We settled on a database choice, that being PostgreSQL. We defined the schema for our tables. Theresa wrote the SQL statements for the migrations. I setup the docker compose yaml for pgAdmin service. We confirmed that all the docker containers are able to run and confirmed the ability to view the database from within pgAdmin.

### 11/17/2022
Last evening I was able to figured out how to implement the user authentication using a demo project. That code assisted Theresa with adding that functionally to main gamma project today.

Once we had our developer branch in a working state we merged the changes into the main branch. Our next steps in our developer branch is start working on our API endpoint by establishing the queries and routers.

We all picked specific endpoint to work on and started to write code for each. I will be creating the endpoint for table "age_range"

### 11/18/2022
I completed full CRUD functionally for the age range endpoint.

---

## Week 2
### 11/21/2022
We continued to finish up our endpoints. The rest of the team completed the endpoints for Gender, Relationships, Interests, and Occasions.

Theresa and I started working on the People endpoint and implemented the full CRUD functionally for that endpoint. Jonathan and Andrew started working the Events endpoint.

I also finished the work on the People endpoint to protect it, allowing only authenticated users the ability to access the endpoints. I also made it so that that endpoints only return data associated with that user. The users ability to update and delete is  also restricted to data linked specifically to them.

### 11/22/2022
I updated the people endpoint to include more details when the endpoints return data. It now shows the the values of the objects linked to them instead of just the associated id.

### 11/23/2022
We started to work on our front end components. I was able to get the nav bar in good spot. I still need to filter certain items base on if the user is logged in or not. We are going to use redux to keep track of the user's auth token. That will likely be the next step. After that, I will start work on the main dashboard component.

---

## Week 3
### 11/28/2022
Before moving onto the main dashboard component, I started working on the login/logout functionally. I was able to get the working but did end up running into several hurdles in getting it working.

In order for the get token api call to return what I needed, I had to include `credentials: 'include'` inside my RTK query. This was mentioned in the documentation for [JWTdown for FastAPI](https://jwtdown-fastapi.readthedocs.io/en/latest/intro.html#getting-tokens-from-http-only-cookies)

Once I was able to get the token, I needed to be able to actually log in the user. This proved to be difficult. I had to change the content-type from `application/json` to `application/x-www-form-urlencoded`.  I was able to figure how to do that after combing through the [RTK documentation](https://redux-toolkit.js.org/rtk-query/api/fetchBaseQuery#setting-the-body)

I still needed to format the data as FormData instead of normal json in order for the request to be processed correctly now that is is using a different content header. I had to reference [StackOverflow](https://stackoverflow.com/questions/35325370/how-do-i-post-a-x-www-form-urlencoded-request-using-fetch#comment71216981_37562814) to figure out to package the data correctly.

Now that the login feature is complete, I will begin working on the dashboard component proper starting tomorrow.

### 11/29/2022
Worked on the dashboard today. I was able to get a fair amount of it built. It still needs edit/delete functionally and products cards added to page, but it coming together.

Candice entered our breakout room today to discuss our database design. She suggested that out foreign key tables connecting to the persons tables could have been setup using enum data type. This would make the overall structure of our database simpler. However, after some deliberation, we decided to continue with our current database structure.

While some of the smaller attributes such as gender and age range would probably benefit from being an enum field, we decided to keep the foreign key tables as it is easier to make changes going forward if needed.

Some reading that was used to help guide our decision to keep the FK tables:
* [Stack Overflow - MySQL ENUM type vs join tables](https://stackoverflow.com/questions/362044/mysql-enum-type-vs-join-tables)
* [Stack Overflow - SQL: Advantages of an ENUM vs. a one-to-many relationship?](https://stackoverflow.com/questions/4293476/sql-advantages-of-an-enum-vs-a-one-to-many-relationship)
* [Medium - PostgreSQL: ENUM is no Silver Bullet](https://medium.com/swlh/postgresql-3-ways-to-replace-enum-305861e089bc)

### 11/30/2022
Today I worked on completing more features for the dashboard. I added some placeholder cards for products and a table that includes the three most recent upcoming events for a specific person. I also started and completed an edit person form. I did run into a significant blocker regarding the form

I had everything working on the edit form except for the PUT request to update the record in the database through the API. I kept getting a `422 Unprocessable Entity` error when trying to complete the request. I tried several things to no avail. I did however figure out what it was in the end.

I wrongly assumed that the `content-type` header was already set to `application/json`. I needed to manually set that header in my fetch before the request would work correctly. It took awhile to figure this out since even when the header was excluded, the dev tools in Chrome still showed the request as having a `content-type` set to `application/json`

### 12/1/2022
Today, I continued to work on the dashboard. I completed the functionally to delete a user and other minor things across the repo.

### 12/2/2022
Spent more time today working on the dashboard. I am now getting specialized results back from Etsy that are more unique to the person. I have the cards formatted in a way that I am happy with. I still need to work on a few more features for the dashboard:
* Showing person details
* Adding dropdown to filter by price
* Allowing the user the highlight an event to show gifts based of that event

---

## Weekend Bonus
### 12/3/2022
I spent some time on Saturday taking care of some small housekeeping items. I made some small adjustments to elements using bootstrap classes to make the look of the site more consistent across the board.

### 12/4/2022
The site was in a good spot and so I merged our development branch into the main branch. I wanted to test out the pipeline and see if I could get the site live on render and gitlab pages. I cleaned up every use of localhost in fetches to use an environment variable instead.

I updated any code that was causing the lint test to fail. The unit tests still have not been completed yet by the entire team, so that aspect is still commented out on the gitlab yml file for now.

Speaking of the unit tests, I did complete a test that checks all the endpoints for the age range, which was the endpoint that I solo wrote from earlier.

After all that, I attempted to get the deployment working. The gitlab page was building and deploying correctly, which was good. However the render side was failing to build and deploy.

Here is a list of issues that I came across before I got the deployment to render fully working:

* ISSUE: ModuleNotFoundError: No module named 'authenticator'
* FIX: I needed to update the production Dockerfile to copy all the needed contents inside the 'sample_service' folder, this included authenticator.py
<br><br>
* ISSUE: KeyError: 'DATABASE_URL'
* FIX: The environment variable for the database was not configured. For our development environment, this was setup via the yml file and thus did not exist when render was using the production Dockerfile to build. To get this working, the fastapi that is hosted on render needed a way to connect to a database. Render also offers [databases to setup and use](https://render.com/docs/databases). I setup a postgreSQL database through render and added a DATABASE_URL environment variable on Render's dashboard for our fastapi service using the internal database url provided by render.
<br><br>
* ISSUE: KeyError: 'SIGNING_KEY'
* FIX: This was another environment variable that needed set in the render dashboard for the authenticator to work. I also made sure to include any 3rd party keys at this stage as well.
<br><br>
* ISSUE: Render was deploying, but when using the site, I was running into CORS errors.
* FIX: I needed to set the CORS_HOST environment variable to the hostname of our ghi gitlab page.

---

## Week 4
### 12/5/2022
I worked on adding validation to all of our forms in the app. I was able to add a few alert messages to certain forms and also made it so that the submit button for forms are disabled until the form is valid. We identified another stretch goal, and that would be implement [bootstrap's method of validation](https://getbootstrap.com/docs/5.2/forms/validation/).

### 12/6/2022
Today, I spent some time on styling the site a little more CSS, asking for input from the rest of the team along the way. Right now, the site is looking better than it was before.

### 12/7/2022
