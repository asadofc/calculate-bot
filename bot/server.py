from http.server import BaseHTTPRequestHandler, HTTPServer
from bot.config import PORT
from bot.utils.logger import logger

class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        logger.info(f"🌐 GET request from {self.client_address}")
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Calculator Bot is alive!")

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        pass  # suppress default logging

def start_server():
    try:
        server = HTTPServer(("0.0.0.0", PORT), DummyHandler)
        logger.info(f"✅ HTTP health server on port {PORT}")
        server.serve_forever()
    except Exception as e:
        logger.error(f"❌ Server error: {e}")
