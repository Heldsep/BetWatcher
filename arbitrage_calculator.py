import json


def save_to_json(file, data):
    """
    Save data to a file as json.
    """
    with open(file, "w", encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


def calculate(input):
    matches = []
    for match in input:
        if arbitrage(match['outcome_1']['odds'], match['outcome_x']['odds'], match['outcome_2']['odds']):
            matches.append(match)
    print(len(matches))
    save_to_json(file="output/arbitrage_matches.json", data=matches)


def arbitrage(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return False
    else:
        return (1/a + 1/b + 1/c) < 1
