#!/usr/bin/env python3

# python app
# espn api path to get current scores:  http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard
# to pass in EventId:
#    http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard/events?event=401267403

import requests
import constants
import threading
from pprint import pprint

totalProjectedScore = 0
def getEvents():
	threading.Timer(30.0, getEvents).start()
	request = 'http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard'
	dataRequest = requests.get(request).json()
	#	pprint(dataRequest)
	
	for x in dataRequest['events']:
		if x['status']['type']['name'] != constants.STATUS_SCHEDULED:
			calculateAndPrintData(x)
		else:
			print("{} - {}".format(x['name'], x['status']['type']['name']))
	print("\n")

def calculateAndPrintData(dataRequest):
	global totalProjectedScore
	
	period = dataRequest['competitions'][0]['status']['period']
	clock = dataRequest['competitions'][0]['status']['clock']
	
		# Get Home Team score + Away Team Score
	totalCurrentScore = 0
	for x in dataRequest['competitions'][0]['competitors']:
		totalCurrentScore = totalCurrentScore + int(x['score'])

	secondsPlayed = (period * constants.SECONDS_PER_PERIOD) - clock

		# PointsPerSecond * TotalSeconds
	totalProjectedScore = (totalCurrentScore / secondsPlayed) * (constants.NUMBER_OF_PERIODS * constants.SECONDS_PER_PERIOD)

	print("___________________________\n{}\n+/- {}\nQ{} - {}\n___________________________".format(dataRequest['name'], round(totalProjectedScore, 2), period, dataRequest['competitions'][0]['status']['displayClock']))

# --------------------------------------------------------------------------------------
# This program begins by getting all the NBA games that have are currently being played.

getEvents()
