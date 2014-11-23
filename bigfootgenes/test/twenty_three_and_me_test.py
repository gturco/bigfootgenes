import sys
import os
sys.path.append("./..")
import json
import unittest
from twenty_three_and_me import TwentyThreeAndMe

class TestTwentyThreeAndMe(unittest.TestCase):

    def setUp(self):
        self.snpedia = Snpedia()


    def test_get_snp_matches(self):
        """get matches"""

        data = TwentyThreeAndMe.parse_23andme_file()
        matches = TwentyThreeAndMe.get_snp_matches(data)
        for match in matches:
            print matches

