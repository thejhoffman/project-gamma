from datetime import date
from rocketry.conds import cron
from rocketry import Rocketry

app = Rocketry(execution="async")
import asyncio

HOLIDAYS = [
    date(2022, 12, 8), #Birthday
]

# @app.task(cron("2 * * * *"))
# async def send_email():
#     print("welcome")
#     print("HERE I AM")

@app.task('every 10 seconds')
def send_email():
    print("welcome")
    print("HERE I AM")


async def main():
    "Launch Rocketry app (and possibly something else)"
    rocketry_task = asyncio.create_task(app.serve())
    # Start possibly other async apps
    await rocketry_task

if __name__ == "__main__":
    app.run()
