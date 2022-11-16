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
