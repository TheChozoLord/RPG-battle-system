# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:31:02 2024

@author: owen.merrill
"""
import random

class Character(object):    
    
    def __init__(self):
        super().__init__()
        self.name = "Guy"
        self.health = 15
        self.hitchance = 75
        self.maxdamage = 4
        self.armor = 4
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def hitpoints(self):
        return self.__hitpoints
    
    @hitpoints.setter
    def hitpoints(self, value):
        value = self.testInt (value, 0, 1000, 0)
        self._hitpoints = value
    
    @property
    def attack(self):
        hit = random.randint(1,100)
        if (hit <= self.hitchance):
            strike = random.randint(1, self.maxdamage)
            return strike
        else:
            print("You miss.")
    
    def printStats(self):
        print(
        f"""
         {self.name}
         Health: {self.health}
         Hit chance: {self.hitchance}%
         Maximum damage: {self.maxdamage}
         Armor: {self.armor}
              """)

def main():
    c = Character()
    c.printStats()
    input("press enter to attack.")
    c.attack
    
main()