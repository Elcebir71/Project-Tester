if __name__ == '__main__':

   def minion_game(string):
    vowels = 'AEIOU'
    cons = 'BCDFGHJKLMNPQRSTUWXYZ'
    turn = 0
    count_vwls, count_cons = 0, 0
    turn_1, turn_2 = 0, 0
    while turn < len(string):
        if turn == 0:
            count_cons =sum( {x : sum([1 for char in string if char == x ]) for x in cons}.values())
            count_vwls = sum({x : sum([1 for char in string if char == x ]) for x in vowels}.values())
            turn+=1
        else:
            while turn < len(string):

                    sub_str=string[i][i+1]
                if sub_str[0] in vowels:
                    count_vwls=+count_vwls
                else:
                    count_cons=+count_cons
            turn+=1
    if count_vwls > count_cons:
        return print("Kevin %i"%(count_vwls))
    elif count_vwls < count_cons:
        return print("Stuart %i" % (count_cons))
    else:
        return print("Draw")
s = input()
minion_game(s)