import json

# input:
# base_site,
# [{
#   "home_name": "Bayer Leverkusen",
#    "away_name": "Club Brugge",
#    "outcome_1": 1640,
#    "outcome_X": 4600,
#    "outcome_2": 5200
#  },
#   {'site': 'toto', 'outcome_1': 1.2, 'outcome_X': 4.6, 'outcome_2': 5.2},
#   {'site': 'betcity', 'outcome_1': 2.2, 'outcome_X': 3.6, 'outcome_2': 4.2}
# ]


def combine_match(base_site, all_match_odds):
    home_name = all_match_odds[0]['home_name']
    away_name = all_match_odds[0]['away_name']
    outcome_1 = max([
        {'site': match_odds['site'], 'odds': match_odds['outcome_1']} for match_odds in all_match_odds], key=lambda x: x['odds'])
    outcome_x = max([
        {'site': match_odds['site'], 'odds': match_odds['outcome_x']} for match_odds in all_match_odds], key=lambda x: x['odds'])
    outcome_2 = max([
        {'site': match_odds['site'], 'odds': match_odds['outcome_2']} for match_odds in all_match_odds], key=lambda x: x['odds'])
    return {
        "home_name": home_name,
        "away_name": away_name,
        "outcome_1": outcome_1,
        "outcome_x": outcome_x,
        "outcome_2": outcome_2}


def reformat_match(base_site, match_odds):
    home_name = match_odds['home_name']
    away_name = match_odds['away_name']
    outcome_1 = {'site': base_site, 'odds': match_odds['outcome_1']}
    outcome_x = {'site': base_site, 'odds': match_odds['outcome_x']}
    outcome_2 = {'site': base_site, 'odds': match_odds['outcome_2']}

    return {
        "home_name": home_name,
        "away_name": away_name,
        "outcome_1": outcome_1,
        "outcome_x": outcome_x,
        "outcome_2": outcome_2}


def merge(scrapes):
    # use the longest json as the base
    base = scrapes.pop(scrapes.index(max(scrapes, key=len)))
    base_site = base.pop(0)['site']
    result = []

    for match in base:
        # get first teams name to hold against other scrapes
        home_team = match['home_name']
        away_team = match['away_name']
        all_match_odds = [match]
        for scrape in scrapes:
            scrape_site = scrape[0]['site']
            for scrap in scrape[1:]:
                if scrap['home_name'] == home_team and scrap['away_name'] == away_team:
                    all_match_odds.append(
                        {'site': scrape_site, 'outcome_1': scrap['outcome_1'], 'outcome_x': scrap['outcome_x'], 'outcome_2': scrap['outcome_2']})
        # Found all the match occurences in the other scrape results
        # saved in the following format:
        # [{'site': 'toto', 'outcome_1': 1.2, 'outcome_X': 4.6, 'outcome_2': 5.2},
        #  {'site': 'betcity', 'outcome_1': 2.2, 'outcome_X': 3.6, 'outcome_2': 4.2}
        # ]
        if len(all_match_odds) > 1:
            result.append(combine_match(base_site, all_match_odds))
        else:
            result.append(reformat_match(base_site, match))
        # TODO een else waarin alleen de base moet worden omgeschreven tot gewenste format
    print(len(result))
    save_to_json(file="output/merged_output.json", data=result)
    return result


def save_to_json(file, data):
    """
    Save data to a file as json.
    """
    # TODO include meta data of included sites
    with open(file, "w", encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


if __name__ == '__main__':
    a = [
        {"site": "unibet"},
        {
            "home_name": "Bayer Leverkusen",
            "away_name": "Club Brugge",
            "outcome_1": 1640,
            "outcome_X": 4600,
            "outcome_2": 5200
        },
        {
            "home_name": "FC Porto",
            "away_name": "Atlético Madrid",
            "outcome_1": 2750,
            "outcome_X": 3450,
            "outcome_2": 2750
        }, ]
    b = [
        {"site": "toto"},
        {
            "home_name": "Al-Nasr SC",
            "away_name": "Al Kuwait SC",
            "outcome_1": 6.0,
            "outcome_X": 2.5,
            "outcome_2": 1.91
        }, {
            "home_name": "Bayer Leverkusen",
            "away_name": "Club Brugge",
            "outcome_1": 1.2,
            "outcome_X": 4.6,
            "outcome_2": 5.2}
    ]
    c = [
        {"site": "betcity"},
        {
            "home_name": "Al-Nasr SC",
            "away_name": "Al Kuwait SC",
            "outcome_1": 6.0,
            "outcome_X": 2.5,
            "outcome_2": 1.91
        }, {
            "home_name": "Bayer Leverkusen",
            "away_name": "Club Brugge",
            "outcome_1": 1.2,
            "outcome_X": 4.6,
            "outcome_2": 5.2}
    ]

    merge([a, b, c])
    # save_to_json(file="output/merged_output.json", data=bets)
