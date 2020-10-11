#!/usr/bin/python3

# All the imports required by the script
import subprocess
import requests
import json


# This will set time, note that running this program requires root privilidges
def set_time(date, time):
	subprocess.run(['sudo', 'date', '-s', f'{date} {time}'])


# This script uses worldtimeapi to get time/date by IP address
def get_time():
	time_t = requests.get("http://worldtimeapi.org/api/ip")
	time = json.loads(time_t.text)
	time = time['datetime'].split('T')
	date = time[0]
	time = time[1][:8]
	return date, time


# Main Function
if __name__ == '__main__':
	date, time = get_time()
	set_time(date, time)
