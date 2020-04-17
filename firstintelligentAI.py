import itertools


class AI:
    """
    AI base class: some basic functions, game analysis.
    """
    def __init__(self, game):
        self.game = game

    @property
    def other_hands(self):
        "The list of other players' hands."
        return self.game.hands[1:]

    @property
    def other_players_cards(self):
        "All of other players's cards, concatenated in a single list."
        # return sum([x.cards for x in self.other_hands], [])
        return list(itertools.chain.from_iterable([hand.cards for hand in self.other_hands]))
        
def not_clued_cards(mycards):
    notcluedcards=[]
    for i in range(len(mycards)):
        card=mycards[i]
        if card.color_clue==False:
            if card.number_clue==False:
                notcluedcards.append((i,card))
    return(notcluedcards)
def one_clued_cards(mycards):
    onecluedcards=[]
    for i in range(len(mycards)):
        card=mycards[i]
        if card.color_clue==False:
            if card.number_clue==True:
                onecluedcards.append((i,card))
        if card.color_clue==True:
            if card.number_clue==False:
                onecluedcards.append((i,card))
    return(onecluedcards)
def randomclue():
    color=[r,b,y,w,g]
    colorornumber=random.randint(1,2)
    if colorornumber==1:
        return("c%d" %random.randint(1,5))
    else:
        return("c%s" %(random.shuffle(color)[0]))
        
    

def count_kown(listcards,comparedcard):
    sum=0
    for card in listcards:
        if comparedcard==card:
            if comparedcard.number_clue==True:
                    if comparedcard.color_clue==True:
                        sum+=1
    return(sum)
def kown_cards(mycards):
    kowncards=[]
    i=-1
    for card in mycards:
        i+=1
        if card.number_clue==True:
            if card.color_clue==True:
                kowncards.append(i,card)
    return(kowncards)


