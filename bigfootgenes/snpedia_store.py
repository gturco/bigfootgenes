import json
import mysql.connector
import logging

from contextlib import closing
from mysql.connector import errorcode
from snpedia import Snpedia

class SnpediaStore:
    def __init__(self):
        self.snpedia = Snpedia()

        self.config = {
          'user': 'bigfootgenes',
          'password': 'dk34DFko99FDOQ',
          'host': '127.0.0.1',
          'database': 'bigfootgenes_development',
          'raise_on_warnings': True
        }

        # get the mysql cursor
        self.cnx = mysql.connector.connect(**self.config)

    def query(self, rsid, genotype):
        """Query snps given a rsid and genotype"""
        query = ("SELECT rsid, genotype, summary FROM snps "
                 "WHERE rsid = %s AND genotype = %s")

        with closing(self.cnx.cursor()) as cur:
            cur.execute(query, (rsid, genotype))
            for (rsid, genotype, summary) in cursor:
                record = {'rsid': rsid, 'genotype': genotype, 'summary': summary}
                yield record

    def import_snps(self, snp_data_file):
        """snp_data_file is created from write_snp_wikitext_to_file.py"""

        with open(snp_data_file, 'r') as input_file:
            for line in input_file:
                try:
                    self.insert_snp(line)
                except Exception as detail:
                    logging.error("Error inserting: {0}\n".format(line))
                    logging.error(detail)

    def insert_snp(self, line):
        """line is created from write_snp_wikitext.py"""

        # TODO when we switch the data format to real json, use json.loads instead of eval
        # snp_data = json.loads(line)
        snp_data = eval(line)

        snp = snp_data['snp']
        wikitext = snp_data['wikitext']

        record = self.snpedia.snp_info_from_wikitext(snp, wikitext)

        if not record.has_key('geno_records'):
            return False

        for geno in record['geno_records']:
            if len(geno) == 0: continue

            stmt = u"""INSERT INTO snps(rsid,genotype,summary) VALUES(%s, %s, %s);"""
            with closing(self.cnx.cursor()) as cur:
                logging.info("Inserting {0}".format(snp))
                cur.execute(stmt, (snp, geno['Geno'], geno['Summary']))

        self.cnx.commit()

        return True
