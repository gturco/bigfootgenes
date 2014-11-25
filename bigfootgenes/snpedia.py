from wikitools import wiki, page, category
from wikitools import wiki
from wikitools import category

from bs4 import BeautifulSoup

from mwlib import dummydb, parser, expander, uparser
from mwlib.expander import DictDB

import re
import itertools
import mwparserfromhell
import urllib
import requests
import json

class Snpedia:
    def __init__(self):
        self.base_url = "http://bots.snpedia.com/api.php"
        self.site = wiki.Wiki(self.base_url)

    def get_snps(self):
        """generator which returns snps from snpedia"""
        snps = category.Category(self.site, "Is_a_snp")
        for article in snps.getAllMembersGen(namespaces=[0]):   # get all snp-names as list and print them
            yield article.title.lower()

    def get_wikitext(self, snp):
        """get the wikitext for a snp"""
        pagehandle = page.Page(self.site, snp)

        try:
            wikitext = pagehandle.getWikiText()
            return {'snp': snp, 'wikitext': wikitext}
        except page.NoPage:
            return {'snp': snp, 'wikitext': ""}

    def snp_info(self, snp):
        """get all the data for a snp"""

        pagehandle = page.Page(self.site, snp)
        wikitext = pagehandle.getWikiText()

        return snp_info_from_wikitext(snp, wikitext)

    def snp_info_from_wikitext(self, snp, wikitext):
        """get all the data for a snp"""

        wikicode = mwparserfromhell.parse(wikitext)
        templates = wikicode.filter_templates()

        data = {}
        if len(templates) > 0:
            infobox = templates[0]
            data = self.expand_infobox(infobox)

        record = {'snp': snp}

        return dict(record.items() + data.items())

    def expand_infobox(self, template):
        """Expand infobox to get all the detail info"""

        options = {"action": "expandtemplates", "format": "json", "text": template.encode('utf-8')}

        url_encoded_template = urllib.urlencode(options)
        url = self.base_url + "?" + url_encoded_template

        res = requests.get(url)
        res_json = json.loads(res.text)
        expanded_html = res_json["expandtemplates"]["*"]

        # get orientation
        orientation_pattern = re.compile('\[\[Orientation::([a-z]+)\]\]')
        orientation_matches = orientation_pattern.search(expanded_html)
        if orientation_matches and orientation_matches.groups():
            orientation = orientation_matches.groups()[0]
        else:
            orientation = None

        # extract the smwtable
        smwtable_pattern = re.compile('\[\[SMW::off\]\](.*)\[\[SMW::on\]\]', re.DOTALL)
        smwtable_matches = smwtable_pattern.search(expanded_html)

        wikitext_table = ""
        if smwtable_matches and smwtable_matches.groups():
            wikitext_table = smwtable_matches.groups()[0]

        data = {}
        if orientation:
            data['orientation'] = orientation
        data['geno_records'] = self.parse_smwtable_wikitext(wikitext_table)
        data['geno_records'] = [self.normalize_geno_record(x, orientation) for x in data['geno_records']]

        return data

    def normalize_geno_record(self, record, orientation):
        """remove extra characters"""

        if record.has_key("Geno"):
            record["Geno"] = record["Geno"].replace("(", "").replace(";", "").replace(")", "")

            if orientation == "minus":
                record["Geno"] = self.reverse_complement(record["Geno"])

        return record

    def reverse_complement(self, genotype):
        """apply a reverse comp. to the genotype, see http://www.snpedia.com/index.php/Orientation"""

        reverse_map = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}

        reversed = ""
        for c in genotype:
            reversed += reverse_map[c]

        # QUESTION: do i need to flip the reversed after applying the reverse_map?

        return reversed

    def parse_smwtable_wikitext(self, wikitext):
        """wikitext must just be the smwtable format. returns back an array of records"""

        parsed = uparser.simpleparse(wikitext)

        results = parsed.find(parser.Table)
        if len(results) == 0:
            return []

        table = results[0]

        keys = []
        for col in table.children[0].children:
            keys.append(col.asText().strip())

        records = []
        for row in itertools.islice(table.children, 1, None):
            data = []
            # 3 cols in each row
            for col in row.children:
                data.append(col.asText().strip())

            zipped = zip(keys, data)
            data_dict = dict(zipped)
            records.append(data_dict)

        return records
