# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class TestGildedRose(unittest.TestCase):
    
    def test_aged_brie_quality_increase(self):
        items = [Item("Aged Brie", 5, 10)]  # Aged Brie with sell_in 5 and quality 10
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 11)
        self.assertEqual('foo', items[0].sell_in, 4)
        
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 12)
        self.assertEqual(items[0].sell_in, 3)
    
    def test_backstage_passes_quality_increase(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]  # Backstage passes with sell_in 15 and quality 20
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21)
        self.assertEqual(items[0].sell_in, 14)
        
        # Increase quality by 2 when sell_in <= 10
        items[0].sell_in = 10
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 23)
        
        # Increase quality by 3 when sell_in <= 5
        items[0].sell_in = 5
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 26)
        
        # Quality drops to 0 after the concert
        items[0].sell_in = 0
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)
    
    def test_sulfuras_quality_and_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]  # Sulfuras with sell_in 0 and quality 80
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 80)  # Quality should remain unchanged
        self.assertEqual(items[0].sell_in, 0)   # Sell_in should remain unchanged
    
    def test_regular_item_quality_decrease(self):
        items = [Item("Elixir of the Mongoose", 7, 5)]  # Regular item with sell_in 7 and quality 5
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 4)
        self.assertEqual(items[0].sell_in, 6)
        
        # Quality decreases by 2 when sell_in <= 0
        items[0].sell_in = 0
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 2)
    
    def test_regular_item_quality_limits(self):
        items = [Item("Elixir of the Mongoose", 5, 0)]  # Regular item with sell_in 5 and quality 0
        gilded_rose = GildedRose(items)
        
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)  # Quality should not go below 0
        
        # Quality should not exceed 50
        items[0].quality = 50
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

if __name__ == '__main__':
    unittest.main()
