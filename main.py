import requests
import asyncio
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = "api key here"

last_staff_total = 0
last_watchdog_total = 0

async def check_punishment_stats():
    global last_staff_total, last_watchdog_total

    while True:
        try:
            response = requests.get('https://api.hypixel.net/punishmentstats', params={'key': API_KEY})
            data = response.json()

            if data['success']:
                staff_total = data['staff_total']
                watchdog_total = data['watchdog_total']

                current_time = datetime.now().strftime('%H:%M:%S')

                if last_staff_total != 0 and staff_total > last_staff_total:
                    print(f"Staff ban #{staff_total} ({current_time}).")

                if last_watchdog_total != 0 and watchdog_total > last_watchdog_total:
                    print(f"Watchdog ban #{watchdog_total} ({current_time}).")

                last_staff_total = staff_total
                last_watchdog_total = watchdog_total

            await asyncio.sleep(1)

        except Exception as e:
            print(f'Error occurred while checking punishment stats: {e}')

asyncio.run(check_punishment_stats())
