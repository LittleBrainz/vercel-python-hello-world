# api/index.py

# https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python


from http.server import BaseHTTPRequestHandler
from os.path import dirname, abspath, join


path = join(dirname(abspath(__file__)), '..' 'data', 'stuff.txt')


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write((path + '\n\n').encode())

        with open(path, 'r') as file:
            for line in file:
                self.wfile.write(('> ' + line).encode())
