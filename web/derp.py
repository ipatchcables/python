import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('0.0.0.0', 443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='/opt/web/fullchain.pem', keyfile='/opt/web/privkey.pem', server_side=True, ssl_version=ssl.PROTOCOL_TLSv1_2)
httpd.serve_forever()
