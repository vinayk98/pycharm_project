def game():
    output = 'you make the wrong choice.sorry you dead.Better luck next time. '
    d = input('************* Mr. Aayush , choose  one number from door1 or door2,if you want to win gold*************:')
    if d == 'door1':
        print('wow! you make the write choice.you complete first stage of stage of second level.**')
        d = input('************* Mr. Aayush , choose  one number from 1 or 2,if you want to win gold**********:')
        if d == '1':
            print('wow! you make the write choice.you complete first stage of stage of second level.**')
            e = input('******* MR. Aayush choose one number from 3 or 4,if you want to win gold*******:')
            if e == '3':
                print('wow!you make the write choice.you complete first stage of stage of second level.**')
                f = input('Mr. Aayush, choose  one number from  5 or 6,if you want to win gold:')
                if f == 5:
                    print('wow!you make the write choice.you complete first stage of stage of second level.**')
                    e = str(input('******who is the pm of india******:'))
                    if e == 'jumlebaaj':
                        print('$$$$$$$$$$congratulations! Mr. Aayush, you win.and the gold.enjoy your day.$$$$$$$$')
                    else:
                        return output
                else:
                    return output
            else:
                return output
        else:
            return output
    else:
        return output
    return output


print(game())