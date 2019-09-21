{"filter":false,"title":"test_boggle.py","tooltip":"/test_boggle.py","undoManager":{"mark":4,"position":4,"stack":[[{"start":{"row":0,"column":0},"end":{"row":7,"column":30},"action":"insert","lines":["","import unittest","","","class test_boggle(unittest.TestCase):","","    def test_is_this_thing_on(self):","        self.assertEqual(1, 1)"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":6,"column":30},"action":"remove","lines":["import unittest","","","class test_boggle(unittest.TestCase):","","    def test_is_this_thing_on(self):","        self.assertEqual(1, 1)"],"id":5},{"start":{"row":0,"column":0},"end":{"row":31,"column":38},"action":"insert","lines":["  ","import unittest","import boggle","","","class TestBoggle(unittest.TestCase):","    \"\"\"","    Our test suite for boggle solver","    \"\"\"","","    def test_can_create_an_empty_grid(self):","        \"\"\"","        Test to see if we can create an empty grid","        \"\"\"","        grid = boggle.make_grid(0, 0)","        self.assertEqual(len(grid), 0)","    ","    def test_grid_size_width_times_height(self):","        \"\"\"","        Test is to ensure that the total size of the grid","        is equal to width * height","        \"\"\"","        grid = boggle.make_grid(2, 3)","        self.assertEqual(len(grid), 6)","    ","    def test_grid_coordinates(self):","        grid = boggle.make_grid(2, 2)","        self.assertIn((0, 0), grid)","        self.assertIn((0, 1), grid)","        self.assertIn((1, 0), grid)","        self.assertIn((1, 1), grid)","        self.assertNotIn((2, 2), grid)"]}],[{"start":{"row":0,"column":2},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":6},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":[" "]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":[" "],"id":7}]]},"ace":{"folds":[],"scrolltop":180,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":11,"state":"qqstring3","mode":"ace/mode/python"}},"timestamp":1569058687543,"hash":"f59b90cf383e4fee22f38e302c01c2abb9701941"}