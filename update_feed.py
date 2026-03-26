import urllib.request
import shutil
import os

FEED_URL = "https://giuliomagnifico.github.io/raiplay-feed/feed_ilruggitodelconiglio.xml"
OUTPUT_FILE = "feed_ilruggitodelconiglio.xml"

headers = {
    "User-Agent": "Mozilla/5.0 (Android 14; Mobile) AppleWebKit/537.36"
}

req = urllib.request.Request(FEED_URL, headers=headers)
with urllib.request.urlopen(req) as response:
    with open(OUTPUT_FILE, "wb") as f:
        f.write(response.read())

print(f"Feed aggiornato: {OUTPUT_FILE}")
