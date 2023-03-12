from models.Card import Card

def generate_cards(raw_card_list: list[str]) -> list[Card]:
    if not isinstance(raw_card_list, list):
        raise TypeError(f'Argument must be of type list, got {type(raw_card_list)} instead')
    if not all(isinstance(item, str) for item in raw_card_list):
        raise TypeError(f'Elements of Argument must be type str')
    return [Card(card_str[0], card_str[1]) for card_str in raw_card_list]