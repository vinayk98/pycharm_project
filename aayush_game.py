def game():
    c = input('********* Mr. Aayush choose one door of the temple to exit,door1 or door2***********:')
    if c == 'door2':
        return 'sorry! you are dead .because you make the wrong choice.'
    else:
        print('**wow! you make the right choice and now you go to  the second level**')
        d = input('************* Mr. Aayush , choose  one number from 1 or 2,if you want to win gold*************:')
        if d == '2':
            return 'oh sorry! you are dead .because you make the wrong choice.'
        else:
            print('***wow! you make the right choice.And you complete the first stage of stage of second level.**')
            e = input('******* MR. Aayush choose one number from 3 or 4,if you want to win gold*******:')
            if e == 4:
                return 'sorry! you are dead .because you make the wrong choice.'
            else:
                print('***wow! Mr. Aayush,you make the right choice. and now are very near to win gold,carry on. ***')
                f = input('Mr. Aayush, choose  one number from  5 or 6,if you want to win gold:')
                if f == 6:
                    return ' oh! you lose,but you are very near to win gold.Better luck next time.'
                else:
                    print('***wow! you are at the phase of the game.this is right chance to win gold**')
                    e = input('******who is the pm of india******:')
                    if e == 'jumlebaaj':
                        return '$$$$$$$$$$congratulations! Mr. Aayush, you win.and the gold.enjoy your day.$$$$$$$$$$'
                    else:
                        return ' oh! you lose,but you are very near to win gold.Better luck next time.'


print(game())
