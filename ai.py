"""
Artificial Intelligence to play Hanabi.
"""

import itertools
import random


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

class Random(AI):
    """
    This player plays random
    Algorithm:
      actions:
        c:gives a clue
        p:play a card
        d:discard a card
      * if blue_coin=0 chooserandomly between p and d
      * if blue_coin=8:choose randomly between c and p
      * else choose randomly between c d and p
    """
    
    
    def play(self):
        "Return a random possible action."
        game = self.game
        
    
        if game.blue_coins == 0:
            actions=['p','d']
            random.shuffle(actions)
            return("%s%d" % (actions[0], random.randint(1,5)))
        if game.blue_coins == 8:
            actions=['p','c']
            random.shuffle(actions)
            if actions[0]=='p':
                return("p%d" %random.randint(1,5))
            else:
                
                color=['r','b','y','w','g']
                colorornumber=random.randint(1,2)
                if colorornumber==1:
                    return("c%d" %random.randint(1,5))
                else:
                    return("c%s" %(random.choice(color)))
        else:
            actions=['d','c','p']
            random.shuffle(actions)
            if actions[0]=='c':

                color=['r','b','y','w','g']
                colorornumber=random.randint(1,2)
                if colorornumber==1:
                    return("c%d" %random.randint(1,5))
                else:
                    return("c%s" %(random.choice(color)))
            else:
                return("%s%d" % (actions[0], random.randint(1,5)))
            



class Cheater(AI):
    """
    This player can see his own cards!

    Algorithm:
      * if 1-or-more card is playable: play the lowest one, then newest one
      * if blue_coin<8 and an unnecessary card present: discard it.
      * if blue_coin>0: give a clue on precious card (so a human can play with a Cheater)
      * if blue_coin<8: discard the largest one, except if it's the last of its kind or in chop position in his opponent.
    """

    def play(self):
        "Return the best cheater action."
        game = self.game
        playable = [ (i+1, card.number) for (i, card) in
                     enumerate(game.current_hand.cards)
                     if game.piles[card.color]+1 == card.number ]

        if playable:
            # sort by ascending number, then newest
            playable.sort(key=lambda p: (p[1], -p[0]))
            print('Cheater would play:', "p%d"%playable[0][0], end=' ')
            if (len(playable) > 1):
                print('but could also pick:', playable[1:])
            else:
                print()

            return "p%d"%playable[0][0]

        #
        discardable = [ i+1 for (i, card) in
                        enumerate(game.current_hand.cards)
                        if ( (card.number <= game.piles[card.color])
                             or (game.current_hand.cards.count(card) > 1)
                        ) ]
        # discard already played cards, doubles in my hand
        # fixme: discard doubles, if I see it in partner's hand
        # fixme: il me manque les cartes sup d'une pile morte

        if discardable and (game.blue_coins < 8):
            print('Cheater would discard:', "d%d"%discardable[0], discardable)
            return "d%d"%discardable[0]

        ## 2nd type of discard: I have a card, and my partner too

        discardable2 = [ i+1 for (i, card) in enumerate(game.current_hand.cards)
                         if card in self.other_players_cards
                       ]
        if discardable2 and (game.blue_coins < 8):
            print('Cheater would discard2:', "d%d"%discardable2[0], discardable2)
            return "d%d"%discardable2[0]


        ## Look at precious cards in other hand, to clue them
        precious = [ card for card in
                     self.other_players_cards
                     if (1+game.discard_pile.cards.count(card))
                         == game.deck.card_count[card.number]
                   ]
        if precious:
            clue = False
            # this loop is such that we prefer to clue an card close to chop
            # would be nice to clue an unclued first, instead of a already clued
            for p in precious:
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
                       clue, precious)
                if game.blue_coins > 0:
                    return clue
                print("... but there's no blue coin left!")


        # if reach here, can't play, can't discard safely, no card to clue-save
        # Let's give a random clue, to see if partner can unblock me
        if game.blue_coins > 0:
            print('Cheater would clue randomly: cW')
            return 'cw'

        # If reach here, can't play, can't discard safely
        # No blue-coin left.
        # Must discard a card. Let's choose a non-precious one (preferably a 4)
        mynotprecious = [ (card.number, i+1) for (i, card) in
                          enumerate(game.current_hand.cards)
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



def count_kown(listcards,comparedcard):
    sum=0
    for card in listcards:
        if comparedcard==card:
            if comparedcard.number_clue is not False:
                    if comparedcard.color_clue is not False:
                        sum+=1
    return(sum)
def kown_cards(mycards):
    kowncards=[]
    i=-1
    for card in mycards:
        i+=1
        if card.number_clue is not False:
            if card.color_clue is not False:
                kowncards.append( (i,card) )
    return(kowncards)
    


class NotCheater(AI):
    """
    This player can see his own cards!
    Algorithm:
      * if 1-or-more card is playable and kown: play the lowest one, then newest one
      * if blue_coin<8 and an unnecessary card present: discard it.
      * if blue_coin>0: give a clue on precious card (so a human can play with a Cheater)
      * if blue_coin<8: discard the largest one, except if it's the last of its kind or in chop position in his opponent.
    """

    def play(self):
        "Return the best cheater action."
        game = self.game
        print(game.piles)
        if list(game.piles.values()) ==[0,0,0,0,0]:
            ones = [ i+1 for (i, card) in
                    enumerate(game.current_hand.cards)
                    if card.number == 1 and card.number_clue is not False]
            if len(ones)>0:
                return("p%d"%ones[0])
                sys.exit(0)
            else:
                ones = [ i+1 for (i, card) in
                        enumerate(self.other_players_cards)
                    if card.number == 1 and card.number_clue is False]
                if len(ones)>0:
                    return("c1")
        
        playable=[ (i+1, card.number) for (i, card) in
                     enumerate(game.current_hand.cards)
                     if game.piles[card.color]+1 == card.number and card.number_clue is not False and card.color_clue is not False]

        
        if playable:
            # sort by ascending number, then newest
            playable.sort(key=lambda p: (p[1], -p[0]))
            print('notCheater would play:', "p%d"%playable[0][0], end=' ')
            if (len(playable) > 1):
                print('but could also pick:', playable[1:])
            else:
                print()

            return "p%d"%playable[0][0]
        precious = [ card for card in
                     self.other_players_cards
                     if (1+game.discard_pile.cards.count(card))
                         == game.deck.card_count[card.number]
                   ]
       
        if precious:
            clue = False
            # this loop is such that we prefer to clue an card close to chop
            # would be nice to clue an unclued first, instead of a already clued
            for p in precious:
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
                       clue, precious)
                if game.blue_coins > 0:
                    return clue
                print("... but there's no blue coin left!")


        #
        discardable = [ i+1 for (i, card) in
                        kown_cards(game.current_hand.cards)
                        if ( (card.number <= game.piles[card.color])
                             or (count_kown(game.current_hand.cards, card) > 1)
                             
                        ) ]
                        
        # discard already played cards, doubles in my hand
        # fixme: discard doubles, if I see it in partner's hand
        # fixme: il me manque les cartes sup d'une pile morte

        if discardable and (game.blue_coins < 8):
            print('notCheater would discard:', "d%d"%discardable[0], discardable)
            return "d%d"%discardable[0]

        ## 2nd type of discard: I have a card, and my partner too

        
        discardable2 = [ i+1 for (i, card) in kown_cards(game.current_hand.cards)
                         if card in self.other_players_cards
                       ]
        if discardable2 and (game.blue_coins < 8):
            print('Cheater would discard2:', "d%d"%discardable2[0], discardable2)
            return "d%d"%discardable2[0]


        ## Look at precious cards in other hand, to clue them
        

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

