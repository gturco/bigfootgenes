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
        test_file_path = os.path.dirname(os.path.realpath(__file__)) + "/../../data/rs7412.py"

        line = ""
        with open(test_file_path, "r") as f:
            line = f.read()

        insert_stmt = self.snpedia_store.create_mysql_insert_stmt_from_snpedia_data_line(line)
        expected = """INSERT INTO snps(rsid,genotype,summary) VALUES("rs7412","CC","more likely to gain weight if taking olanzapine");INSERT INTO snps(rsid,genotype,summary) VALUES("rs7412","CT","more likely to gain weight if taking olanzapine");INSERT INTO snps(rsid,genotype,summary) VALUES("rs7412","TT","normal");"""
        self.assertEqual(expected,insert_stmt)

    def test_query(self):
        """docstring for test_queyr"""
        rsid = "rs7412"
        genotype = "CC"

        for result in self.snpedia_store.query(rsid, genotype):
            self.assertEqual(result['genotype'], 'CC')

if __name__ == '__main__':
    unittest.main()
