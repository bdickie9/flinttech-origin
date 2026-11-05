"""Inspect the actual public HTML; no Stripe calls or extra dependencies."""
from html.parser import HTMLParser
from pathlib import Path
import unittest
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = "https://buy.stripe.com/5kQ6oH1qR94M7aZeyBeZ212"


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stripe = []
        self.inquiries = []

    def handle_starttag(self, tag, attrs):
        href = dict(attrs).get("href", "")
        if tag == "a" and urlsplit(href).hostname == "buy.stripe.com":
            self.stripe.append(href)
        if tag == "a" and href.startswith("mailto:"):
            self.inquiries.append(href)


class MetroCheckoutTests(unittest.TestCase):
    def test_all_public_stripe_anchors_use_the_approved_destination(self):
        counts = {}
        for path in ROOT.glob("*.html"):
            page = Links()
            page.feed(path.read_text())
            for href in page.stripe:
                self.assertEqual(href, CANONICAL, str(path))
            if page.stripe:
                counts[path.name] = len(page.stripe)
        self.assertEqual(counts, {"index.html": 2, "product.html": 1})

    def test_new_sales_scope_has_no_unverified_city_or_exclusive_seat(self):
        for name in ["index.html", "product.html"]:
            html = (ROOT / name).read_text()
            self.assertNotRegex(html, r"St\. Paul|Saint Paul|One seat per trade per city|one seat per trade per city")
            self.assertIn("Minneapolis", html)
            self.assertIn("confirm your trade and delivery schedule", html)
            page = Links()
            page.feed(html)
            self.assertTrue(page.inquiries, name)

    def test_operator_readme_agrees_with_checkout_account(self):
        readme = (ROOT / "README.md").read_text()
        self.assertIn(CANONICAL, readme)
        self.assertIn("acct_1TaUSsEYm87XGaC5", readme)
        self.assertNotIn("6oU5kF62efuW1GP41U7Zu18", readme)


if __name__ == "__main__":
    unittest.main()
