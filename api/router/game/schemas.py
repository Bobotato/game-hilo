from pydantic import BaseModel


class Bet(BaseModel):
    bet: int


class Card(BaseModel):
    rank: str
    suit: str


class Player(BaseModel):
    username: str
    credits: int


class Prediction(BaseModel):
    prediction: str


class RoundInfo(BaseModel):
    player: dict
    current_card: dict


class RoundResult(BaseModel):
    drawn_card: dict
    win: bool
    is_player_bankrupt: bool
    is_deck_empty: bool
