import json
import urllib.request
import socket
import time
import random
import os
import datetime


def get_ip(link='https://api.ipify.org/?format=json', outfile='ip_info.txt', delimiter="\t", keep_last=4):
    log_lines=5
    print("IP Address Retriever")
    now = datetime.datetime.now()
    print(now)
    # Getting computer name --------------------------------------------------------------------------------------------
    print("Getting Hostname...", end='\r')
    print("\t\t\t", end='\r')
    print(socket.gethostname())
    # getting internal ip information ----------------------------------------------------------------------------------
    print("Getting Internal IP...", end='\r')
    # time.sleep(random.random() * 2)
    lip = socket.gethostbyname(socket.gethostname())  # getting local ip
    print("\t\t\t", end='\r')
    print(lip)  # printing said local ip
    # getting external information -------------------------------------------------------------------------------------
    print("Getting External IP...", end='\r')
    resp = urllib.request.urlopen(link).read()
    code = json.loads(resp.decode('utf-8'))
    ip = code["ip"]
    print("\t\t\t", end='\r')
    print(ip)  # printing external ip
    # preparing to write information to a file -------------------------------------------------------------------------
    outfile, ext = outfile.split(".", 1)
    path = os.path.dirname(os.path.realpath(__file__))
    outfile = path + "\\" + outfile + "_" + socket.gethostname() + '.' + ext
    data = list()
    # getting past data
    with open(outfile, mode='r') as f:
        for i in f:
            data.append(i)
    #writing past data
    with open(outfile, mode='w') as f:
        f.write("computer " + delimiter + socket.gethostname() + "\n")
        f.write("time     " + delimiter + str(now) + "\n")
        f.write("external " + delimiter + str(ip) + "\n")
        f.write("internal " + delimiter + str(lip) + "\n\n")
        for i in data[:(keep_last * log_lines)]:  # writing last 'keep last' entries.  
            f.write(i)
    print("Written to: " + outfile)
    time.sleep(5)


if __name__ == "__main__":
    get_ip()
