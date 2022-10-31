import json

import requests

MAIN_SECTION_STRING = "MAIN"
TOURNAMENT_WIDGET_STRING = "TOURNAMENT"
BET_TYPE_MATCH = 2


def get_footbal_feed():
    """
    Return the current .json footbal feed from Unibet.
    """
    url = (
        "https://unibet.nl/sportsbook-feeds/views/filter/football/all/matches?includeParticipants=true&useCombined=true"
    )

    response = requests.get(url)
    data = response.json()
    return data


def extract_bets(feed):
    """
    Extract all the match bets from an input feed.
    """
    sections = feed["layout"]["sections"]
    main_section = [
        section for section in sections if section["position"] == MAIN_SECTION_STRING][0]

    widgets = main_section["widgets"]
    tournament_widget = [
        widget for widget in widgets if widget["widgetType"] == TOURNAMENT_WIDGET_STRING][0]

    match_groups = tournament_widget["matches"]["groups"]

    master_events = []
    for group in match_groups:
        for sub_group in group["subGroups"]:
            master_events.extend(sub_group["events"])

    result = []
    for event in master_events:
        bet_offers = event["betOffers"]
        filtered_offer = [
            offer for offer in bet_offers if offer["betOfferType"]["id"] == BET_TYPE_MATCH]

        if len(filtered_offer) == 0:
            continue

        outcomes = filtered_offer[0]["outcomes"]
        result.append(prepare_bet(outcomes))

    return result


def prepare_bet(outcomes):
    """
    Return a dict object with the odds for a given match.
    """
    outcome_1 = [outcome for outcome in outcomes if outcome["label"] == "1"][0]
    outcome_x = [outcome for outcome in outcomes if outcome["label"] == "X"][0]
    outcome_2 = [outcome for outcome in outcomes if outcome["label"] == "2"][0]

    return {
        "home_name": outcome_1["participant"],
        "away_name": outcome_2["participant"],
        "outcome_1": outcome_1["odds"] if "odds" in outcome_1 else None,
        "outcome_X": outcome_x["odds"] if "odds" in outcome_x else None,
        "outcome_2": outcome_2["odds"] if "odds" in outcome_2 else None,
    }


def save_to_json(file, data):
    """
    Save data to a file as json.
    """
    meta = [{"site": 'unibet', }]
    with open(file, "w", encoding='utf8') as f:
        json.dump(meta + data, f, ensure_ascii=False)


def main():
    """
    Extract all the current footbal bets listed on Unibet.
    """
    feed = get_footbal_feed()
    bets = extract_bets(feed)
    print(len(bets))
    save_to_json(file="output/unibet_output.json", data=bets)


if __name__ == "__main__":
    main()
