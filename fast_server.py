import http.server
import socketserver

# This allows the server to handle multiple image requests at once
class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

if __name__ == "__main__":
    # We use 127.0.0.1 to prevent the '502 Bad Gateway' error
    server_address = ('127.0.0.1', 8080)
    handler = http.server.SimpleHTTPRequestHandler
    httpd = ThreadedHTTPServer(server_address, handler)
    print("🚀 North East Yatra Server is LIVE at http://127.0.0.1:8080")
    httpd.serve_forever()