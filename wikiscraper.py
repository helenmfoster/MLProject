import urllib
import urllib2
from wikipage import Wikipage
from bs4 import BeautifulSoup

class Wikiscraper:
  """Wikipedia scraper"""

  def __init__(self):
    self.opener = urllib2.build_opener()
    self.opener.addheaders = [('User-agent', 'Mozilla/5.0')] #wikipedia needs this
    
  def scrape_article(self, subject):
    """ Returns a Wikipage object about given subject"""
    url = self._build_url(subject)
    article_soup = self._build_soup(url)
    return Wikipage(subject, article_soup)

  def _build_url(self, subject):
    """Builds wikipedia url for given subject"""
    article = urllib.quote(subject)
    return "http://en.wikipedia.org/wiki/" + article

  def _build_soup(self, url):
    """Returns beautiful soup object for given url"""
    resource = self.opener.open(url)
    data = resource.read()
    resource.close()

    return BeautifulSoup(data)
