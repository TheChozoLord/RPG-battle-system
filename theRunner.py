# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:12:01 2024

@author: owen.merrill
"""
import tbc

def main():
    player = tbc.Character()
    npc = tbc.Character("notus", 30, 20, 5, 0)

    player.printStats()
    npc.printStats()

    tbc.fight(player, npc)

if __name__ == "__main__":
    main()