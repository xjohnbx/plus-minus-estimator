# This is a file with classes that conform to the json returned from this endpoint: http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard

class NbaGames():
	def __init__(self, day, events, leagues, season):
		self.day = Day(**day) # This is a Day data Type

		eventCollection = []
		for event in events:
			eventCollection.append(Event(**event))
		self.events = eventCollection # Collection of Events (Haven't yet seen a scenario with more than 1

		leagueCollection = []
		for league in leagues:
			leagueCollection.append(League(**league))
		self.leagues = leagueCollection  # Collection of League

		self.season = Season(**season) # Season Object with type and year only

class Address():
	def __init__(self, city, state):
		self.city = city # String 'Portland'
		self.state = state # String e.g. 'OR'

class Athlete():
	def __init__(self, displayName, fullName, headshot, id, jersey, links, position, shortName, team, active=None):
		self.active = active # Bool
		self.displayName = displayName # Two part String 'Justin ', 'Holiday'
		self.fullName = fullName # Two part String 'Justin ' 'Holiday'
		self.headshot = headshot # This is a link to the headshot of each player
		self.id = id # String (e.g. '2284101' - Should return Justin Holiday)
		self.jersey = jersey # String rep. of a number (e.g. '8')

		linkCollection = []
		for link in links:
			linkCollection.append(Link(**link))
		self.links = linkCollection # Collection of Links (href and rel only)

		self.position = Position(**position) # Position Object
		self.shortName = shortName # Two Part String - (e.g. 'J. ' 'Holiday')
		self.team = Team(**team) # Team Object with Id only

class Broadcast():
	def __init__(self, market, names):
		self.market = market # String representing (National, Home, Away)
		self.names = names # Collection of strings representing channel (e.g. 'FS1', 'NBATV')

class Competition():
	def __init__(self, attendance, broadcasts, competitors, conferenceCompetition, date, geoBroadcasts, id, neutralSite, notes, recent, series, startDate, status, timeValid, type, uid, venue, headlines=None, odds=None, situation=None, tickets=None):
		self.attendance = attendance # Int

		broadcastCollection = []
		for broadcast in broadcasts:
			broadcastCollection.append(Broadcast(**broadcast))
		self.broadcasts = broadcastCollection # Collection of Broadcasts

		competitorCollection = []
		for competitor in competitors:
			competitorCollection.append(Competitor(**competitor))
		self.competitors = competitorCollection # Collection of Competitors

		self.conferenceCompetition = conferenceCompetition # Bool
		self.date = date # String of Date of Event (e.g. '2021-01-24T18:00Z')

		geoBroadcastCollection = []
		for geoBroadcast in geoBroadcasts:
			geoBroadcastCollection.append(GeoBroadcast(**geoBroadcast))
		self.geoBroadcasts = geoBroadcastCollection # Collection of GeoBroadcast

		if headlines is not None:
			headlineCollection = []
			for headline in headlineCollection:
				headlineCollection.append(Headline(**headline))
			self.headlines = headlineCollection # Collection of headline objects
			
		self.id = id # String representing id (e.g. '401267409')
		self.neutralSite = neutralSite # Bool
		self.notes = notes # This is an empty array. I assume a Collection of strings, maybe a Note object
		
		if odds is not None:
			oddsCollection = []
			for odd in odds:
				oddsCollection.append(Odd(**odd))
			self.odds = odds # This is a optional Variable - Collection of Odds Type
			
		self.recent = recent # Bool
		
		self.series = series
		if situation is not None:
			self.situation = Situation(**situation) # Situation Object
			
		self.startDate = startDate # String of Date e.g. '2021-01-26T03:00Z'
		self.status = Status(**status) # Status Object'
		
		if tickets is not None:
			ticketsCollection = []
			for ticket in tickets:
				ticketsCollection.append(Ticket(**ticket))
		self.timeValid = timeValid # Bool
		self.type = Competition_Type(**type) # CompetitionType object
		self.uid = uid # String of userId 's:40~l:46~e:401267427~c:401267427'
		self.venue = Venue(**venue) # Venue Object

class Competition_Type():
	def __init__(self, abbreviation, id):
		self.abbreviation = abbreviation # String e.g. 'STD' - I assume this means non-playoff
		self.id = id # String of Int e.g. '1'

