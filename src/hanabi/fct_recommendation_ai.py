def hint_into_number(hint,currentplayernumber):
#    tab=[['c1A','c2A','c3A','c4A','crA','cjA','cvA','cbA'],['c1B','c2B','c3B','c4A','crA','cjA','cvA','cbA'],['c1A','c2A','c3A','c4A','crA','cjA','cvA','cbA'],['c1A','c2A','c3A','c4A','crA','cjA','cvA','cbA'],['c1A','c2A','c3A','c4A','crA','cjA','cvA','cbA'],['c1A','c2A','c3A','c4A','crA','cjA','cvA','cbA']] ****pb: hint=1 2 3 4 r b j v ???
 
    tabnumber=['1','2','3','4','5']
    i=0
    foundnumber=False
    while i<4:
        if tabnumber[i]==hint[1]:
            foundnumber=True
        i+=1   
    if foundnumber:
        i=0
    else:
        i=4

    tabplayer=['A','B','C','D','E','A','B','C','D','E']  
    j=currentplayernumber
    foundplayer=False
    while not foundplayer:
        if tabplayer[j]==hint[2]:
            foundplayer=True
        else:
            j+=1   
    j=j-currentplayernumber
    print(j)         
    return(i+j)


def number_into_hint(number,currentplayernumber):
        tab=[['c1B','c1C','c1D','c1E','crB','crC','crD','crE'],['c1C','c1D','c1E','c1A','crC','crD','crE','crA',],['c1D','c1E','c1A','c1B','crD','crE','crA','crB'],['c1E','c1A','c1B','c1C','crE','crA','crB','crC',],
['c1A','c1B','c1C','c1D','crA','crB','crC','crD']]

        return(tab[currentplayernumber][number])

move=['p1','h','yy','ctt','c1','fff','h','hh','ph','p2']
def the_most_recent_recommendation():
    NumberOfMoves=len(move)-1
    i=0
    while i<=NumberOfMoves:
        if move[NumberOfMoves-i][0]=='c':
            return(move[NumberOfMoves-i])
        i+=1
    return('no recommendation')
#what happens if recommendation='nothing'





def rank_of_second_last_card_played():
    NumberOfMoves=len(move)-1
    i=0
    FirstClue=False
    while i<=NumberOfMoves and not FirstClue:
        if move[NumberOfMoves-i][0]=='p':
            FirstClue=True
        i+=1
    j=i
    if FirstClue:
        while j<=NumberOfMoves:
            if move[NumberOfMoves-j][0]=='p':
                return(move[NumberOfMoves-j])
            j+=1
        
    return(-1)

rank_of_last_clue=5
rank_of_last_card_played=-1

def no_card_has_been__played_since_the_last_hint():
    if rank_of_last_clue<0:
        return(False)
    if rank_of_last_clue<0:
        return(True)
    return(rank_of_last_clue>rank_of_last_card_played)
#tested with rank_of.. with ints insted od fonctions



