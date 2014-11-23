import json
import mysql.connector

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

        cursor = self.cnx.cursor()
        cursor.execute(query, (rsid, genotype))

        for (rsid, genotype, summary) in cursor:
            record = {'rsid': rsid, 'genotype': genotype, 'summary': summary}
            yield record

        cursor.close()

    def import_data(self, snp_data_file):
        """snp_data_file is created from \
        SnpediaFetcher.write_snp_wikitext_to_file"""

        with open(snp_data_file, 'r') as file:
            for line in file:
                mysql_insert_stmt = self.create_mysql_insert_stmt_from_snpedia_data_line(line)
                print mysql_insert_stmt


    def create_mysql_insert_stmt_from_snpedia_data_line(self, line):
        """docstring for create_mysql_insert_stmt_from_snpedia"""

        # TODO when we switch the data format to real json, use json.loads instead of eval
        # snp_data = json.loads(line)
        snp_data = eval(line)

        snp = snp_data['snp']
        wikitext = snp_data['wikitext']

        record = self.snpedia.snp_info_from_wikitext(snp, wikitext)

        mysql_stmt = "";
        for geno in record['geno_records']:
            if len(geno) > 0:
                stmt = "INSERT INTO snps(rsid,genotype,summary) VALUES(\"{0}\",\"{1}\",\"{2}\");".format(snp, geno['Geno'], geno['Summary'])
                mysql_stmt += stmt;

        return mysql_stmt
