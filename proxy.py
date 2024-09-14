import http.server
import socketserver

class Proxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Simple proxy that forwards the request to the target URL
        import urllib.request
        url = 'https://www.example.com' + self.path
        req = urllib.request.Request(url)
        try:
            with urllib.request.urlopen(req) as response:
                self.send_response(response.status)
                self.send_header('Content-type', response.headers.get('Content-Type', 'text/html'))
                self.end_headers()
                self.wfile.write(response.read())
        except Exception as e:
            self.send_error(500, str(e))

PORT = 8000
with socketserver.TCPServer(("", PORT), Proxy) as httpd:
    print(f"Serving HTTP on port {PORT}")
    httpd.serve_forever()
