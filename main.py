import socketserver
import random
from request import Request
from urllib.parse import parse_qs
from page import Page

HOST, PORT = '127.0.0.1', 1025


def generate_numbers(n):
    massive = []
    while len(massive) < n:
        random_number = random.randint(1, 10)
        if random_number not in massive:
            massive.append(random_number)
    return massive


class MyTCPHandler(socketserver.StreamRequestHandler):
    secret_nums = generate_numbers(4)

    def handle(self) -> None:
        request = Request(file=self.rfile)
        print(
            f'Method: {request.method}\n'
            f'URI: {request.uri}\n'
            f'Protocol: {request.protocol}\n'
        )

        data_person = parse_qs(request.body)

        response_body = Page(data_person, self.secret_nums).check_person()
        response_body_length = str(len(response_body.encode()))

        response = (
            'HTTP/1.1 200 OK',
            'Content-Type: text/html',
            f'Content-Length: {response_body_length}',
            'Connection: close',
            '',
            response_body
        )
        self.wfile.write('\r\n'.join(response).encode())


socketserver.TCPServer.allow_reuse_address = True

with socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) as server:
    server.serve_forever()