class firstintelligentAI(AI):
    """
    
    Algorithm:
      * if 1-or-more card he know is playable: play the lowest one, then newest one
      * if blue_coin<8 and an unnecessary card present: discard it.
      * if blue_coin>0: give a clue on precious card (so a human can play with a Cheater)
      * if blue_coin<8: discard the largest one, except if it's the last of its kind or in chop position in his opponent.
      
      
      
    
    
    how to choose :
    how to discard a card
        fixme:if no unnecessery card, discard cards without clues
    
    when to play a card
        play when you know it and it is a suitable one
        no card is played and he has a one
        fixme: if you have a clue, the card is intressting, this about how to decide wether the card is to save or not)
        
    how to give clues
        fixme:the card is the last one in the game: first give its number if its unknown, than the color
        fixme:the card can be played: randomly give the number or the color(think about how to improve this)
        
        
if he can play
    play
if coins==0:
    if he has cards he can discard: discard
    if he has cards without clues: discard
    else: discard a random card
if coins==8
    if he can give a clue, give a clue
    else: give a random clue
    
    if blue_coin>=3 
        if he can clue: 
            clue 
        else 
            if he can discard:
                discard
            else:
                if he has cards without clues:
                    discard a random  card without clues, 
                else
                    give a random clue
    if blue_coin<3 
        if he can discard
            discard, 
        else 
            if he can give a clue:
                clue
            else
                if he has cards without clues:
                    discard a random  card without clues, 
                else
                    give a random clue
                    
                    
he can discard if: 
    the card is already placed
    fixme:the card is not presious and far to be placed(two cards are missing to place it)
    fixme:the card is on a dead pile
    other players have the same card
he can play if:
    no card is played and he has a one
    he knows the card and it is suatable
he can give a clue if 
    one player has a suitable card
    one player has a presious card
                    
                    
       
    """
    

    
    
    
    def play(self):
        "Return the best cheater action."
        game = self.game
        if game.piles==[0,0,0,0,0]:
            ones = [ i+1 for (i, card) in
                    enumerate(game.current_hand.cards)
                    if (1== card.number) and (card.number_clue==True)]
            if len(ones)>0:
                return("p%d"%ones[0])
            else:
                ones = [ i+1 for (i, card) in
                        enumerate(self.other_players_cards)
                        if (1== card.number) and (card.number_clue==False)]
                if len(ones)>0:
                    return("c1")
        
        playable=[ (i+1, card.number) for (i, card) in
                     enumerate(game.current_hand.cards)
                     if (game.piles[card.color]+1 == card.number) and (card.number_clue==True) and (card.color_clue==True ]

        
        if playable:
            # sort by ascending number, then newest
            playable.sort(key=lambda p: (p[1], -p[0]))
            print('notCheater would play:', "p%d"%playable[0][0], end=' ')
            if (len(playable) > 1):
                print('but could also pick:', playable[1:])
            else:
                print()

            return "p%d"%playable[0][0]

           
        discardable = [ i+1 for (i, card) in
                        enumerate(game.current_hand.cards)
                        if ( (card.number <= game.piles[card.color])
                             or (game.current_hand.cards.count_kown(card) > 1)
                             
                        ) ]
                        
        # discard already played cards, doubles in my hand
        # fixme: discard doubles, if I see it in partner's hand
        # fixme: il me manque les cartes sup d'une pile morte

        

        ## 2nd type of discard: I have a card, and my partner too

        for 
        discardable2 = [ i+1 for (i, card) in kown_cards(game.current_hand.cards)
                         if card in self.other_players_cards
        
        if game.blue_coins == 0:
            if discardable:
                return "d%d"%discardable[0]
            if discardable2:
                return "d%d"%discardable2[0]
            notcluedcards=not_clued_cards(game.current_hand.cards)
            if notcluedcards:
                random.shuffle(notcluedcards)
                return('d%d'%notcluedcards[0][0])
            onecluedcards=one_clued_cards(game.current_hand.cards)
            if onecluedcards:
                random.shuffle(onecluedcards)
                return('d%d'%onecluedcards[0][0])
            else:
                return('d%d'%random.randint(1,5))
        if game.blue_coins == 8: #?????
             
                
                       ]
        if game.blue_coins < 3:
            if discardale:
                    print('Cheater would discard2:', "d%d"%discardable2[0], discardable2)
            return "d%d"%discardable[0]

            if discardable2 and (game.blue_coins < 3):
            
                print('notCheater would discard:', "d%d"%discardable[0], discardable)
                return "d%d"%discardable2[0]
            
            
        ## Look at other precious cards in other hand, to clue them
        Oprecious = [ card for card in
                     self.other_players_cards
                     if (1+game.discard_pile.cards.count(card))
                         == game.deck.card_count[card.number]
                   ]
        if Oprecious:
            clue = False
            # this loop is such that we prefer to clue an card close to chop
            # would be nice to clue an unclued first, instead of a already clued
            for p in Oprecious:
                # print(p, p.number_clue, p.color_clue)
                if p.number_clue is False:
                    clue = "c%d"%p.number
                    break
                if p.color_clue is False:
                    clue = "c%s"%p.color
                    clue = clue[:2]   # quick fix, with 3+ players, can't clue cRed anymore, only cR
                    break
                # this one was tricky:
                # don't want to give twice the same clue
        
            if clue:
                
                
                
                
                
                
                print('Cheater would clue a precious:',
                       clue, Oprecious)
                if game.blue_coins > 0:
                    return clue
                print("... but there's no blue coin left!")
        notCluedCards=not_clued_cards(game.current_hand.cards)
        if notCluedCards:
            random.shuffle(notCluedCards)
            retrun('d%d'%notCluedCards[0][0])
        else:
            return(randomclue)
        
            


        # if reach here, can't play, can't discard safely, no card to clue-save
        # Let's give a random clue, to see if partner can unblock me
        if game.blue_coins > 0:
            print('Cheater would clue randomly: cW')
            return 'cw'

        # If reach here, can't play, can't discard safely
        # No blue-coin left.
        # Must discard a card. Let's choose a non-precious one (preferably a 4)
        mynotprecious = [ (card.number, i+1) for (i, card) in
                          kown_cards(game.current_hand.cards)
                          if not (
                                  (1+game.discard_pile.cards.count(card))
                                  == game.deck.card_count[card.number])
                     ]
        mynotprecious.sort(key=lambda p: (-p[0], p[1]))
        if mynotprecious:
            act = 'd%d'%mynotprecious[0][1]
            print('Cheater is trapped and must discard:', act, mynotprecious)
            return act

        # Oh boy, not even a safe discard, this is gonna hurt!
        # it's a loss. Discard the biggest
        myprecious = [ (card.number, i+1) for (i, card) in enumerate(game.current_hand.cards) ]
        myprecious.sort(key=lambda p: (-p[0], p[1]))
        act = 'd%d'%myprecious[0][1]
        print('Cheater is doomed and must discard:', act, myprecious)
        return act