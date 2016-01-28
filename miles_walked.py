# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 20:40:26 2016

@author: Erin
"""

##mile_walking_program
miles_walked1 = 0

miles_walked2 = 102

walking = True

while walking:
      print("Walker1 still walking! On mile {}".format(miles_walked1))
      miles_walked1 += 2
      if miles_walked1 == 102:
          walking = False
      elif miles_walked2 != miles_walked1:
          print("Walker2 hasn't met Walker1 yet. On mile{}".format(miles_walked2))
          miles_walked2 -= 1
          if miles_walked2 == 0:
              walking = False
          
      if miles_walked2 == miles_walked1:
          print("Walker2 has met Walker1 at mile{}".format(miles_walked2))
          walking = False

      
else:
    walking = False

print("Whew! We're tired")
