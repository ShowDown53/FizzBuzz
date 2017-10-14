#!/usr/bin/env python
# -*- coding: utf-8 -*-

start = "da"

while start.lower() == "da":
    userInput = raw_input("Vnesite število med 1 in 100: ")

    if not userInput.isdigit():
        print("Niste vnesli števila.")
        continue

    userInput = int(userInput)

    if userInput > 100:
        print("Vnesli ste število večje kot 100.")
        continue

    if userInput < 1:
        print("Vnesli ste število manjše kot 1.")
        continue

    for x in range(1, userInput + 1):
            if x % 3 == 0 and x % 5 == 0:
                print "fizzbuzz"
            elif x % 3 == 0:
                print "fizz"
            elif x % 5 == 0:
                print "buzz"
            else:
                print x

    start = raw_input("Želite poskusiti ponovno? Odgovorite z 'Da' ali 'Ne': ")

print "<<<<-----Have a nice day!----->>>>"