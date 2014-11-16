from wikitools import wiki, page, category
from wikitools import wiki
from wikitools import category

from bs4 import BeautifulSoup

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

        return {infobox: infobox}

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

        data = {}

        # TODO fix parsing the infobox
        rows = infobox_html.find_all("tr")
        print rows
        for row in rows:
            cols = row.find_all("td")

            if len(cols) == 2:
                key = cols[0].get_text()
                value = cols[1].get_text()
                data[key] = value

        return data
