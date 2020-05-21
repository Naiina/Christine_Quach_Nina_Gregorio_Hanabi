import unittest
import hanabi



class ColorTest(unittest.TestCase):
    def test_str(self):
        colors = [(31, "Red"), (32, "Green"), (34, "Blue"), (33, "Yellow"), (37, "White")]
        trouve = True
        for (c, color) in colors:
            a = str(hanabi.deck.Color(c))
            self.assertEqual(a, color)
    def test_valid(self):
        for s in (54, 78, 46, 54, -5, 3):
            self.assertRaises(ValueError, hanabi.deck.Color, s)


class CardTest(unittest.TestCase):
    def test_not_equal_cards(self):
        c1 = hanabi.deck.Card('B', 4)
        c2 = hanabi.deck.Card('R', 4)
        self.assertNotEqual(c1, c2)

    def test_equal_cards(self):
        c1 = hanabi.deck.Card('R', 4)
        string_card = "R4"
        self.assertEqual(c1, string_card)

    def test_number(self):
        #self.assertRaises(hanabi.deck.Card('R', 7),  AssertionError)
        with self.assertRaises(AssertionError):
            hanabi.deck.Card('R', 7)
    # TODO: itertools.product to test that all cards are possible

class HandTest(unittest.TestCase):
    # test __special__ functions


    # test normal functions
    def setUp(self):
        self.deck1 = hanabi.deck.Deck()
        self.hand1 = hanabi.deck.Hand(self.deck1)
        self.deck1.shuffle()

        self.deck3 = hanabi.deck.Deck()
        self.hand3 = hanabi.deck.Hand(self.deck3, 1)

    def test_basic_hand(self):
        self.assertEqual(str(self.hand3), hanabi.deck.Card(hanabi.deck.Color.Red, 1).str_color())

    def test_len(self):
        self.assertEqual(5, len(self.hand1))
    
    def test_shuffle(self):
        self.deck1.shuffle()
        mem = str(self.deck1)[0:len(repr(self.hand1))]
        self.hand2 = hanabi.deck.Hand(self.deck1)
        self.assertEqual(str(self.hand2), mem)



class DeckTest(unittest.TestCase):
    # test __special__ functions
    

    # test normal functions
    def setUp(self):
        pass


    def test_shuffle(self):
        pass


    def test_draw(self):
        pass

    def test_deal(self):
        pass


class DeckTest2(unittest.TestCase):
    pass



class GameTest(unittest.TestCase):

    def setUp(self):
        self.unshuffled_game = hanabi.Game()
        self.random_game = hanabi.Game()
        # ... group G here! 
        self.predefined_game = hanabi.Game()
        # ...


    # lines 193, 227
    def test_A1(self):
        game = hanabi.Game(2)
        game.quiet = True
        game.turn('p3')  # check that we can play blindly

    # lines 227, 261
    def test_B1(self):
        pass


    # lines 261, 295
    def test_play_R2_over_R1(self):
        pass


    # lines 295, 329
    def test_add_blue_coin1(self):
        self.blue_coins = 8
        self.assertRaises(ValueError,hanabi.deck.Game.add_blue_coin,self)

    def test_add_blue_coin2(self):
        self.blue_coins = 4
        hanabi.deck.Game.add_blue_coin(self)
        self.assertEqual(5,self.blue_coins)

    def test_remove_blue_coin1(self):
        self.blue_coins = 0
        self.assertRaises(ValueError,hanabi.deck.Game.remove_blue_coin,self)

    def test_remove_blue_coin2(self):
        self.blue_coins = 3
        hanabi.deck.Game.remove_blue_coin(self)
        self.assertEqual(2,self.blue_coins)

    def test_add_red_coin1(self):
        self.red_coins = 2
        self.assertRaises(StopIteration,hanabi.deck.Game.add_red_coin,self)

    def test_add_red_coin2(self):
        self.red_coins = 0
        hanabi.deck.Game.add_red_coin(self)
        self.assertEqual(1,self.red_coins)    


    # lines 329, 363

    

    # lines 363, 397
    def test_clue1(self):
        game = hanabi.Game(2)
        game.blue_coins = 4
        hanabi.deck.Game.clue(game,["R","B"])
        self.assertEqual(3,game.blue_coins)

    def test_clue2(self):
        game = hanabi.Game(2)
        self.assertRaises(ValueError,hanabi.deck.Game.clue,game,["T","B"])

    def test_clue3(self):  
        game = hanabi.Game(2)
        self.assertRaises(ValueError,hanabi.deck.Game.clue,game,["R","A"])      


    # lines 397, 431
    
