import readline
from datetime import datetime
import paramiko
import os,sys,socket

target = raw_input("Masukkan Target IP : ")
user_hotspot = raw_input("Masukkan user hotspot : ")
pass_hotspot = raw_input("Masukkan password hotspot : ")

konfig = """
:global bridge1 [interface bridge port get [/interface bridge port find interface=ether2] bridge]
:global bridge2 [interface bridge port get [/interface bridge port find interface=ether10] bridge]
:global pool1  [ip dhcp-server get [/ip dhcp-server find interface=$bridge1] address-pool ]
:global pool2  [ip dhcp-server get [/ip dhcp-server find interface=$bridge2] address-pool ]
:global ip1 [/ip address get [find interface=$bridge1] address]
:set ip1 [:pick $ip1 0 [:find $ip1 "/" -1]]
:global ip2 [/ip address get [find interface=$bridge2] address]
:set ip2 [:pick $ip2 0 [:find $ip2 "/" -1]]
/ip hotspot profile add hotspot-address=$ip1 name=hsprof1
/ip hotspot profile add hotspot-address=$ip2 name=hsprof2
/ip hotspot add address-pool=$pool1 interface=$bridge1 name=hotspot1 profile=hsprof1
/ip hotspot add address-pool=$pool2 interface=$bridge2 name=hotspot2 profile=hsprof2
/ip hotspot user add name={} password={}
/system identity print
/ip hotspot export
/export file=14-5-2020


""".format(user_hotspot,pass_hotspot)

dssh = paramiko.SSHClient()
dssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
dssh.connect(target, port=22, username='usernya', password='password')
stdin, stdout, stderr = dssh.exec_command(konfig)
print "===================================="
print "Berikut Lognya :"
print "===================================="
print stdout.read()
print "===================================="
print "Aceng'WH @ 2020"