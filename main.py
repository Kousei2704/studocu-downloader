import argparse
import time
import sys
from playwright.sync_api import sync_playwright, Error as PlaywrightError

def remove_paywall_and_blur(page):
    try:
        page.evaluate('''() => {
            const paywalls = document.querySelectorAll('[data-test-selector="document-viewer-paywall"], .modal-overlay, .paywall');
            paywalls.forEach(el => el.remove());
            const blurredElements = document.querySelectorAll('[style*="filter: blur"], .blurred-container, .page-content');
            blurredElements.forEach(el => { el.style.filter = 'none'; el.style.userSelect = 'auto'; });
            document.body.style.overflow = 'auto';
        }''')
    except Exception:
        pass

def scroll_to_load_pages(page):
    try:
        last_height = page.evaluate("document.body.scrollHeight")
        while True:
            page.evaluate("window.scrollBy(0, 800);")
            time.sleep(1.5)
            remove_paywall_and_blur(page)
            new_height = page.evaluate("document.documentElement.scrollTop + window.innerHeight")
            if new_height >= last_height:
                break
            last_height = page.evaluate("document.body.scrollHeight")
    except Exception:
        pass

def download_pdf(url, output, headless, browser_choice):
    try:
        with sync_playwright() as p:
            if browser_choice == 'firefox':
                browser = p.firefox.launch(headless=headless)
            elif browser_choice == 'webkit':
                browser = p.webkit.launch(headless=headless)
            elif browser_choice == 'edge':
                browser = p.chromium.launch(channel="msedge", headless=headless)
            elif browser_choice == 'chrome':
                browser = p.chromium.launch(channel="chrome", headless=headless)
            else:
                browser = p.chromium.launch(headless=headless)
            
            context = browser.new_context(viewport={'width': 1200, 'height': 1080})
            page = context.new_page()
            
            print(f"[*] Accessing via {browser_choice.upper()}: {url}")
            page.goto(url, wait_until="networkidle", timeout=60000)
            time.sleep(3)

            print("[*] Bypassing paywall and lazy-loading pages...")
            remove_paywall_and_blur(page)
            scroll_to_load_pages(page)
            
            print(f"[*] Exporting to: {output}")
            page.pdf(path=output, format="A4", print_background=True)
            print("[+] Done!")
            browser.close()
    except PlaywrightError as pe:
        print(f"[-] Playwright Error: {pe}")
        sys.exit(1)
    except Exception as e:
        print(f"[-] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="StuDocu PDF Downloader")
    parser.add_argument("url", help="StuDocu Document URL")
    parser.add_argument("-o", "--output", default="document.pdf", help="Output PDF filename")
    parser.add_argument("--show", action="store_true", help="Run browser in headful mode")
    parser.add_argument("--browser", choices=['chromium', 'firefox', 'webkit', 'edge', 'chrome'], default='chromium', help="Browser engine selection")
    
    args = parser.parse_args()
    download_pdf(args.url, args.output, headless=not args.show, browser_choice=args.browser)