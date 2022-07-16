from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
from urllib.parse import urlparse
import signal

logfile = open("zetamac_log.csv", "a")

class handler(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(200)
        time = datetime.now().replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%S")

        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))

        logfile.write(f"{time},{query_components['score']}\n")
        logfile.flush()

def sigterm_handler(signo, stack_frame):
    logfile.close()

if __name__ == "__main__":

    signal.signal(signal.SIGTERM, sigterm_handler)

    with HTTPServer(('', 8015), handler) as server:
        server.serve_forever()
