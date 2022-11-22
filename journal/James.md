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

### 11/21/2022
We continued to finish up our endpoints. The rest of the team completed the endpoints for Gender, Relationships, Interests, and Occasions.

Theresa and I started working on the People endpoint and implemented the full CRUD functionally for that endpoint. Jonathan and Andrew started working the Events endpoint.

I also finished the work on the People endpoint to protect it, allowing only authenticated users the ability to access the endpoints. I also made it so that that endpoints only return data associated with that user. The users ability to update and delete is  also restricted to data linked specifically to them.


### 11/22/2022
I updated the people endpoint to include more details when the endpoints return data. It now shows the the values of the objects linked to them instead of just the associated id.
