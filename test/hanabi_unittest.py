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
    	game = hanabi.Game(5)
        ai=hanabi.ai.RecommendationStrategy(game)
        c1 = hanabi.deck.Card(hanabi.deck.Color.Blue,5)
        c2 = hanabi.deck.Card(hanabi.deck.Color.Red,2)
        c3 = hanabi.deck.Card(hanabi.deck.Color.Green,4)
        c4 = hanabi.deck.Card(hanabi.deck.Color.Blue,2)
        hand=hanabi.deck.Hand([c1,c2,c3,c4])   
        game.piles[hanabi.deck.Color.Blue]=4
        game.piles[hanabi.deck.Color.Red]=1
        game.piles[hanabi.deck.Color.Green]=3
        game.piles[hanabi.deck.Color.Yellow]=1
        self.assertEqual(hanabi.ai.RecommendationStrategy.deduce_number(ai,hand), 0)


    def test_deduce_number_2(self):
        game = hanabi.Game(5)
        ai=hanabi.ai.RecommendationStrategy(game)
        c1 = hanabi.deck.Card(hanabi.deck.Color.Blue,1)
        c2 = hanabi.deck.Card(hanabi.deck.Color.Red,1)
        c3 = hanabi.deck.Card(hanabi.deck.Color.Green,1)
        c4 = hanabi.deck.Card(hanabi.deck.Color.Yellow,1)
        hand=hanabi.deck.Hand([c1,c2,c3,c4])   
        game.piles[hanabi.deck.Color.Blue]=2
        game.piles[hanabi.deck.Color.Red]=2
        game.piles[hanabi.deck.Color.Green]=2
        game.piles[hanabi.deck.Color.Yellow]=2
        self.assertEqual(hanabi.ai.RecommendationStrategy.deduce_number(ai,hand), 5)

    def test_give_a_hint(self):
        game = hanabi.Game(5)
        ai=hanabi.ai.RecommendationStrategy(game)
        c1 = hanabi.deck.Card(hanabi.deck.Color.Blue,5)
        c2 = hanabi.deck.Card(hanabi.deck.Color.Red,1)
        c3 = hanabi.deck.Card(hanabi.deck.Color.Green,1)
        c4 = hanabi.deck.Card(hanabi.deck.Color.Yellow,1)
        c5 = hanabi.deck.Card(hanabi.deck.Color.Red,5)
        c6 = hanabi.deck.Card(hanabi.deck.Color.Green,5)
        c7 = hanabi.deck.Card(hanabi.deck.Color.Yellow,5)
        hand1=hanabi.deck.Hand([c1,c2,c3,c4]) 
        hand2=hanabi.deck.Hand([c5,c2,c3,c4]) 
        hand3=hanabi.deck.Hand([c6,c2,c3,c4])
        hand4=hanabi.deck.Hand([c2,c7,c3,c4])
        game.other_hands=[hand1,hand2,hand3,hand4]
        self.assertEqual(hanabi.ai.RecommendationStrategy.give_a_hint(ai), 1)





if __name__ == '__main__':
    unittest.main()
