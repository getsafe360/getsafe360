"""
seo.py
GetSafe AI-Agent Optimization Suite
Handles SEO analysis for website optimization.
"""

import requests
from bs4 import BeautifulSoup
from typing import Dict, Any, List, Optional

class SEOAnalyzer:
    """
    SEOAnalyzer performs basic SEO checks on a given URL.
    Extend this class with additional methods as needed.
    (canonical tags, robots.txt, sitemap.xml, image alt texts, etc.)
    """

    def __init__(self, url: str):
        self.url = url
        self.page_content = None
        self.soup = None

    def fetch_page(self) -> bool:
        """Fetch the page content."""
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            self.page_content = response.text
            self.soup = BeautifulSoup(self.page_content, 'html.parser')
            return True
        except Exception as e:
            print(f"[ERROR] Could not fetch page: {e}")
            return False

    def check_title(self) -> Dict[str, Any]:
        """Check for presence and quality of <title> tag."""
        title = self.soup.title.string.strip() if self.soup.title else None
        if title:
            return {
                "present": True,
                "text": title,
                "length": len(title),
                "issue": None if 10 <= len(title) <= 70 else "Title length suboptimal"
            }
        else:
            return {
                "present": False,
                "text": None,
                "length": 0,
                "issue": "No <title> tag found"
            }

    def check_meta_description(self) -> Dict[str, Any]:
        """Check for presence and quality of meta description."""
        desc_tag = self.soup.find('meta', attrs={'name': 'description'})
        desc = desc_tag['content'].strip() if desc_tag and desc_tag.get('content') else None
        if desc:
            return {
                "present": True,
                "text": desc,
                "length": len(desc),
                "issue": None if 50 <= len(desc) <= 160 else "Meta description length suboptimal"
            }
        else:
            return {
                "present": False,
                "text": None,
                "length": 0,
                "issue": "No meta description found"
            }

    def check_h1(self) -> Dict[str, Any]:
        """Check for the presence and quality of the first H1 tag."""
        h1 = self.soup.find('h1')
        h1_text = h1.text.strip() if h1 else None
        return {
            "present": bool(h1),
            "text": h1_text,
            "issue": None if h1_text else "No H1 tag found"
        }

    def run_all_checks(self) -> Dict[str, Any]:
        """Run all SEO checks and return a report dictionary."""
        if not self.page_content:
            if not self.fetch_page():
                return {"error": "Page could not be fetched"}

        return {
            "title": self.check_title(),
            "meta_description": self.check_meta_description(),
            "h1": self.check_h1()
        }