class AiTest(unittest.TestCase):

    def test_deduce_number_1(self):
        """
        Test si il y a un 5 jouable, recommende de le jouer
        """
        game = hanabi.Game(5)
        ai=hanabi.ai.RecommendationStrategy(game)
        c1 = hanabi.deck.Card(hanabi.deck.Color.Green,4)
        c2 = hanabi.deck.Card(hanabi.deck.Color.Red,2)
        c3 = hanabi.deck.Card(hanabi.deck.Color.Blue,5)
        c4 = hanabi.deck.Card(hanabi.deck.Color.Blue,2)
        ok=hanabi.deck.Deck([c1,c2,c3,c4]) 
        hand = hanabi.deck.Hand(ok, 4)  
        game.piles[hanabi.deck.Color.Blue]=4
        game.piles[hanabi.deck.Color.Red]=1
        game.piles[hanabi.deck.Color.Green]=3
        game.piles[hanabi.deck.Color.Yellow]=1
        self.assertEqual(hanabi.ai.RecommendationStrategy.deduce_number(ai,hand), 2)


    def test_deduce_number_2(self):
        """
        Test si toutes les cartes sont mortes, recommande de jeter la premiere carte
        """
        game = hanabi.Game(5)
        ai=hanabi.ai.RecommendationStrategy(game)
        c1 = hanabi.deck.Card(hanabi.deck.Color.Blue,1)
        c2 = hanabi.deck.Card(hanabi.deck.Color.Red,1)
        c3 = hanabi.deck.Card(hanabi.deck.Color.Green,1)
        c4 = hanabi.deck.Card(hanabi.deck.Color.Yellow,1)
        ok=hanabi.deck.Deck([c1,c2,c3,c4]) 
        hand = hanabi.deck.Hand(ok, 4) 
        game.piles[hanabi.deck.Color.Blue]=2
        game.piles[hanabi.deck.Color.Red]=2
        game.piles[hanabi.deck.Color.Green]=2
        game.piles[hanabi.deck.Color.Yellow]=2
        self.assertEqual(hanabi.ai.RecommendationStrategy.deduce_number(ai,hand), 4)

    def test_deduce_number_3(self):
        """
        Test si toutes les cartes sont indispensables, recommande de jeter la premiere
        """
        game = hanabi.Game(5)
        ai=hanabi.ai.RecommendationStrategy(game)
        c1 = hanabi.deck.Card(hanabi.deck.Color.Blue,5)
        c2 = hanabi.deck.Card(hanabi.deck.Color.Red,5)
        c3 = hanabi.deck.Card(hanabi.deck.Color.Green,5)
        c4 = hanabi.deck.Card(hanabi.deck.Color.Yellow,5)
        ok=hanabi.deck.Deck([c1,c2,c3,c4]) 
        hand = hanabi.deck.Hand(ok, 4) 
        game.piles[hanabi.deck.Color.Blue]=2
        game.piles[hanabi.deck.Color.Red]=2
        game.piles[hanabi.deck.Color.Green]=2
        game.piles[hanabi.deck.Color.Yellow]=2
        self.assertEqual(hanabi.ai.RecommendationStrategy.deduce_number(ai,hand), 4)

    def test_deduce_number_4(self):
        """
        Test si aucune cartes nest morte et aucune carte nest jouable, mais que les cartes 1 2 et 4 sont indispensables, 
        recommande de jeter la 3 
        """
        game = hanabi.Game(5)
        ai=hanabi.ai.RecommendationStrategy(game)
        c1 = hanabi.deck.Card(hanabi.deck.Color.Blue,5)
        c2 = hanabi.deck.Card(hanabi.deck.Color.Red,5)
        c3 = hanabi.deck.Card(hanabi.deck.Color.Green,4)
        c4 = hanabi.deck.Card(hanabi.deck.Color.Yellow,5)
        ok=hanabi.deck.Deck([c1,c2,c3,c4]) 
        hand = hanabi.deck.Hand(ok, 4) 
        game.piles[hanabi.deck.Color.Blue]=2
        game.piles[hanabi.deck.Color.Red]=2
        game.piles[hanabi.deck.Color.Green]=2
        game.piles[hanabi.deck.Color.Yellow]=2
        self.assertEqual(hanabi.ai.RecommendationStrategy.deduce_number(ai,hand), 6)

    def test_deduce_number_5(self):
        game = hanabi.Game(5)
        ai=hanabi.ai.RecommendationStrategy(game)
        c1 = hanabi.deck.Card(hanabi.deck.Color.Blue,5)
        c2 = hanabi.deck.Card(hanabi.deck.Color.Red,1)
        c3 = hanabi.deck.Card(hanabi.deck.Color.Green,1)
        c4 = hanabi.deck.Card(hanabi.deck.Color.Yellow,1)
        game.piles[hanabi.deck.Color.Blue]=4
        game.piles[hanabi.deck.Color.Red]=4
        game.piles[hanabi.deck.Color.Green]=4
        game.piles[hanabi.deck.Color.Yellow]=4
        ok1=hanabi.deck.Deck([c1,c2,c3,c4]) 
        hand1 = hanabi.deck.Hand(ok1, 4)
        self.assertEqual(hanabi.ai.RecommendationStrategy.deduce_number(ai,hand1), 0)

    def test_deduce_number_6(self):
        game = hanabi.Game(5)
        ai=hanabi.ai.RecommendationStrategy(game)
        c1 = hanabi.deck.Card(hanabi.deck.Color.Blue,1)
        c2 = hanabi.deck.Card(hanabi.deck.Color.Red,5)
        c3 = hanabi.deck.Card(hanabi.deck.Color.Green,1)
        c4 = hanabi.deck.Card(hanabi.deck.Color.Yellow,1)
        game.piles[hanabi.deck.Color.Blue]=4
        game.piles[hanabi.deck.Color.Red]=4
        game.piles[hanabi.deck.Color.Green]=4
        game.piles[hanabi.deck.Color.Yellow]=4
        ok1=hanabi.deck.Deck([c1,c2,c3,c4]) 
        hand1 = hanabi.deck.Hand(ok1, 4)
        self.assertEqual(hanabi.ai.RecommendationStrategy.deduce_number(ai,hand1), 1)

    def test_hint_into_number(self):
        game = hanabi.Game(5)
        ai=hanabi.ai.RecommendationStrategy(game)
        self.assertEqual(hanabi.ai.RecommendationStrategy.hint_into_number(ai,'c12',1), 1)

    def test_number_into_hint(self):
        game = hanabi.Game(5)
        ai=hanabi.ai.RecommendationStrategy(game)
        self.assertEqual(hanabi.ai.RecommendationStrategy.number_into_hint(ai,5), 'd2')

    def test_give_a_hint_1(self):
        """
        Test si joueur 1 2 et 3 doivent jouer la carte 1 et joueur 4 la carte 2, la recommandation doit etre 0+0+0+1=1 qui donne
        en format indice : 'c12'
        """
        game = hanabi.Game(5)
        ai=hanabi.ai.RecommendationStrategy(game)
        c1 = hanabi.deck.Card(hanabi.deck.Color.Blue,5)
        c2 = hanabi.deck.Card(hanabi.deck.Color.Red,1)
        c3 = hanabi.deck.Card(hanabi.deck.Color.Green,1)
        c4 = hanabi.deck.Card(hanabi.deck.Color.Yellow,1)
        c5 = hanabi.deck.Card(hanabi.deck.Color.Red,5)
        c6 = hanabi.deck.Card(hanabi.deck.Color.Green,5)
        c7 = hanabi.deck.Card(hanabi.deck.Color.Yellow,5)
        game.piles[hanabi.deck.Color.Blue]=4
        game.piles[hanabi.deck.Color.Red]=4
        game.piles[hanabi.deck.Color.Green]=4
        game.piles[hanabi.deck.Color.Yellow]=4
        ok1=hanabi.deck.Deck([c1,c2,c3,c4]) 
        hand1 = hanabi.deck.Hand(ok1, 4)
        ok2=hanabi.deck.Deck([c5,c2,c3,c4])
        hand2 = hanabi.deck.Hand(ok2, 4) 
        ok3=hanabi.deck.Deck([c6,c2,c3,c4])
        hand3 = hanabi.deck.Hand(ok3, 4)
        ok4=hanabi.deck.Deck([c2,c7,c3,c4])
        hand4 = hanabi.deck.Hand(ok4, 4)
        hanabi.ai.RecommendationStrategy.other_hands=[hand1,hand2,hand3,hand4]
        self.assertEqual(hanabi.ai.RecommendationStrategy.give_a_hint(ai), 'c12')

    def test_give_a_hint_2(self):
        game = hanabi.Game(5)
        RS=hanabi.ai.RecommendationStrategy(game) 
        c1 = hanabi.deck.Card(hanabi.deck.Color.Blue,2)
        c2 = hanabi.deck.Card(hanabi.deck.Color.Blue,1)
        c3 = hanabi.deck.Card(hanabi.deck.Color.Green,1)
        c4 = hanabi.deck.Card(hanabi.deck.Color.Yellow,1)

        c5 = hanabi.deck.Card(hanabi.deck.Color.Red,1)
        c6 = hanabi.deck.Card(hanabi.deck.Color.Blue,5)
        c7 = hanabi.deck.Card(hanabi.deck.Color.Green,5)
        c8 = hanabi.deck.Card(hanabi.deck.Color.Yellow,5)

        c9 = hanabi.deck.Card(hanabi.deck.Color.Red,1)
        c10 = hanabi.deck.Card(hanabi.deck.Color.Green,2)
        c11 = hanabi.deck.Card(hanabi.deck.Color.Blue,1)
        c12  = hanabi.deck.Card(hanabi.deck.Color.Green,1)

        c13 = hanabi.deck.Card(hanabi.deck.Color.Green,4)
        c14 = hanabi.deck.Card(hanabi.deck.Color.Yellow,1)
        c15 = hanabi.deck.Card(hanabi.deck.Color.Yellow,2)
        c16 = hanabi.deck.Card(hanabi.deck.Color.Red,5)

        c17 = hanabi.deck.Card(hanabi.deck.Color.Green,3)
        c18 = hanabi.deck.Card(hanabi.deck.Color.Yellow,3)
        c19 = hanabi.deck.Card(hanabi.deck.Color.Red,4)
        c20 = hanabi.deck.Card(hanabi.deck.Color.Blue,4)

        game.piles[hanabi.deck.Color.Blue]=1
        game.piles[hanabi.deck.Color.Red]=1
        game.piles[hanabi.deck.Color.Green]=1
        game.piles[hanabi.deck.Color.Yellow]=1

        ok1=hanabi.deck.Deck([c1,c2,c3,c4]) 
        hand1 = hanabi.deck.Hand(ok1, 4)
        ok2=hanabi.deck.Deck([c5,c6,c7,c8])
        hand2 = hanabi.deck.Hand(ok2, 4) 
        ok3=hanabi.deck.Deck([c9,c10,c11,c12])
        hand3 = hanabi.deck.Hand(ok3, 4)
        ok4=hanabi.deck.Deck([c13,c14,c15,c16])
        hand4 = hanabi.deck.Hand(ok4, 4)
        ok5=hanabi.deck.Deck([c17,c18,c19,c20])
        hand5 = hanabi.deck.Hand(ok5, 4)
        hanabi.ai.RecommendationStrategy.other_hands=[hand1,hand2,hand3,hand4]
        self.assertEqual(hanabi.ai.RecommendationStrategy.give_a_hint(RS), 'cr4')

    def test_deduce_my_moves_2(self):  
        game = hanabi.Game(5)
        RS=hanabi.ai.RecommendationStrategy(game) 
        c1 = hanabi.deck.Card(hanabi.deck.Color.Blue,2)
        c2 = hanabi.deck.Card(hanabi.deck.Color.Blue,1)
        c3 = hanabi.deck.Card(hanabi.deck.Color.Green,1)
        c4 = hanabi.deck.Card(hanabi.deck.Color.Yellow,1)

        c5 = hanabi.deck.Card(hanabi.deck.Color.Red,1)
        c6 = hanabi.deck.Card(hanabi.deck.Color.Blue,5)
        c7 = hanabi.deck.Card(hanabi.deck.Color.Green,5)
        c8 = hanabi.deck.Card(hanabi.deck.Color.Yellow,5)

        c9 = hanabi.deck.Card(hanabi.deck.Color.Red,1)
        c10 = hanabi.deck.Card(hanabi.deck.Color.Green,2)
        c11 = hanabi.deck.Card(hanabi.deck.Color.Blue,1)
        c12  = hanabi.deck.Card(hanabi.deck.Color.Green,1)

        c13 = hanabi.deck.Card(hanabi.deck.Color.Green,4)
        c14 = hanabi.deck.Card(hanabi.deck.Color.Yellow,1)
        c15 = hanabi.deck.Card(hanabi.deck.Color.Yellow,2)
        c16 = hanabi.deck.Card(hanabi.deck.Color.Red,5)

        c17 = hanabi.deck.Card(hanabi.deck.Color.Green,3)
        c18 = hanabi.deck.Card(hanabi.deck.Color.Yellow,3)
        c19 = hanabi.deck.Card(hanabi.deck.Color.Red,4)
        c20 = hanabi.deck.Card(hanabi.deck.Color.Blue,4)

        game.piles[hanabi.deck.Color.Blue]=1
        game.piles[hanabi.deck.Color.Red]=1
        game.piles[hanabi.deck.Color.Green]=1
        game.piles[hanabi.deck.Color.Yellow]=1

        ok1=hanabi.deck.Deck([c1,c2,c3,c4]) 
        hand1 = hanabi.deck.Hand(ok1, 4)
        ok2=hanabi.deck.Deck([c5,c6,c7,c8])
        hand2 = hanabi.deck.Hand(ok2, 4) 
        ok3=hanabi.deck.Deck([c9,c10,c11,c12])
        hand3 = hanabi.deck.Hand(ok3, 4)
        ok4=hanabi.deck.Deck([c13,c14,c15,c16])
        hand4 = hanabi.deck.Hand(ok4, 4)
        ok5=hanabi.deck.Deck([c17,c18,c19,c20])
        hand5 = hanabi.deck.Hand(ok5, 4)
        hanabi.ai.RecommendationStrategy.other_hands=[hand3,hand4,hand5,hand1]
        self.assertEqual(hanabi.ai.RecommendationStrategy.deduce_my_moves(RS,'cr4',3), 'd1')


    def test_deduce_my_moves_1(self):
        game = hanabi.Game(5)
        RS=hanabi.ai.RecommendationStrategy(game)
        c1 = hanabi.deck.Card(hanabi.deck.Color.Blue,5)
        c2 = hanabi.deck.Card(hanabi.deck.Color.Red,1)
        c3 = hanabi.deck.Card(hanabi.deck.Color.Green,1)
        c4 = hanabi.deck.Card(hanabi.deck.Color.Yellow,1)
        c5 = hanabi.deck.Card(hanabi.deck.Color.Red,5)
        c6 = hanabi.deck.Card(hanabi.deck.Color.Green,5)
        c7 = hanabi.deck.Card(hanabi.deck.Color.Yellow,5)
        game.piles[hanabi.deck.Color.Blue]=4
        game.piles[hanabi.deck.Color.Red]=4
        game.piles[hanabi.deck.Color.Green]=4
        game.piles[hanabi.deck.Color.Yellow]=4
        ok1=hanabi.deck.Deck([c1,c2,c3,c4]) 
        hand1 = hanabi.deck.Hand(ok1, 4)
        ok2=hanabi.deck.Deck([c5,c2,c3,c4])
        hand2 = hanabi.deck.Hand(ok2, 4) 
        ok3=hanabi.deck.Deck([c6,c2,c3,c4])
        hand3 = hanabi.deck.Hand(ok3, 4)
        ok4=hanabi.deck.Deck([c2,c4,c3,c4])
        hand4 = hanabi.deck.Hand(ok4, 4)
        hanabi.ai.RecommendationStrategy.other_hands=[hand1,hand2,hand3,hand4]
        self.assertEqual(hanabi.ai.RecommendationStrategy.deduce_my_moves(RS,'c12',4), 'p2')

    def test_play(self):
        game = hanabi.Game(5)
        RS=hanabi.ai.RecommendationStrategy(game)

        c1 = hanabi.deck.Card(hanabi.deck.Color.Blue,1)
        c2 = hanabi.deck.Card(hanabi.deck.Color.Red,2)
        c3 = hanabi.deck.Card(hanabi.deck.Color.Green,1)
        c4 = hanabi.deck.Card(hanabi.deck.Color.Yellow,1)
        c5 = hanabi.deck.Card(hanabi.deck.Color.Blue,3)
        c6 = hanabi.deck.Card(hanabi.deck.Color.Green,3)
        c7 = hanabi.deck.Card(hanabi.deck.Color.Yellow,3)
        game.piles[hanabi.deck.Color.Blue]=0
        game.piles[hanabi.deck.Color.Red]=1
        game.piles[hanabi.deck.Color.Green]=0
        game.piles[hanabi.deck.Color.Yellow]=0
        ok1=hanabi.deck.Deck([c5,c2,c6,c7]) 
        hand1 = hanabi.deck.Hand(ok1, 4)
        ok2=hanabi.deck.Deck([c5,c6,c1,c7])
        hand2 = hanabi.deck.Hand(ok2, 4) 
        ok3=hanabi.deck.Deck([c1,c7,c5,c6])
        hand3 = hanabi.deck.Hand(ok3, 4)
        ok4=hanabi.deck.Deck([c4,c6,c5,c7])
        hand4 = hanabi.deck.Hand(ok4, 4)

        game.red_coins=2
        game.blue_coins=5

        game.moves=['cr4','p2']
        game.memoire=[-1,'p2','p3','p1','d1']

        hanabi.ai.RecommendationStrategy.other_hands=[hand1,hand2,hand3,hand4]
        self.assertEqual(hanabi.ai.RecommendationStrategy.play(RS), 'c14')





if __name__ == '__main__':
    unittest.main()
