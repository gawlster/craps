import random


MIN_DIE = 1
MAX_DIE = 6
MAX_CHIPS = 100000
MIN_BET = 20
MAX_BET = 100000


'''
NOTES FOR ADDITIONS
- a valid UI with dice animations
- different bets possible, not just a 1:1 bet on a seven or point value
--------> need to learn different tyoes of craps bets from youtube... ADDED DONT PASS LINE AND ODDS BETS, TRY TO ADD HIGH STAKES BETS
- confirmation of cashing out... COMPLETED
'''



def play_craps() -> None:
    """ simulates a game of Craps according to the following algorithm
    - allows the user to buy 0 or more dollars worth of casino chips
    - allows the user to continually play rounds of Craps 
    while they have at least MIN_BET dollars worth of casino chips left and 
    they still want to play again
    - In a round:
    -- the user makes a valid bet
    -- the round of Craps is played and 
    if they win the round they win the amount they bet, 
    otherwise they lose the amount they bet.  
    -- The updated number of dollars worth of casino chips is printed
    
    - when the user is done playing, a cashout message is printed
    """    
    #TODO: complete this function
    num_chips = buy_casino_chips()
    if num_chips < MIN_BET:
        cashout(num_chips)
    
    else:
        playing = play_again()
        while playing and num_chips >= MIN_BET:
            change_in_balance = make_bet(num_chips)
            num_chips += change_in_balance
            print('Your new chip count is:', num_chips)
            if num_chips < MIN_BET:
                break
            else:
                playing = play_again()
    
    
        cashout(num_chips)
    
    
    
    
    
    

def buy_casino_chips() -> int:
    """ Prompts user for the amount of chips they want to buy in whole dollars.
    Keeps prompting user until a value of at least $0
    but no more than MAX_CHIPS is entered
    """
    #TODO: complete this function... COMPLETED
    buy_prompt = 'Enter a whole number between 0 and 100000 inclusive: '
    retry_buy_prompt = 'Not a valid transaction - Enter a whole number between 0 and 100000 inclusive: '
    
    print('Buy your chips here! How many dollars do you want?')
    chip_count = input(buy_prompt)
    
    while not chip_count.isdigit() or int(chip_count) > MAX_CHIPS:
        chip_count = input(retry_buy_prompt)
    
    chip_count = int(chip_count)
    return chip_count
    


def make_bet(num_chips: int) -> int:
    """ repeatedly prompts user to make a valid bet that is at least MIN_BET 
    but does not go over MAX_BET or num_chips.
    Returns the amount of the valid bet.
    """
    #TODO: complete this function... COMPLETED
    bet_type_prompt = 'Choose your bet type: Enter 1 for pass line, 2 for don\'t pass line: '
    
    bet_type = input(bet_type_prompt)
    
    while not bet_type.isdigit() or int(bet_type) > 2 or int(bet_type) == 0:
        bet_type = input(bet_type_prompt)
            
    if int(bet_type) == 1:
        winnings = pass_line(num_chips)
        return winnings
    elif int(bet_type) == 2:
        winnings = not_pass_line(num_chips)
        return winnings
    
    
    
    

def play_again() -> bool:
    """ Prompts the user to determine whether they want to play again.
    Returns True if the user enters 'yes' and False otherwise.
    """
    #TODO: complete this function... COMPLETED
    play_again_prompt = 'Do you want to play? Please enter \'yes\' if you do: '
    confirmation = 'You are about to cash out your chips - enter \'yes\' to confirm: '
    
    play = input(play_again_prompt)
    
    if play == 'yes':
        return True
    else:    
        while play != 'yes':
            confirm = input(confirmation)
            while confirm == 'yes':
                return False
            play = input(play_again_prompt)
        return True
    
    
    

def cashout(num_chips: int) -> None:
    """  Prints goodbye message to user:
    Says they are broke if they have less than MIN_BET chips left. 
    Prints how many dollars worth of chips they are cashing out.
    """
    #TODO: complete this function... COMPLETED
    bye_message = 'Thank you, please come again!'
    broke_message = 'We are sorry, but you do not have enough chips to play'
    cash_out_message_p1 = 'You are cashing out $'
    cash_out_message_p2 = ' in chips'
    confirmation = 'You are about to cash out your chips - enter \'yes\' to confirm'
    
    if num_chips < MIN_BET:
        print(broke_message)
    else:
        print(bye_message)
    print(cash_out_message_p1, num_chips, cash_out_message_p2, sep='')
    
    


