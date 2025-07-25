import unittest
from pathlib import Path

from hsc.scrapers.works_page import AllWorksPage

WORKS_PAGE = Path(__file__).parent.joinpath("html").joinpath("works.html")


class WorksPageTest(unittest.TestCase):
    def setUp(self):
        with open(WORKS_PAGE) as f:
            self.html_bytes = f.read()

    def test(self):
        wp = AllWorksPage(html=self.html_bytes)
        for i in wp.get_works():
            self.assertGreaterEqual(i.id, 1)
            self.assertIsNotNone(i.title)


if __name__ == "__main__":
    unittest.main()
