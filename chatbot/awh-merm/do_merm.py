#!/usr/bin/python

import aiml
k = aiml.Kernel()
k.learn("merm-startup.xml")
k.respond("load aiml b")
while True: 
    print (k.respond(input("> ")))