def roll_dice() -> int:
    """ simulates the roll of 2 dice and returns the sum of the two
    """
    two_die = roll_one_die() + roll_one_die()
    return two_die

def roll_one_die() -> int:
    """ simulates the roll of a single die and returns the value
    """
    die = random.randint(MIN_DIE, MAX_DIE)
    return die



def determine_og_winnings(bet: int, if_won: bool, win_pays: int) -> int:
    '''
    takes the bet placed and whether the round was won or lost and returns the amount won or lost then tells the player how much they won or lost
    '''
    if if_won:
        winnings = bet * win_pays
        print('You won $', winnings, ' from your pass line bet!', sep='')
        return winnings
    else:
        loss = bet
        print('Unfortunately, you lost your $', loss, ' bet from your pass line bet', sep='')
        loss = bet * -1
        return loss
    
    
    
    
def pass_line(num_chips: int) -> int:
    '''
    if the player selects pass line, they will be directed to this function to make their bet
    '''
    win_pays = 1
    
    winnings = 0
    odds_num = 0
    odds_betting_amount = 0
    odds_pays = 0    
    odds_winnings = 0
    
    bet_prompt = 'Place your bet: '
    bet_parameters = 'A valid bet must be between $20 and $5000 but must not exceed your chip count'
    retry_bet_parameters = 'Invalid bet - A valid bet must be between $20 and $5000 but must not exceed your chip count'
    pass_line_rules = 'Welcome to the pass line... win on a 7 or 11, lose on a 2, 3, or 12... \notherwise hope for the first roll to be rolled again before a 7, have fun!'
    
    # MAKE A BET HERE
    if num_chips < MAX_BET:
        valid_max = num_chips
    else:
        valid_max = MAX_BET
    
    print(pass_line_rules)
    print(bet_parameters)
    bet = input(bet_prompt)
    
    while not bet.isdigit() or int(bet) > valid_max or int(bet) < MIN_BET:
        print(retry_bet_parameters)
        print('Your chip count is: ', num_chips)
        bet = input(bet_prompt)
    
    bet = int(bet)
    
    # PLAY THE ROUND HERE
    point_value = 0
    result = roll_dice()
    print('First roll was: ', result)
    if result == 7 or result == 11:
        won = True
    elif result == 2 or result == 3 or result == 12:
        won = False
    else:
        point_value = result
        
        additional_bet_prompt = 'Would you like to place an odds bet? Enter \'yes\' if you do: '
        add_bets = input(additional_bet_prompt)
        if add_bets == 'yes':
            #call additional bet functions
            odds_num = odds_bets(num_chips, point_value)
            odds_betting_amount = odds_bet_amount(num_chips)
            
            if odds_num == 4 or odds_num == 10:
                odds_pays = 2
            elif odds_num == 5 or odds_num == 9:
                odds_pays = 3/2
            elif odds_num == 6 or odds_num == 8:
                odds_pays = 6/5
        
        result = roll_dice()
        print('You then rolled: ', result)
        
        if result == odds_num:
            print('Congratulations... you won your odds bet of $', odds_betting_amount, ' at a payout value of ', odds_pays, sep='')
            odds_winnings = odds_betting_amount * odds_pays
        else:
            odds_winnings = -1 * odds_betting_amount
        
        while result != 7 and result != point_value:
            result = roll_dice()
            print('You then rolled: ', result)
            if result == odds_num:
                print('Congratulations... you won your odds bet of $', odds_betting_amount, ' at a payout value of ', odds_pays, sep='')
                odds_winnings = odds_betting_amount * odds_pays 
            else:
                odds_winnings = -1 * odds_betting_amount
        
        if result != 7:
            won = True
        else:
            won = False
            
    
    winnings = odds_winnings + determine_og_winnings(bet, won, win_pays)
    return int(winnings)




