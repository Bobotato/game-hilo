from pydantic import BaseModel


class Card(BaseModel):
    rank: str
    suit: str


class Player(BaseModel):
    username: str
    credits: int


class RoundInfo(BaseModel):
    player: Player
    current_card: Card


class RoundResult(BaseModel):
    drawn_card: Card
    win: bool
    is_player_bankrupt: bool
    is_deck_empty: bool
