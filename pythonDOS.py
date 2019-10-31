# Import dependencies
import socket, random, time, sys


# Class definition
class pythonDOS():

    # Class init function, initialize object
    def __init__(self, ip, port=80, socketsCount = 200):
        self._ip = ip
        self._port = port
        self._headers = [
            "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)",
            "Accept-Language: en-us,en;q=0.5"
        ]


# Main function
if __name__ == "__main__":
    dos = pythonDOS("192.168.0.236", 81, socketsCount=200)