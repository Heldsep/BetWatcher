import json

import requests

HOME_WIN = "H"
DRAW = "D"
AWAY_WIN = "A"


def get_footbal_feed():
    """
    Return the current .json footbal feed from Toto.
    """
    url = (
        "https://content.toto.nl/content-service/api/v1/q/event-list?includeChildMarkets=true&marketSortsIncluded=MR&drilldownTagIds=11"
    )

    response = requests.get(url)
    data = response.json()
    return data


def extract_bets(feed):
    """
    Extract all the match bets from an input feed.
    """
    entries = feed["data"]["events"]

    matches = [entry["markets"][0]["outcomes"] for entry in entries]

    result = []

    for match in matches:
        result.append(prepare_bet(match))

    return result


def prepare_bet(match):
    """
    Return a dict object with the odds for a given match.
    """
    outcome_1 = [bet for bet in match if bet["subType"] == HOME_WIN]
    outcome_x = [bet for bet in match if bet["subType"] == DRAW]
    outcome_2 = [bet for bet in match if bet["subType"] == AWAY_WIN]

    return {
        "site": 'toto',
        "home_name": outcome_1[0]["name"] if outcome_1 else '',
        "away_name": outcome_2[0]["name"] if outcome_2 else '',
        "outcome_1": outcome_1[0]["prices"][0]["decimal"] if outcome_1 else 0,
        "outcome_x": outcome_x[0]["prices"][0]["decimal"] if outcome_x else 0,
        "outcome_2": outcome_2[0]["prices"][0]["decimal"] if outcome_2 else 0,
    }


def save_to_json(file, data):
    """
    Save data to a file as json.
    """
    with open(file, "w", encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


def main():
    """
    Extract all the current footbal bets listed on Unibet.
    """
    feed = get_footbal_feed()
    bets = extract_bets(feed)
    print(len(bets))
    save_to_json(file="output/toto_output.json", data=bets)
    return bets


if __name__ == "__main__":
    main()
