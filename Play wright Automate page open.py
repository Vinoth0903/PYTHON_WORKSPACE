from playwright.sync_api import sync_playwright
with sync_playwright() as p:
   browser = p.chromium.launch(headless=True)
   page = browser.new_page()
   page.goto("https://www.amazon.in")
   print("Page title:", page.title())
   page.screenshot(path="amazon.png")
   browser.close()
