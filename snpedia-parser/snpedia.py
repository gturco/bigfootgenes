from wikitools import wiki, page, category
from wikitools import wiki
from wikitools import category

from bs4 import BeautifulSoup

from mwlib import dummydb, parser, expander, uparser
from mwlib.expander import DictDB

import itertools
import mwparserfromhell
import urllib
import requests
import json

class Snpedia:
    def get_snps(self):
        """generator which returns snps from snpedia"""
        site = wiki.Wiki("http://bots.snpedia.com/api.php")                  # open snpedia
        snps = category.Category(site, "Is_a_snp")
        for article in snps.getAllMembersGen(namespaces=[0]):   # get all snp-names as list and print them
            yield article.title.lower()

    def snp_info(self, snp):
        """docstring for snp_info"""
        site = wiki.Wiki("http://bots.snpedia.com/api.php")
        pagehandle = page.Page(site, snp)
        wikitext = pagehandle.getWikiText()
        wikicode = mwparserfromhell.parse(wikitext)
        templates = wikicode.filter_templates()
        infobox = templates[0]

        # TODO eval the infobox to get the summary gene info
        # format as a dictionary

        return {snp: snp, infobox: infobox}

    def expand_templates(self, template):
        """Expand templates to get all the detail info"""

        options = {"action": "expandtemplates", "format": "json", "text": template}

        url_encoded_template = urllib.urlencode(options)
        base_url = "http://bots.snpedia.com/api.php"
        url = base_url + "?" + url_encoded_template

        res = requests.get(url)
        res_json = json.loads(res.text)
        expanded_html = res_json["expandtemplates"]["*"]

        infobox_html = BeautifulSoup(expanded_html)
        wikitext_table = ""

        data = {}

        # TODO extract the smwtable
        data['geno_records'] = self.parse_smwtable_wikitext(wikitext_table)

        return data

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
