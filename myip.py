#!/usr/bin/python
'''
Get external IP Address
@author: kbandla
'''
import urllib
def getip():
        url = "http://automation.whatismyip.com/n09230945.asp"
        u = urllib.urlopen(url)
        ip = u.read()
        u.close()
        return ip

if __name__ == "__main__":
        print getip()
