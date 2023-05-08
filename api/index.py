# api/index.py

# https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python


from http.server import BaseHTTPRequestHandler
from os.path import join


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        path = join('data', 'stuff.txt')
        self.wfile.write(path.encode())

        with open(path, 'r') as file:
            for line_text in file:
                write_text = '> ' + line_text
                self.wfile.write(write_text.encode())