class Competitor():
	def __init__(self, homeAway, id, order, records, score, statistics, team, type, uid, leaders=None, linescores=None, winner=None):
		self.homeAway = homeAway # String that will be 'home' or 'away'
		self.id = id # String representing id as number

		if leaders is not None:
			leaderCollection = []
			for leader in leaders:
				leaderCollection.append(Leader(**leader))
			self.leaders = leaderCollection # Collection of Leader objects

		if linescores is not None:
			linescoreCollection = []
			for linescore in linescores:
				linescoreCollection.append(Linescore(**linescore))
			self.lineScores = linescoreCollection # Collection of LineScores - This is optional

		self.order = order # Int representing not sure (e.g. 0)

		recordCollection = []
		for record in recordCollection:
			recordCollection.append(Record(**record))
		self.records = recordCollection # Collection of Record

		self.score = score # String rep. number (e.g. '58')

		statisticCollection = []
		for statistic in statistics:
			statisticCollection.append(Statistic(**statistic))
		self.statistics = statisticCollection # Collection of Statistics

		self.team = Team(**team) # Team Object
		self.type = type # String (e.g. 'team')
		self.uid = uid # String for userId I assume ( e.g. 's:40~l:46~t:11')
		self.winner = winner # Bool

class Day():
	def __init__(self, date):
		self.date = date # Date

class DeviceRestrictions():
	def __init__(self, devices, type):
		self.devices = devices # Collection of Strings e.g. 'desktop'
		self.type = type # String e.g. 'whitelist'
		
class Event():
	def __init__(self, competitions, date, id, links, name, season, shortName, status, uid):
		competitionCollection = []
		for competition in competitions:
			competitionCollection.append(Competition(**competition))
		self.competitions = competitionCollection # Collection of Competitions

		self.date = date # String rep. of Date '2021-01-26T03:00Z'
		self.id = id # String rep of number; e.g. '401267427'

		linkCollection = []
		for link in links:
			linkCollection.append(Link(**link))
		self.links = linkCollection # Collection of Links

		self.name = name # String of Full name
		self.season = Season(**season) # Season Object
		self.shortName = shortName # String e.g. 'OKC @ POR'
		self.status = Status(**status) # Status Object
		self.uid = uid # UserId I assume - String

class GeoBroadcast():
	def __init__(self, lang, market, media, region, type):
		self.lang = lang # String for what language (e.g. 'en')
		self.market = Market(**market) # Market Object
		self.media = Media(**media) # Media Object
		self.region = region # String for region (e.g. 'us')
		self.type = Geo_Type(**type) # GeoType Object

class GeoRestrictions():
	def __init__(self, countries, type):
		self.countries = countries # Collection of Strings e.g. states and countries 'IL'
		self.type = type # String e.g. 'whitelist'
		
class Geo_Type():
	def __init__(self, id, shortName):
		self.id = id # String for Id
		self.shortName = shortName # String for shortName (e.g. 'TV')

class Headline():
	def __init__(self, description, shortLinkText, type, video):
		self.description = description # String long text description
		self.shortLinkText = shortLinkText # String - shortened version of description
		self.type = type # String e.g. 'recap'
		
		videoCollection = []
		for vid in video:
			videoCollection.append(Video(**vid))
		self.video = videoCollection # Collection of Video Objects
		
class LastPlay():
	def __init__(self, id, probability, scoreValue, text, type, athletesInvolved=None, team=None):
	
		if athletesInvolved is not None:
			athleteCollection = []
			for athlete in athleteCollection:
				athleteCollection.append(athlete)
			self.athletesInvolved = athleteCollection
			
		self.id = id # String rep of Id '401267427323'
		self.probability = Probability(**probability) # Probability Object
		self.scoreValue = scoreValue # Int of Score
		self.text = text # String two part - 'End of the ' '2nd Quarter'
		self.type = LastPlay_Type(**type) # Type Object (id, text)
		if team is not None:
			self.team = Team(**team)

class LastPlay_Type():
	def __init__(self, id, text):
		self.id = id # String e.g. '412'
		self.text = text # Two part 'End ' 'Period'

class Leader():
	def __init__(self, abbreviation, displayName, leaders, name, shortDisplayName):
		self.abbreviation = abbreviation # String (e.g.  'Pts', 'Reb'))
		self.displayName = displayName # String giving display name of above (e.g. "Points", "Rebounds")

		statLeaderCollection = []
		for leader in leaders:
			statLeaderCollection.append(StatLeader(**leader))
		self.statLeaders = statLeaderCollection # This is competitors.leaders.leaders (This is a collection of each stat)

		self.name = name # This is the string for name (e.g. 'points')
		self.shortDisplayName = shortDisplayName # This is the short displayName (e.g. 'Pts')

