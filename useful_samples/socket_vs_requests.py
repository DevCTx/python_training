'''
    Shows some differences between socket and requests module to send a simple request to a server
'''
import sys

def test_socket_vs_request(MODULE_SOCKET=False):

    if MODULE_SOCKET :
        print("\nTest with socket module")
        import socket
    else :
        print("\nTest with requests module")
        import requests

    if len(sys.argv) not in [2, 3]:
        print("Improper number of arguments : at least one is required and no more than 2 are allowed :")
        print("- http server's address (required)")
        print("- port number (defaults to 80 if not specified)")
        return 1
    else :
        port = int(sys.argv[2]) if len(sys.argv) == 3 else 80
        if 1 <= port <= 65535:
            try:
                if MODULE_SOCKET:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    print("Try to connect to", sys.argv[1], "on port", port)
                    sock.settimeout(1)
                    sock.connect((sys.argv[1], port))
                else:
                    print("Try to connect to", sys.argv[1], "on port", port)
                    answer = requests.head("http://"+sys.argv[1]+":"+str(port), timeout=1)

            except TimeoutError if MODULE_SOCKET else requests.Timeout :
                print("Timeout : Server has not been connect on time ")
                return 3

            except ConnectionRefusedError if MODULE_SOCKET else requests.ConnectionError:
                print("Error : Connection refused by the server")
                return 4

            except socket.gaierror if MODULE_SOCKET else requests.RequestException:
                print("Error : Impossible to get address information")
                return 5

            else:
                if MODULE_SOCKET:
                    sock.send(b"GET / HTTP/1.1\r\nHost:" + bytes(sys.argv[1], "utf8") + b"\r\nConnection: close\r\n\r\n")
                    answer = sock.recv(10000)        #  The return value is a bytes object representing the data received.
                    print( answer.decode('utf-8') )  #  Can be read as str using decode
                else:
                    print( answer )            # Answer by a Response object
                    print( answer.status_code, answer.headers )     # Easily accessible via a dictionary
                return 0
        else:
            print("Wrong argument : Port number must be between 1 and 65535")
            return 2


# socket_vs_requests.py github.com 80

test_socket_vs_request(False)   # Test requests

# Test with requests module
# Try to connect to github.com on port 80
# <Response [301]>
# 301 {'Content-Length': '0', 'Location': 'https://github.com/'}

test_socket_vs_request(True)    # Test socket

# Test with socket module
# Try to connect to github.com on port 80
# HTTP/1.1 301 Moved Permanently
# Content-Length: 0
# Location: https://github.com/
# connection: close