class Smart(AI):

    def deduce_number(self,hand):
    """ 
    Cette fonction donne une recommendation de type liste (ex : R=["p",1]) pour seule main. Mais ici on prend p=-1 et d=3
    pour que la fonction renvoie R[0]+R[1] qui se trouve entre 0 et 7. 
    """
    """
    On definit 3 types de cartes : 
        - playable : celles que l'on peut mettre sur une les piles 
        - dead : les cartes qui sont deja dans les piles (deja jouees)
        - indispensable : les cartes dont il ne reste qu'un exemplaire (pas encore joue)
    """
        game=self.game

        playable = [ (i+1, card.number) for (i, card) in
                    enumerate(hand.cards)
                    if game.piles[card.color]+1 == card.number]

        dead = [ i+1 for (i, card) in
                enumerate(hand.cards)
                if ( card.number <= game.piles[card.color])]

        indispensable = [ card for card in
                     hand.cards
                     if (1+game.discard_pile.cards.count(card))
                         == game.deck.card_count[card.number]
                        ]
    """
    La recommendation est faite selon les 5 priorites :
        Numero 1 : Si dans la liste playable et non vide il y en a une de rang 5 on la joue, si il y en a plusieur on joue 
        la plus petite d'indice.
        Numero 2 : Si la liste playable est non vide : jouer celle de rang le plus petit, si il y en a plusieurs, on joue la
        plus petite d'indice.
        Numero 3 : Si liste dead est non vide : jeter celle d'indice (dans la main) la plus petite. 
        Numero 4 : Si dead est vide, jeter carte de rang LE PLUS GRAND, PAS dans indispensable. Si il y en a plusieurs, on joue
        la plus petite d'indice.
        Numero 5 : jeter carte 1. 
    """

        R=[0,0]
        if playable : 
            R[0]=(-1)

        #CAS NUMERO 1 
            #on trie les cartes par ordre decroissant de rang, et par anciennete les plus anciennes avant
            playable.sort(key=lambda p: (-p[1],p[0]))
            if playable[0][1]==5 :
                R[1]=playable[0][0]
                return (R[0]+R[1])

        #CAS NUMERO 2 
            #on trie les cartes par ordre croissant de rang et par anciennete les plus anciennes avant
            playable.sort(key=lambda p: (p[1],p[0]))
            R[1]=playable[0][0]
            return (R[0]+R[1])

        #CAS NUMERO 3 
        if dead : 
            dead.sort()
            R=[3,dead[0]]
            return (R[0]+R[1])

        #CAS NUMERO 4
        if indispensable : 
            intersection=[ (i+1, card.number) for (i, card) in
                    enumerate(hand.cards)
                    if (card not in indispensable)]

            if intersection : 
                intersection.sort(key=lambda p: (-p[1],p[0]))
                R[0]=3
                R[1]=intersection[0][0]
                return (R[0]+R[1])

        #CAS NUMERO 5
        R=[3,1]
        return (R[0]+R[1]) 



    def give_a_hint(self):
        """
        On fait la somme des recommendations (en chiffre) pour chaque main, modulo 7, appele hint. 
        Puis, a ce chiffre hint, on associe la liste A=[rang ou couleur, numero joueur]. 
        Enfin, on donne l'indice.
        """
        game=self.game

        s=0
        for hand in self.other_hands :
            s=s+deduce_number(self,hand)
        hint=s%7

        IND=[[1,1],[1,2],[1,3],[1,4],["R",1],["R",2],["R",3],["R",4]]
        A=IND[hint]

        return A 
        #ou direct hanabi.deck.Game.clue(game,A) c'est comme tu veux haha 
