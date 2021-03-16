#!/usr/bin/python3 
#Author: New Wavex86 
#Date Created: Mon 15 Mar 2021
#Goes over the basic object oriented aspacts of python by defining classes
'''
Syntax:
    class ClassName:
    'Optional class documentation string'
        class_suite
'''

#Get nmap, and os to run shell commands
import nmap os 

scanner = nmap.PortScanner()


class Target:
    'Common class for all employees'
    tCount = 0

    def __init__(self, name, IP, Port): # __init__:  class constructor that is called at a new
                                    #Instance of the class
        self.name = name
        self.IP  = IP
        self.Port = Port

        self.tCount += 1

        #All the new methods must have self passed to them npw

    def displayCount(self):
        print ("Total Targets %d" % Target.tCount)

    def displayTarget(self):
        print ("Name : ", self.name, ",IP: ", self.IP, ", Port: ", self.Port)

    def scanTarget(self):
        scanner.scan(self.IP,'1-1024', '-v -sS ')
        print(scanner.scaninfo())
        print("Ip Status: ", scanner[self.IP].state())

    def scanTargetUdp(self):
        scanner.scan(self.IP,'1-1024', '-v -sU')
        print(scanner.scaninfo())
        # state() tells if target is up or down
        print("Ip Status: ", scanner[ip_addr].state())
        # all_protocols() tells which protocols are enabled like TCP UDP etc
        print("protocols:",scanner[ip_addr].all_protocols())
        print("Open Ports: ", scanner[ip_addr]['udp'].keys())

    def dnsInfo(self):
        os.system("whois " + str(self.name))

#Creating instance objects
target1 = Target("localhost", "127.0.0.1", 80)

target1.displayTarget()

target1.scanTarget()

exit (0) 