def not_pass_line(num_chips: int) -> int:
    '''
    if the player selects dont pass line, they will be directed to this function
    '''
    win_pays = 1
    
    winnings = 0
    odds_num = 0
    odds_betting_amount = 0
    odds_pays = 0
    odds_winnings = 0
    
    bet_prompt = 'Place your bet: '
    bet_parameters = 'A valid bet must be between $20 and $5000 but must not exceed your chip count'
    retry_bet_parameters = 'Invalid bet - A valid bet must be between $20 and $5000 but must not exceed your chip count'
    pass_line_rules = 'Welcome to the don\'t pass line... win on 2, 3, or 12, lose on a 7 or 11... \notherwise hope for a 7 before the first roll is rolled again, have fun!'
    
    if num_chips < MAX_BET:
        valid_max = num_chips
    else:
        valid_max = MAX_BET
    
    print(pass_line_rules)
    print(bet_parameters)
    bet = input(bet_prompt)
    
    while not bet.isdigit() or int(bet) > valid_max or int(bet) < MIN_BET:
        print(retry_bet_parameters)
        print('Your chip count is: ', num_chips)
        bet = input(bet_prompt)
    
    bet = int(bet)
    
    #PLAY ROUND HERE
    point_value = 0
    result = roll_dice()
    print('First roll was: ', result)
    if result == 7 or result == 11:
        won = False
    elif result == 2 or result == 3 or result == 12:
        won = True
    else:
        point_value = result
        
        additional_bet_prompt = 'Would you like to place an odds bet? Enter \'yes\' if you do: '
        add_bets = input(additional_bet_prompt)
        if add_bets == 'yes':
            #call additional bet functions
            odds_num = odds_bets(num_chips, point_value)
            odds_betting_amount = odds_bet_amount(num_chips)
            
            if odds_num == 4 or odds_num == 10:
                odds_pays = 2
            elif odds_num == 5 or odds_num == 9:
                odds_pays = 3/2
            elif odds_num == 6 or odds_num == 8:
                odds_pays = 6/5            
        
        result = roll_dice()
        print('You then rolled: ', result)
        
        if result == odds_num:
            print('Congratulations... you won your odds bet of $', odds_betting_amount, ' at a payout value of ', odds_pays, sep='')
            odds_winnings = odds_betting_amount * odds_pays
        else:
            odds_winnings = -1 * odds_betting_amount
        
        while result != 7 and result != point_value:
            result = roll_dice()
            print('You then rolled: ', result)
            if result == odds_num:
                print('Congratulations... you won your odds bet of $', odds_betting_amount, ' at a payout value of ', odds_pays, sep='')
                odds_winnings = odds_betting_amount * odds_pays
            else:
                odds_winnings = -1 * odds_betting_amount
        
        if result != 7:
            won = False
        else:
            won = True
    
    winnings = odds_winnings + determine_og_winnings(bet, won, win_pays)
    return int(winnings)



def odds_bets(num_chips: int, point_value: int) -> int:
    '''
    odds bets are placed after a point value is established... they can be placed on 4 thru 10 except 7
    if that number is rolled before the 7 or the point value, they win
    betting a 4 or 10 is 2:1 odds
    betting a 5 or 9 is 3:2 odds
    betting a 6 or 8 is 6:5 odds
    '''
    pass_odds_prompt = 'Welcome to odds bets! \n4 and 10 pay 2:1, 5 and 9 pay 3:2, 6 and 8 pay 6:5 \nIf the number you bet on is rolled before a 7 or the point value(You may place odds bets on the point value), you win \nEnter either a 4, 5, 6, 8, 9, or 10 representing the number you are betting on: '
    retry_odds_prompt = 'Please enter 4, 5, 6, 8, 9, or 10: '
    
    num_bet_on = input(pass_odds_prompt)
    
    while not num_bet_on.isdigit() or int(num_bet_on) > 10 or int(num_bet_on) < 4 or int(num_bet_on) == 7:
        num_bet_on = input(retry_odds_prompt)
        
    return int(num_bet_on)
    

def odds_bet_amount(num_chips: int):
    '''
    determines how much the player is betting for their odds bet
    '''
    odd_amount_prompt = 'How much would you like to bet for your odds bet? Enter amount here: '
    
    if num_chips < MAX_BET:
        max_valid_bet = num_chips
    else:
        max_valid_bet = MAX_BET
    
    bet_amount = input(odd_amount_prompt)
    
    while not bet_amount.isdigit() or int(bet_amount) > max_valid_bet:
        print('Your chip count is', num_chips)
        bet_amount = input('Your bet must be between $20 and $5000 and may not exceed you chip count. Enter your bet here: ')
    
    return int(bet_amount)










play_craps()