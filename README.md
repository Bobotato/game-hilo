# game-hilo
A browser based hi-lo card game. 

How to play:
Hi-lo is a simple card game in which the player is presented an initial card and is tasked to guess if a following card will be higher or lower in terms of value. The player has a wallet and must bet on his/her guess. The aim of the game is to increase the player's wallet value as much as possible without reaching 0.

Game Rules:

1. The Cards
The game uses a standard 52 card deck (Ace to King, Club, Heart, Spade and Diamond Suits). The card values are ascending, with Ace being the lowest value and King being the highest value. In the case of a tie, the suits are valued in ascending order: Diamonds, Hearts, Clubs, Spades.

2. Betting
The player starts with a wallet with 100 credits. The player can bet any amount less or equal to their wallet value. Twice the bet is returned on a successful guess.

Architecture:

Frontend:
The frontend is built using Vue3 and is served using nginx.

Backend:
The backend is built using Python, the API is built using fastAPI and accesses the DB with SQLalchemy.

Database:
The database is a PostgreSQL database.
