import unittest
from seismology_randomizer import docs_conf

class TestDocsConf(unittest.TestCase):

    def test_project(self):
        self.assertEqual(docs_conf.project, "Seismology Monte Carlo Engine")

    def test_copyright(self):
        self.assertEqual(docs_conf.copyright, "2023, Your Name")

    def test_version(self):
        self.assertEqual(docs_conf.version, "1.0")
        self.assertEqual(docs_conf.release, "1.0")

    def test_language(self):
        self.assertIsNone(docs_conf.language)

    def test_html_static_path(self):
        self.assertEqual(docs_conf.html_static_path, ["_static"])

    def test_htmlhelp_basename(self):
        self.assertEqual(docs_conf.htmlhelp_basename, "SeismologyMonteCarloEnginedoc")

if __name__ == '__main__':
    unittest.main()
