import http.server
import sys

PORT = 8000


def create_handler(ppk: str):
    class MyHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            html_content = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                  <meta charset="UTF-8">
                  <title>Tidio Test Chat</title>
                </head>
                <body>
                  <h1>Welcome to Tidio Chat Page</h1>
                
                  <!-- Paste your Tidio snippet below -->
                  <script src="//code.tidio.co/{ppk}.js" async></script>
                </body>
                </html>
            """

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))
    return MyHandler


def start_server(pkk: str) -> None:
    """
    Start HTTP server

    :param pkk: Tidio Public Key
    :return: None
    """
    print(f"Starting HTTP server at http://localhost:{PORT}")
    try:
        handler = create_handler(pkk)
        with http.server.HTTPServer(("", PORT), handler) as http_server:
            http_server.serve_forever()
    except Exception as exc:
        print(f"Failed to run HTTP server: {str(exc)}")
        sys.exit(1)
