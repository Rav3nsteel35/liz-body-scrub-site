"""Run the Liz Body Scrub site locally and open it in your browser.

Usage:
    python tools/serve_site.py

Stop it with Ctrl+C in the terminal it's running in.
"""

import http.server
import os
import socketserver
import sys
import webbrowser

PORT = 8000
SITE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "site")


def main():
    os.chdir(SITE_DIR)
    handler = http.server.SimpleHTTPRequestHandler

    try:
        httpd = socketserver.TCPServer(("", PORT), handler)
    except OSError:
        print(f"Port {PORT} is already in use — the site may already be running at:")
        print(f"  http://localhost:{PORT}")
        sys.exit(0)

    url = f"http://localhost:{PORT}"
    print(f"Serving {SITE_DIR}")
    print(f"Open the site at: {url}")
    print("Press Ctrl+C to stop.")

    webbrowser.open(url)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        httpd.server_close()


if __name__ == "__main__":
    main()
