from pydantic import BaseModel


class InfoIn(BaseModel):
    access_token: str


class InfoOut(BaseModel):
    player: dict
    current_card: dict

    class Config:
        orm_mode = True


class ResultIn(BaseModel):
    bet: int
    prediction: int
    access_token: str


class ResultOut(BaseModel):
    drawn_card: dict
    win: bool
    is_player_bankrupt: bool
    is_deck_empty: bool

    class Config:
        orm_mode = True
