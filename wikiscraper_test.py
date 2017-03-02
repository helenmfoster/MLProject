import unittest
from wikiscraper import Wikiscraper

class TestWikiscraper(unittest.TestCase):
  ws = Wikiscraper()

  def test_scrape_article(self):
    test_subject = "Albert Einstein"
    wikipage = self.ws.scrape_article(test_subject)
    
    self.assertEqual(wikipage.subject, "Albert Einstein")
    self.assertEqual(str(wikipage.soup.title), "<title>Albert Einstein - Wikipedia</title>")

if __name__ == '__main__':
    unittest.main()


