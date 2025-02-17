![HiloLogo](https://github.com/user-attachments/assets/d003683a-edb3-417e-8596-5cbadae9db1f)

# Hilo
A browser based hi-lo card game. This was my first deployed full-stack project created as as part of the learning process to go from no experience to full-stack.

How to play:
Hi-lo is a simple card game in which the player is presented an initial card and is tasked to guess if a following card will be higher or lower in terms of value. The player has a credit carrying wallet and must bet on his/her guess. The aim of the game is to increase the player's wallet value as much as possible without reaching 0.

Game Rules:

1. The Cards
The game uses a standard 52 card deck (Ace to King, Club, Heart, Spade and Diamond Suits). The card values are ascending, with Ace being the lowest value and King being the highest value. In the case of a tie, the suits are valued in ascending order: Diamonds, Hearts, Clubs, Spades.

2. Betting
The player starts with a wallet with 100 credits. The player can bet any amount less or equal to their wallet value. Twice the bet is returned on a successful guess.

## Stack

Frontend:
- [Vue3](https://vuejs.org/)
- [Typescript](https://typescriptlang.org/)
- [TailwindCSS](https://tailwindcss.com/)

Backend:
- [FastAPI](https://fastapi.tiangolo.com/)
- [Python](https://www.python.org/)

DB:
- [PostgreSQL](https://www.postgresql.org/)

Testing:
- [Pytest](https://www.pytest.org/)

## Running the project
The project can be run locally using Docker compose. The docker images are also conveniently uploaded to Dockerhub for use with a deployment using your preferred cloud service provider. The provided Terraform and Ansible files are for use with a DigitalOcean based deployment.

## Credits
Many thanks to Nik for teaching me for the entirety of this project, as well as Royce and Tim for being my classmates and providing helpful advice and learning points.
