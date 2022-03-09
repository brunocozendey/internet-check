import subprocess, platform
import re
from datetime import datetime
from time import sleep

def get_default_ip():
    output = subprocess.check_output(["ip", "-o", "route", "get", "1.1.1.1"],
                                     universal_newlines=True)
    return str(output.split(" ")[2])

def pingOk(sHost):
    rtt_regex = re.compile('(time=)([0-9.-]+)')
    dt_string = str(datetime.now().strftime("%d/%m/%Y|%H:%M:%S"))
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', sHost), shell=True)
        rtt = rtt_regex.findall(str(output))
        
        

    except Exception:
        return ("{}|{}".format(dt_string,"-1"))

    return ("{}|{}".format(dt_string,rtt[0][1]))


ip_list = [(0,get_default_ip()),(1, '8.8.8.8'),(1,'google.com'), (2, '186.192.81.31'),(2, 'g1.globo.com'), (3,'31.13.85.36'), (3,'facebook.com')]

while (True):
    for ip in ip_list:
        ping_result = pingOk(ip[1])
        filename = str(datetime.now().strftime("%Y%m%d"))+"_connection_status"
        with open(filename, "a") as file_object:
            # print("{}|{}|{}".format(ping_result, ip[1], ip[0]))
            file_object.write("{}|{}|{}\n".format(ping_result, ip[1], ip[0]))
    sleep(60)


