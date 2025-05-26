"""
Test file to verify the HTML file contains the expected content
"""
import unittest
import os
from pathlib import Path


class TestIndexHTML(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.html_file = Path(__file__).parent.parent / "index.html"
    
    def test_html_file_exists(self):
        """Test that the HTML file exists"""
        self.assertTrue(self.html_file.exists(), "index.html file should exist")
    
    def test_html_contains_expected_text(self):
        """Test that the HTML file contains 'hello world'"""
        with open(self.html_file, 'r', encoding='utf-8') as f:
            content = f.read().lower()
        
        self.assertIn("hello world", content, 
                     f"HTML file should contain 'hello world'")
    
    def test_html_is_valid_structure(self):
        """Test that the HTML has basic valid structure"""
        with open(self.html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for basic HTML structure
        self.assertIn("<!DOCTYPE html>", content, "Should have DOCTYPE declaration")
        self.assertIn("<html", content, "Should have html tag")
        self.assertIn("<head>", content, "Should have head section")
        self.assertIn("<body>", content, "Should have body section")
        self.assertIn("</html>", content, "Should close html tag")


if __name__ == '__main__':
    unittest.main()
