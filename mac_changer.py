#!/usr/bin/env python

import subprocess
from optparse import OptionParser

def Change_Mac(interface, new_mac):
    print("[+] Changing mac address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

parser = OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New Mac Address")

(options, arguments) = parser.parse_args()

if __name__ == "__main__":
    Change_Mac(options.interface, options.new_mac)