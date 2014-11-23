import sys
import os
sys.path.append("./..")
import json
import unittest
from snpedia_store import SnpediaStore

class TestSnpediaStore(unittest.TestCase):

    def setUp(self):
        self.snpedia_store = SnpediaStore()

    def test_create_mysql_insert_stmt_from_snpedia_data_line(self):
        line = ""
        test_file_path = os.path.dirname(os.path.realpath(__file__)) + "/../../data/rs7412.py"

        with open(test_file_path, "r") as f:
            line = f.read()

        insert_stmt = self.snpedia_store.create_mysql_insert_stmt_from_snpedia_data_line(line)

        print insert_stmt

if __name__ == '__main__':
    unittest.main()


