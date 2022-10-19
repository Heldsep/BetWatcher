https://content.toto.nl/content-service/api/v1/q/event-list?minPrice=1.25&maxPrice=9.90&numOutcomes=3&startTimeFrom=2022-10-19T19%3A42%3A35Z&startTimeTo=2022-10-20T19%3A42%3A35Z&marketSortsIncluded=HH%2CMR

https://content.toto.nl/content-service/api/v1/q/time-band-event-list?maxMarkets=10&marketSortsIncluded=--%2CHH%2CHL%2CMR%2CWH&marketGroupTypesIncluded=MONEYLINE%2CROLLING_SPREAD%2CROLLING_TOTAL%2CSTATIC_SPREAD%2CSTATIC_TOTAL&allowedEventSorts=MTCH&includeChildMarkets=true&prioritisePrimaryMarkets=true&includeCommentary=true&includeMedia=true&drilldownTagIds=12&maxTotalItems=25&maxEventsPerCompetition=3&maxCompetitionsPerSportPerBand=2&maxEventsForNextToGo=5&startTimeOffsetForNextToGo=600&dates=2022-10-20T22%3A00%3A00Z%2C2022-10-21T22%3A00%3A00Z%2C2022-10-22T22%3A00%3A00Z

https://content.toto.nl/content-service/api/v1/q/event-list?includeChildMarkets=true&prioritisePrimaryMarkets=true&drilldownTagIds=12

url for all matches in the HH and MR market:

https://content.toto.nl/content-service/api/v1/q/event-list?includeChildMarkets=true&marketSortsIncluded=HH%2CMR

Alternatives for /event-list? are:
    /time-band-event-list? (orders the json in sections LIVE, Up next, Tomorrow, etc. used fot he tabs on top of a page)
    /popular-bets-event-list? (to fill up the recommended betslip somewhere on screen)

&includeChildMarkets=true is set to also get the specific bets and their odds

&drilldownTagIds=12 can be used to select a specific competition or sport (the higher the number the more specific)
    - American football: 3
    - Soccer: 11
    - Baseball: 4
    - Basketball: 5
    - Boxing: 6
    - Ice Hockey: 8
    - Mixed Martial Arts: 9
    - Premier League (soccer): 567

Multiple sportcategories which can be accessed/filtered by their name and (alphabetical) id ("category":{"id":"34","name":"Tennis",...})
    - American footbal: 1
    - Badminton: 4
    - Baseball: 6
    - Basketball: 7
    - Boxing: 11
    - Cricket: 12
    - Darts: 15
    - Soccer: 17
    - Ice Hockey: 26
    - Mixed Martial Arts: 27
    - Snooker: 32
    - Table tennis: 33
    - Tennis: 34
    - Volleybal: 35
I did not find (by trying sensible things) a parameter that would filter the json based on sportId

Multiple markets (&marketSortsIncluded=HH%2CMR), 
    - HH (head to head, 1v1, either home or away wins)
    - MR (match result, home, away or draw)
    - HL ?
    - WH ?