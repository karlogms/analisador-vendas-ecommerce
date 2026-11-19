
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class MeuServidor(SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.path = "/paginas/index.html"

        return SimpleHTTPRequestHandler.do_GET(self)


os.chdir(os.path.dirname(os.path.abspath(__file__)))

servidor = HTTPServer(("localhost", 8000), MeuServidor)

print("Servidor iniciado!")
print("Acesse: http://localhost:8000")

servidor.serve_forever()
