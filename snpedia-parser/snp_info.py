from wikitools import wiki, page, category

import mwparserfromhell

snp = "rs7412"

def snp_info(snp):
    """docstring for snp_info"""
    site = wiki.Wiki("http://bots.snpedia.com/api.php")
    pagehandle = page.Page(site, snp)
    wikitext = pagehandle.getWikiText()
    wikicode = mwparserfromhell.parse(wikitext)
    templates = wikicode.filter_templates()
    infobox = templates[0]

