from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import webbrowser

root = Path(__file__).resolve().parent
handler = partial(SimpleHTTPRequestHandler, directory=str(root))
try:
    with ThreadingHTTPServer(("127.0.0.1", 8060), handler) as server:
        url = "http://127.0.0.1:8060/Build.html"
        print("Unge Shogi preview: " + url, flush=True)
        print("Keep this window open. Press Ctrl+C to stop.", flush=True)
        webbrowser.open(url)
        server.serve_forever()
except KeyboardInterrupt:
    print("Preview stopped.")
except OSError as error:
    print("Cannot start preview:", error)
    raise SystemExit(1)
