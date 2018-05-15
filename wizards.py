#!/usr/bin/env python

import random

def random_wiz_property(wizprop):
    line = next(wizprop)
    for num, aline in enumerate(wizprop):
      if random.randrange(num + 2): continue
      line = aline
    return line

files = ['wizard_names.txt','wizard_elements.txt','wizard_from.txt']

wizard_property = []
for propfile in files:
  wizard_property.append(random_wiz_property(open(propfile)).strip())

print wizard_property[0] + " " + wizard_property[1] + " from " + wizard_property[2]
