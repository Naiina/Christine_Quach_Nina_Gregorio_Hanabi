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
        
    
        if game.blue_coins = 0:
            actions=['p','d']
            random.shuffle(actions)
            return("%s%d" % (actions[0], random.randint(1,5)))
        if game.blue_coins = 8:
            actions=['p','c']
            random.shuffle(actions)
            if actions[0]=='p':
                return("p%d" %random.randint(1,5))
            else:
                
                color=[r,b,y,w,g]
                colorornumber=random.randint(1,2)
                if colorornumber==1:
                    return("c%d" %random.randint(1,5))
                else:
                    return("c%s" %(random.shuffle(color)[0]))
        else:
            actions=['d','c','p']
            random.shuffle(actions)
            if actions[0]=='c':

                color=[r,b,y,w,g]
                colorornumber=random.randint(1,2)
                if colorornumber==1:
                    return("c%d" %random.randint(1,5))
                else:
                    return("c%s" %(random.shuffle(color)[0]))
            else:
                return("%s%d" % (actions[0], random.randint(1,5)))
            










