#!/usr/bin/env python3
"""Convert HTML poster to PDF using Playwright (browser-based rendering)."""
import sys
import os
from playwright.sync_api import sync_playwright

def html_to_pdf(html_path, pdf_path):
    html_path = os.path.abspath(html_path)
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        page.goto(f"file://{html_path}", wait_until="networkidle", timeout=30000)
        
        page.pdf(
            path=pdf_path,
            width="33.1in",
            height="46.8in",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}
        )
        
        browser.close()
    
    print(f"PDF saved to {pdf_path}")

if __name__ == '__main__':
    html_to_pdf(sys.argv[1], sys.argv[2])
