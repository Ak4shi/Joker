from math import sqrt
import time

def getclass(number:int):
  classer = "null"
  if number < 10:
    number += 6
    number*1.5
  while number > 7:
    number = sqrt(number)
    number = round(number)
  if number == 1:
    classer = "beserker"
  if number == 2:
    classer = "rider"
  if number == 3:
    classer = "lancer"
  if number == 4:
    classer = "saber"
  if number == 5:
    classer = "archer"
  if number == 6:
    classer = "assassin"
  if number == 7:
    classer = "caster"
  return classer

def getattack(number:int):
  if number < 150:
    number += 123
    number = number*1.5
  while number > 150:
    number = number ** (1./3.)
    number = round(number)
  return number


def gethp(number:int):
  if number < 1100:
    number += 1234
    number = number*1.5
  while number > 1100:
    number = sqrt(number)
    number = round(number)
  return number
