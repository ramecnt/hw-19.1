from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from urllib.parse import parse_qs, urlparse

#  First, let's specify the run settings
hostName = "localhost"  # Network access address
serverPort = 8020  # Port for network access


class MyServer(BaseHTTPRequestHandler):
    """
        A special class responsible for
        processing incoming requests from clients
    """

    def __get_html_content(self):
        with open("page.html", "r") as f:
            return f.read()

    def do_GET(self):
        """ Method for processing incoming GET requests """
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)  # Sending a response status code
        self.send_header("Content-type", "text/html")  # Sending the type of data to be transferred
        self.end_headers()  # Completing response headers
        self.wfile.write(bytes(page_content, "utf-8"))  # Response body


if __name__ == "__main__":
    # Initialization of a web server that will accept requests on the network according to the specified parameters
    # and send them for processing to a special class that was described above
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Setting the web server to accept incoming requests indefinitely
        webServer.serve_forever()
    except KeyboardInterrupt:
        # The correct way to stop the server in the console using the keyboard shortcut Ctrl + C
        pass

    # The correct way to stop the server currently using the address and port on the network
    webServer.server_close()
    print("Server stopped.")
