### December 06, 2022 (12/06/2022):
Today, I added some edits to the mainpage style before deploying the application. I am excited to begin researching how to implement new stretch goals for our application.

### December 05, 2022 (12/05/2022):
Today, I noticed an error with the unit test for interests. I looked at the CLI from Docker to identify where the issue was. Then, I edited the code at the location of the error and was able to resolve it. Now the unit tests I wrote all work. I also made some edits to the format of the application in order to help with consistency. I also added descriptions to the pages to assist users in understanding what needs to be done. I also added alt texts to the images on the main page. I learned that alt text is important for ensuring accessibility in the images.

### December 02, 2022 (12/02/2022):
Today, I completed  the New Event form to handle situations when a user attempts to create an event without first adding a person. A person needs to be added so that the user can choose who is associated with the event. I learned about to use the if/else for the return statements so that if there are no people added, then it will display a message stating that the user needs to add a person first. Then, I added a button to link to the add person form. For next week, I plan on editing the readme, making sure the front end looks cohesive, then looking at the stretch goals.

### December 01, 2022 (12/01/2022):
Today, I completed adding the edit button to the calendar page. I created an EditEvent form with PUT method so that the button leads to this. I also added the create event button to the calendar page to link the create event form. Furthermore, I added redirects to the create event and edit event forms so that the user will be redirected to the calendar view to see the events. I plan to add error handling if a user attempts to create an event without already having a person added. I also plan on looking into more front-end design concepts to make each of our group's pages more cohesive.

### November 30, 2022 (11/30/2022):
I am working on the edit button for the calendar page to allow a logged-in user to edit the event that was created. I also plan to look into more front-end design ideas to improve the calendar and events form page.

### November 29, 2022 (11/29/2022):
Morning: Yesterday, I worked on the EventForm. I used React hooks for this. Today, I will continue to edit the eventform and also create a unit test. Today, we learned about unit tests and how to write our own. I will write a unit test for one of the endpoints I created.
Evening: I finished creating the EventForm, I utilized react hooks and learned how to use authorization to ensure the logged-in users can only see the people they added. I also assisted in editing the events queries to incorporate Person name/id and Occasion name/id. This involved editing the SQL tables and functions. I also completed the Calendar list, which will show the upcoming events for the logged-in users. This also included working with authorization to make sure the logged-in users only see the events they created. I also finished creating the unit tests for the interests endpoints.

### November 23, 2022 (11/23/2022):
Today, I learned about websockets. I will be working on the event form and event list react front-ends. I will be incorporating React hooks for these.

### November 22, 2022 (11/22/2022):
Today, I learned more about redux. I began the set up for redux in our project and commited those changes. I plan to begin front-end portions tomorrow with React.

### November 21, 2022 (11/21/2022):
During the weekend, I completed the Get All API Endpoint for Interests. Today, I worked on the Create Events API Endpoint, and the Update Events API endpoint. I also assisted teammates in any technical issues they faced. Our plan tomorrow is to incorporate redux into the project.

### November 18, 2022 (11/18/2022):
I learned how to create API endpoints for create and get interests. I created my create interests API endpoint and tested that it works correctly on the localhost. My plan is to continue API endpoints for interests, events, and people. Then we can create the front-end React components.

### November 17, 2022 (11/17/2022):
Yesterday, we troubleshot problems related to creating our login/logout authenticators. Today, I created the Create Event API endpoint in Queries, Routers, and Main. I learned how to create API endpoints using FastAPI. My plan is to work on Interests API endpoint and assist teammates if any technical issues arise.

### November 16, 2022 (11/16/2022):
Yesterday, we learned more SQL fundamentals. We also created our database and are currently planning on using PostgreSQL. I also fixed my docker issues from Windows.

### November 14, 2022 (11/14/2022):
Last week, we worked collaboratively to create a wireframe design for our project. We each brought unique perspectives and ideas to fulfill our vision for this application. We also began creating API endpoints and incorporating them with our specific project. I wrote API endpoints for getting an event, updating an event, and deleting an event. We also incorporated authorization tokens into our endpoints.
