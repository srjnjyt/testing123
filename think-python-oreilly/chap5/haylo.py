"""
checks friendship levels
"""


import os
import sys
import math
import xml.etree.ElementTree as ET
import csv

def main():
    
    tree = ET.parse('haylo')

    player = tree.find('player')
    
    friends = player.find('friendshipData').findall('item')
    is_datable = ['Emily', 'Leah', 'Penny', 'Maru', 'Haley', 'Abigail', 'Elliott', 'Alex', 'Harvey', 'Sam', 'Sebastian', 'Shane']
    npc_friendship = dict()
    for item in player.find('friendshipData').findall('item'):
        t = int(item.find('value').find('Friendship').find('Points').text)//250
        v = item.find('key').find('string').text
        if t >= 8:
            if v in is_datable:
                npc_friendship[item.find('key').find('string').text] = '💙'
            else:
                if t >= 10:
                    npc_friendship[item.find('key').find('string').text] = '💙'
            
        else:
            npc_friendship[v] = t

    npc_list = ['Harvey', 'Pierre', 'Abigail', 'Caroline', 'George', 'Evelyn', 'Alex', 'Penny', '-', 
    'Gus', 'Emily', 'Shane', 'Lewis', 'Clint', 'Pam' , '-', 
    'Jodi', 'Kent', 'Vincent', 'Sam', 'Haley', 'Marnie', 'Leah', 'Elliott', 'Willy', 'Jas', 'Krobus', 'Wizard', '-', 
    'Robin', 'Demetrius', 'Maru', 'Sebastian', 'Linus', 'Dwarf', 'Leo', '-', 
    'Sandy']

    with open('friendship.csv', 'w') as friendship:
        writer = csv.writer(friendship)
        writer.writerow(['Person', 'Hearts'])
        for i in range(len(npc_list)):
            try:
                writer.writerow([npc_list[i], npc_friendship[npc_list[i]]])
            except:
                writer.writerow([npc_list[i], ' '])


if __name__ == "__main__":
	main()