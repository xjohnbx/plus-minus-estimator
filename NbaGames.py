# This is the file for the NBA game dataClass
# Enum TODO
# 	- competitor.homeAway
#   - statistic.name

class NbaGame:
	def _init_(day, events ):
		self.day = day # This is a Day data Type
		self.events = events # Collection of Events (Haven't yet seen a scenario with more than 1


class Day:
	def _init_(date):
		self.date = date # Date

class Event:
	def _init_(competitions):
		self.competitions = competitions # Collection of Competitions


class Competition:
	def _init_(attendance, broadcasts, competitors, conferenceCompetition, date, geoBroadcasts, id, neutralSite, notes, recent):
		self.attendance = attendance # Int
		self.broadcasts = broadcasts # Collection of Broadcasts
		self.competitors = competitors # Collection of Competitors
		self.conferenceCompetition = conferenceCompetition # Bool
		self.date = date = # Date of Event (e.g. '2021-01-24T18:00Z')
		self.geoBroadcasts = geoBroadcasts # Collection of GeoBroadcast
		self.id = id # String representing id (e.g. '401267409')
		self.neutralSite = neutralSite # Bool
		self.notes = notes # This is an empty array. I assume a Collection of strings, maybe a Note object
		self.recent = recent # Bool
# NEXT STEP will be the situation


class Broadcast:
	def _init_(market, names):
		self.market = market # String representing (National, Home, Away)
		self.names = names # Collection of strings representing channel (e.g. 'FS1', 'NBATV')

class Competitor:
	def _init_(homeAway, id, leaders, lineScores, order, records, score, statistics, team, type, uid):
		self.homeAway = homeAway # String that will be 'home' or 'away'
		self.id = id # String representing id as number
		self.leaders = leaders # Collection of Leader objects
		self.lineScores = lineScores # Collection of LineScores
		self.order = order # Int representing not sure (e.g. 0)
		self.records = records # Collection of Record
		self.score = score # String rep. number (e.g. '58')
		self.statistics = statistics # Collection of Statistics
		self.team = team # Team Object
		self.type = type # String (e.g. 'team')
		self.uid = uid # String for userId I assume ( e.g. 's:40~l:46~t:11')

class Leader:
	def _init_(abbreviation, displayName, statLeaders, name, shortDisplayName):
		self.abbreviation = abbreviation # String (e.g.  'Pts', 'Reb'))
		self.displayName = displayName # String giving display name of above (e.g. "Points", "Rebounds")
		self.statLeaders = statLeaders # This is competitors.leaders.leaders (This is a collection of each stat)
		self.name = name # This is the string for name (e.g. 'points')
		self.shortDisplayName = shortDisplayName # This is the short displayName (e.g. 'Pts')

class StatLeaders:
	def _init_(athlete, displayValue, team, value):
		self.athlete = athlete # Athlete
		self.displayValue = displayValue # String representing number (e.g. '13')
		self.team = team # Team Object
		self.value = value # Float value of stat (e.g. 13.0)

class Athlete:
	def _init_(active, displayName, fullName, headshot, id, jersey, links, position, shortName, team):
		self.active = active # Bool
		self.displayName = displayName # Two part String 'Justin ', 'Holiday'
		self.fullName = fullName # Two part String 'Justin ' 'Holiday'
		self.headshot = headshot # This is a link to the headshot of each player
		self.id = id # String (e.g. '2284101' - Should return Justin Holiday)
		self.jersey = jersey # String rep. of a number (e.g. '8')
		self.links = links # Collection of Links
		self.shortName = shortName # Two Part String - (e.g. 'J. ' 'Holiday')
		self.team = team # Team Object with Id only

class Link:
	# href, rel are used, rest are optional
	def _init_(href, isExternal, isPremium, rel, text):
		self.href = href # String address of espn home screen for player
		self.isExternal = isExternal # Bool
		self.isPremium = isPremium # Bool
		self.rel = rel # Collection of Strings
		self.text = text # String representing first rel it looks like (e.g. 'Clubhouse')

class Position:
	def _init_(abbreviation):
		self.abbreviation = abbreviation # String for position shortened (e.g. 'SG' - Starting Guard)

class Team:
	# Id is the only one that is used everywhere
	def _init_(abbreviation, alternateColor, color, displayName, id, isActive, links, location, logo, name, shortDisplayName, uid, venue):
		self.abbreviation = abbreviation # Abbreviation of team name (e.g. 'IND')
		self.alternateColor = alternateColor # String representing alternateColor: (e.g. '00275d')
		self.color = color # This is the color String (e.g. '061642')
		self.displayName = displayName # This is the display name of the team (e.g. 'Indiana ' 'Pacers')
		self.id = id # String representing number as id (e.g. '11')
		self.isActive = isActive # Bool
		self.links = links # Collection of Link
		self.location = location # String of location (e.g. 'Indiana')
		self.logo = logo # Link to the logo of the team as a String
		self.name = name # String of Name (e.g. 'Pacers')
		self.shortDisplayName = shortDisplayName # String of shortName (e.g. 'Pacers')
		self.uid = uid # String of UID, might be userID (e.g. 's:40~l:46~t:11')
		self.venue = venue # Venue object

class LineScore:
	def _init_(value):
		self.value = value # Float representing lineScore (e.g. 24.0)

class Record:
	def _init_(abbreviation, name, summary, type):
		self.abbreviation = abbreviation # This seems optional as not all have it, String
		self.name = name # String maybe 2 parts (e.g. 'All ' 'Splits', or 'Home')
		self.summary = summary # Summary of record as string (e.g. '9-6')
		self.type = type # Possibly Enum (e.g. 'road', 'home', 'total'

class Statistic:
	def _init_(abbreviation, displayValue, name):
		self.abbreviation = abbreviation # Abbreviation of name: (e.g. '3P%')
		self.displayValue = displayValue # Display value of Number: '31.8'
		self.name = name # This is probably enum (e.g. 'threePointFieldGoalPct')

class Venue:
	def _init_(id):
		self.id = id # String of id (e.g. 2183)

class GeoBroadcast:
	def _init_(lang, market, media, region, type):
		self.lang = lang # string for what language (e.g. 'en')
		self.market = market # Market Object
		self.media = media # Media Object
		self.region = region # String for region (e.g. 'us')
		self.type = type # Type Object

class Market:
	def _init_(id, type):
		self.id = id # String representing id
		self.type = type # String (e.g. 'National')

class Media:
	def _init_(shortName):
		self.shortName = shortName # ShortName of Media (e.g. 'NBATV')

class Type:
	def _init_(id, shortName):
		self.id = id # String for Id
		self.shortName = shortName # String for shortName (e.g. 'TV')













