class League():
	def __init__(self, abbreviation, calendar, calendarEndDate, calendarIsWhitelist, calendarStartDate, calendarType, id, name, season, slug, uid):
		self.abbreviation = abbreviation # String e.g. 'NBA'
		self.calendar = calendar # Collection of String Dates e.g '2020-12-11T08:00Z'
		self.calendarEndDate = calendarEndDate # String of Date e.g. '2020-12-11T08:00Z'
		self.calendarIsWhitelist = calendarIsWhitelist # Bool
		self.calendarStartDate = calendarStartDate # String of date e.g. '2020-12-11T08:00Z'
		self.calendarType = calendarType # Enum I assume e.g. 'day'
		self.id = id # String of Int e.g. '46'
		self.name = name # String long name e.g. 'National Basketball Association'
		self.season = League_Season(**season) # Season Object
		self.slug = slug # String e.g. 'nba' - Not sure what this represents
		self.uid = uid # String of id e.g. 's:40~l:46'

class League_Season():
	def __init__(self, endDate, startDate, type, year):
		self.endDate = endDate
		self.startDate = startDate
		self.type = Season_Type(**type)
		self.year = year
		
class Linescore():
	def __init__(self, value):
		self.value = value # Float representing lineScore (e.g. 24.0)

class Link():
	def __init__(self, href, isExternal=None, isPremium=None, language=None, rel=None, shortText=None, text=None):
		self.href = href # String address of espn home screen for player
		self.isExternal = isExternal # Bool
		self.isPremium = isPremium # Bool
		self.language = language # String e.g. 'en-us'
		self.rel = rel # Collection of Strings
		self.shortText = shortText # Optional ShortText e.g. 'Gamecast'
		self.text = text # String representing first rel it looks like (e.g. 'Clubhouse')

class Market():
	def __init__(self, id, type):
		self.id = id # String representing id
		self.type = type # String (e.g. 'National', 'Home', 'Away')

class Media():
	def __init__(self, shortName):
		self.shortName = shortName # ShortName of Media (e.g. 'NBATV')

class Odd():
	def __init__(self, details, overUnder, provider):
		self.details = details	# details string (e.g. 'POR -5.5')
		self.overUnder = overUnder # Float (e.g. 224.5)
		self.provider = Provider(**provider)


class Position():
	def __init__(self, abbreviation):
		self.abbreviation = abbreviation # String for position shortened (e.g. 'SG' - Starting Guard)

class Probability():
	def __init__(self, awayWinPercentage, homeWinPercentage, tiePercentage):
		self.awayWinPercentage = awayWinPercentage # Float 0.76
		self.homeWinPercentage = homeWinPercentage # Float 0.24
		self.tiePercentage = tiePercentage # Float 0.0

class Provider():
	def __init__(self, id, name, priority):
		self.id = id # string ID (e.g. '45')
		self.name = name	# 2 part string (e.g. 'William Hill ' '(New Jersey)')
		self.priority = priority # Int

class Record():
	def __init__(self, abbreviation, name, summary, type):
		self.abbreviation = abbreviation # This seems optional as not all have it, String
		self.name = name # String maybe 2 parts (e.g. 'All ' 'Splits', or 'Home')
		self.summary = summary # Summary of record as string (e.g. '9-6')
		self.type = type # Possibly Enum (e.g. 'road', 'home', 'total')

class Season():
	def __init__(self, type, year, slug=None):
		self.slug = slug # TODO: We need to figure this out
		self.type = type # Int e.g. 2 - NONOPTIONAL
		self.year = year # Int e.g. 2021 - NONOPTIONAL

class Season_Type():
	def __init__(self, abbreviation, id, name, type):
		self.abbreviation = abbreviation # String 'reg'
		self.id = id # String rep of Int e.g. '1'
		self.name = name # String - 'Regular Season'
		self.type = type # Int e.g. 2

class Situation():
	def __init__(self, lastPlay):
		self.lastPlay = LastPlay(**lastPlay)

class Statistic():
	def __init__(self, abbreviation, displayValue, name, rankDisplayValue=None):
		self.abbreviation = abbreviation # Abbreviation of name: (e.g. '3P%')
		self.displayValue = displayValue # Display value of Number: '31.8'
		self.name = name # This is probably enum (e.g. 'threePointFieldGoalPct')
		self.rankDisplayValue = rankDisplayValue # String of rank in stat

