from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

from hello import greet


class GreetingHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code: int = 200, content_type: str = "application/json") -> None:
        self.send_response(status_code)
        self.send_header("Content-Type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_OPTIONS(self) -> None:
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self) -> None:
        if self.path == "/greeting":
            self._set_headers()
            payload = {"greeting": greet()}
            self.wfile.write(json.dumps(payload).encode("utf-8"))
            return

        self._set_headers(404)
        payload = {"error": "Not found"}
        self.wfile.write(json.dumps(payload).encode("utf-8"))


def run_server() -> None:
    port = int(os.environ.get("PORT", "8000"))
    server = HTTPServer(("127.0.0.1", port), GreetingHandler)
    print(f"Server running at http://127.0.0.1:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
