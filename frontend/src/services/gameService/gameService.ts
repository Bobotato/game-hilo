function startGame(currentCard) {
    if(currentCard == null) {
        currentCard = drawCard()
    }
}



// def get_bet(game: Game) -> int:    
//     while True:                   
//         print(                    
//             f"\nYou have {game.player.credits} credits.\n"    
//             "How much would you like to bet?\n"    
//         )                         
                                  
//         try:                      
//             bet = int(input("> "))    
//         except ValueError:        
//             print("Please only input whole numbers.\n")    
//             continue              
                                  
//         if bet > game.player.credits:    
//             print("You cannot bet more credits than you have.\n")    
                                  
//         elif bet <= 0:            
//             print("You cannot bet 0 or negative amounts.\n")    
                                  
//         else:                     
//             return bet    

// def get_prediction(round_info: RoundInfo) -> Prediction:
//     while True:
//         print(
//             f"The current card is {round_info.current_card}.\n"
//             "Will the drawn card be higher or lower?\n"
//             "[1] Higher\n"
//             "[2] Lower\n"
//         )
//         prediction = input("> ")

//         try:
//             return Prediction(int(prediction))
//         except ValueError:
//             print("Please only use 1 for higher or 2 for lower.")

// def is_continuing() -> bool:
//     while True:
//         print("Would you like to continue?\n[1] Yes\n[2] No\n")
//         continuing = input("> ")

//         if continuing == "1":
//             return True

//         elif continuing == "2":
//             return False

//         else:
//             print("Please only input either 1 or 2.")


// def is_game_over(round_result: RoundResult) -> bool:
//     return round_result.is_player_bankrupt or round_result.is_deck_empty

// def is_restarting() -> bool:
//     while True:
//         print(
//             "Would you like to try again with 100 credits?\n"
//             "[1] Yes\n"
//             "[2] No\n"
//         )
//         restart = input("> ")

//         if restart == "1":
//             print("Credits will reset to 100, and the deck will be populated.")
//             return True

//         elif restart == "2":
//             return False

//         else:
//             print("Please only input 1 to restart or 2 to quit.")
