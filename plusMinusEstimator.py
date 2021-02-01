#!/usr/bin/env python3

#	python app
#	espn api path to get current scores:		http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard
#	To pass in EventId:
#	http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard/events?event=401267403

import requests
import constants
import threading
import json
from NbaGames import NbaGames
from pprint import pprint

def getEvents():
	threading.Timer(30.0, getEvents).start()
	request = 'http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard'
	dataRequest = requests.get(request).json()
	pprint(dataRequest)

	nbaGames = NbaGames(**dataRequest)

	for event in nbaGames.events:
		if event.status.type.name != constants.STATUS_SCHEDULED and event.status.type.name != constants.STATUS_POSTPONED:
			calculateAndPrintData(event)
		else:
			print("{} - {}\n".format(event.name, event.status.type.name))
	print("\n")

def calculateAndPrintData(event):
	totalProjectedScore = 0
	competition = event.competitions[0]

	period = competition.status.period
	clock = competition.status.clock
	awayTeam = ''
	homeTeam = ''
		# Get Home Team score + Away Team Score
	totalCurrentScore = 0
	for competitor in competition.competitors:
		if competitor.homeAway == constants.AWAY_TEAM:
			awayTeam = '{} - {}'.format(competitor.team.abbreviation, competitor.score)
		else:
			homeTeam = '{} - {}'.format(competitor.team.abbreviation, competitor.score)
			
		totalCurrentScore = totalCurrentScore + int(competitor.score)

	secondsPlayed = (period * constants.SECONDS_PER_PERIOD) - clock

		# PointsPerSecond * TotalSeconds
	if secondsPlayed > 0:
		totalProjectedScore = (totalCurrentScore / secondsPlayed) * (constants.NUMBER_OF_PERIODS * constants.SECONDS_PER_PERIOD)

	print("___________________________\n{}\n{}	{}\n+/- {}\nQ{} - {}\n___________________________".format(event.name, awayTeam, homeTeam, round(totalProjectedScore, 2), period, competition.status.displayClock))

# --------------------------------------------------------------------------------------
# This program begins by getting all the NBA games that have are currently being played.

getEvents()