class StatLeader():
	def __init__(self, athlete, displayValue, team, value):
		self.athlete = Athlete(**athlete) # Athlete
		self.displayValue = displayValue # String representing number (e.g. '13')
		self.team = Team(**team) # Team Object
		self.value = value # Float value of stat (e.g. 13.0)

class Status():
	def __init__(self, clock, displayClock, period, type):
		self.clock = clock # Float e.g. 0.0
		self.displayClock = displayClock # String of above as displayed (e.g. '11:42')
		self.period = period # Int
		self.type = Status_Type(**type) # StatusType object

class Status_Type():
	def __init__(self, completed, description, detail, id, name, shortDetail, state):
		self.completed = completed # Bool
		self.description = description # String (e.g. 'Schedule', 'Halftime')
		self.detail = detail # Multi-line String (e.g. 'Mon, January ' '25th at 10:00 PM' 'EST', or one line 'Halftime')
		self.id = id # String of Number '1'
		self.name = name	# enum of 'STATUS_SCHEDULED, STATUS_HALFTIME'
		self.shortDetail = shortDetail # String (e.g. '1/25 - ' '10:00 PM ' 'EST')
		self.state = state # String probably enum (e.g. 'pre')

class Ticket():
	def __init__(self, links, numberAvailable, summary):
		linksCollection = []
		for link in links:
			linksCollection.append(Link(**link))
		self.links = linksCollection
		
		self.numberAvailable = numberAvailable
		self.summary = summary
		
class Team():
	def __init__(self, id, abbreviation=None, alternateColor=None, color=None, displayName=None, isActive=None, links=None, location=None, logo=None, name=None, shortDisplayName=None, uid=None, venue=None):
		self.abbreviation = abbreviation # Abbreviation of team name (e.g. 'IND')
		self.alternateColor = alternateColor # String representing alternateColor: (e.g. '00275d')
		self.color = color # This is the color String (e.g. '061642')
		self.displayName = displayName # This is the display name of the team (e.g. 'Indiana ' 'Pacers')
		self.id = id # String representing number as id (e.g. '11')
		self.isActive = isActive # Bool

		if links is not None:
			linkCollection = []
			for link in links:
				linkCollection.append(Link(**link))
			self.links = linkCollection # Collection of Links

		self.location = location # String of location (e.g. 'Indiana')
		self.logo = logo # Link to the logo of the team as a String
		self.name = name # String of Name (e.g. 'Pacers')
		self.shortDisplayName = shortDisplayName # String of shortName (e.g. 'Pacers')
		self.uid = uid # String of UID, might be userID (e.g. 's:40~l:46~t:11')
		self.venue = venue # Venue object

class Tracking():
	def __init__(self, coverageType, leagueName, sportName, trackingId, trackingName):
		self.coverageType = coverageType # String 'Final ' 'Game ' 'Highlight'
		self.leagueName = leagueName # String 'No ' 'League'
		self.sportName = sportName # String 'nba'
		self.trackingId = trackingId # String 'dm_210125_NBA_Highlight_lebron_sot_full'
		self.trackingName = trackingName # String - MultiPart
		
class Venue():
	def __init__(self, address, capacity, fullName, id, indoor):
		self.address = Address(**address) # Address Object
		self.capacity = capacity # Int e.g. 19441
		self.fullName = fullName # String 'Moda Center'
		self.id = id # String of id (e.g. 2183) - NONOPTIONAL
		self.indoor = indoor # Bool

class Video():
	def __init__(self, deviceRestrictions, duration, geoRestrictions, headline, id, links, source, thumbnail, tracking):
		self.deviceRestrictions = DeviceRestrictions(**deviceRestrictions) # DeviceRestriction Object
		self.duration = duration # Int e.g. 120 I assume seconds
		self.geoRestrictions = GeoRestrictions(**geoRestrictions) # GeoRestrictions object
		self.headline = headline # String
		self.id = id # Int 30779413
		
		# TODO: Links is a mess in VSCode for example formatting
		self.links = links
		self.source = source # String e.g. 'espn'
		self.thumbnail = thumbnail # String representing thumbnail link
		self.tracking = Tracking(**tracking) # Tracking Object
		
#class VideoLink():
#	def __init__
