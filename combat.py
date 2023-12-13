# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:59:51 2023

@author: Kyle Sanders and David Muana
"""

import tbc

def main():
    hero = tbc.Character()
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 5
    
    monster = tbc.Character("Monster", 20, 50, 3, 2)
    
    hero.printStats()
    monster.printStats()
    
    tbc.fight(hero, monster)
    
if __name__ == "__main__":
    main()
    
    