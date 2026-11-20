"""Inspect the actual public HTML; no Stripe calls or extra dependencies."""
from html.parser import HTMLParser
from pathlib import Path
import unittest
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SAMPLE_CONTACT = "mailto:f1intt3ch@gmail.com?subject=Metro%20Permit%20Leads%20sample%20and%20delivery"


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.checkout_links = []
        self.inquiries = []

    def handle_starttag(self, tag, attrs):
        href = dict(attrs).get("href", "")
        if tag != "a":
            return
        url = urlsplit(href)
        if (url.hostname in {"buy.stripe.com", "checkout.stripe.com"}
                or (url.hostname == "midas-api-sand.vercel.app" and url.path.rstrip("/") == "/buy")):
            self.checkout_links.append(href)
        if href.startswith("mailto:"):
            self.inquiries.append(href)


class MetroCheckoutTests(unittest.TestCase):
    def test_public_pages_offer_no_direct_checkout(self):
        for path in ROOT.rglob("*.html"):
            with self.subTest(page=path.name):
                page = Links()
                page.feed(path.read_text())
                self.assertEqual(page.checkout_links, [])

    def test_new_sales_scope_has_no_unverified_city_or_exclusive_seat(self):
        for name in ["index.html", "product.html"]:
            html = (ROOT / name).read_text()
            self.assertNotRegex(html, r"St\. Paul|Saint Paul|One seat per trade per city|one seat per trade per city")
            self.assertIn("Minneapolis", html)
            self.assertIn("confirm your trade and delivery schedule", html)
            page = Links()
            page.feed(html)
            self.assertIn(SAMPLE_CONTACT, page.inquiries, name)

    def test_press_copy_and_product_route_match_the_current_offer(self):
        press = (ROOT / "press.html").read_text()
        self.assertNotIn("Saint Paul", press)
        self.assertIn('href="product.html">Metro product and sample inquiry', press)
        self.assertNotIn("is 402 until", (ROOT / "product.html").read_text())

    def test_operator_readme_agrees_with_checkout_account(self):
        readme = (ROOT / "README.md").read_text()
        self.assertNotIn("buy.stripe.com", readme)
        self.assertIn("plink_1UHSKmEYm87XGaC5IVhIkF5B", readme)
        self.assertIn("acct_1TaUSsEYm87XGaC5", readme)
        self.assertNotIn("6oU5kF62efuW1GP41U7Zu18", readme)


if __name__ == "__main__":
    unittest.main()
