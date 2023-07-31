# game-hilo
A terminal based hi-lo card game.

How to play:
Hi-lo is a simple card game in which the player is presented an initial card and is tasked to guess if a following card will be higher or lower in terms of value. The player has a wallet and must bet on his/her guess. The aim of the game is to increase the player's wallet value as much as possible without reaching 0.

Game Rules:

1. The Cards
The game uses a standard 52 card deck (Ace to King, Club, Heart, Spade and Diamond Suits). The card values are ascending, with Ace being the lowest and King being the highest. There is no distinction between the value of the suits.

2. Betting
The player starts with a wallet with 100 credits. The player can bet any amount less or equal to his wallet value. The player wins a multiple of his bet based on the probability of him/her being correct (higher probabilities = lower payout multiple). The player forfeits his/her bet if the guess is wrong.

3. Win/Lose Conditions
The player wins if his prediction is correct. Draws and wrong guesses are counted as losses. The game is considered over if the player's wallet reaches 0 and he/she is unable to bid.

Architecture:








