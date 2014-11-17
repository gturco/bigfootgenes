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
        wikitext = pagehandle.getWikiText()

        return {'snp': snp, 'wikitext': wikitext}

    def snp_info(self, snp):
        """get all the data for a snp"""

        pagehandle = page.Page(self.site, snp)
        wikitext = pagehandle.getWikiText()
        wikicode = mwparserfromhell.parse(wikitext)
        templates = wikicode.filter_templates()
        infobox = templates[0]

        data = self.expand_templates(infobox)

        # TODO eval the infobox to get the summary gene info
        # format as a dictionary

        return {'snp': snp, 'infobox': infobox, 'data': data}

    def expand_templates(self, template):
        """Expand templates to get all the detail info"""

        options = {"action": "expandtemplates", "format": "json", "text": template}

        url_encoded_template = urllib.urlencode(options)
        url = self.base_url + "?" + url_encoded_template

        res = requests.get(url)
        res_json = json.loads(res.text)
        expanded_html = res_json["expandtemplates"]["*"]

        infobox_html = BeautifulSoup(expanded_html)
        # TODO get the orientation

        # TODO extract the smwtable
        wikitext_table = ""

        data = {}
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
