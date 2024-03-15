# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 10:31:02 2024

@author: owen.merrill
"""
import random

class Character(object):    
    
    def __init__(self,
                 name = "Guy",
                 health = 15,
                 hitchance = 75,
                 maxdamage = 4,
                 armor = 4):
        
        super().__init__()
        self.name = name
        self.health = health
        self.hitchance = hitchance
        self.maxdamage = maxdamage
        self.armor = armor
        
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
    
    def attack(self, target):
        hit = random.randint(1,100)
        if (hit <= self.hitchance):
            damage = random.randint(1, self.maxdamage)
            damage -= target.armor 
            if damage < 0:
                damage = 0
            target.health -= damage
            print(f"""{self.name} deals {damage} points of damage to {target.name}.""")
            return damage
        else:
            print(f"""{self.name} misses.""")
    
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
    player = Character()
    npc = Character("notus", 30, 20, 5, 0)
    player.printStats()
    npc.printStats()
    fight(player, npc)
    
def fight(player, npc):
    keepGoing = True
    while keepGoing == True:
        print(f"""{player.name}: {player.health}""")
        print(f"""{npc.name}: {npc.health}""")
        input("press enter to attack.")
        player.attack(npc)
        npc.attack(player)
        if player.health <= 0:
            print("You lose.")
            keepGoing = False
        if npc.health <= 0:
            print("You win!")
            keepGoing = False

main()