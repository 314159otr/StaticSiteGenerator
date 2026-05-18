import unittest
from generate_page import extract_title
class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        markdown = """
# Title
some text
"""
        result = extract_title(markdown)
        expected = "Title"
        self.assertEqual(expected, result)



