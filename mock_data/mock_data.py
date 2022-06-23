#!/usr/bin/python3

import random

class MockData:
    
    YES_NO = ['Yes','No']    
    FICTIONAL_PEOPLE = [
        'Henry Higgins','Eliza Doolittle','Jason Rhodes','Riley Jones','Frank Cross','Eliza Zhao',
        'Alex Lane','George Lane','Claire Thompson','Robert Graham','Angie Pogue','Francis Rosencrantz',
        'James Lipton','Thomas Sully','Finn Harris','Julia Harris','Kyyle Wibble','James Kirk','Leonard McCoy',
        'Nihota Uhura','Hikaru Sulu','Pavel Checkov','Montgomery Scott','Amanda Grayson','Richard Daystrom',
        'Jack ONeill','Daniel Jackson','Samantha Carter','George Hammond','Meredith McKay','John Sheppard',
        'Cameron Mitchell','Hank Landry','Jonas Quinn','Vala Maldoran','Janet Fraiser','Walter Harriman',
        'Robert Kinsey','Richard Woolsey','Catherine Langford','Ryland Grace', 
    ]

    @classmethod
    def random_entity():
        return random.choice(MockData.FICTIONAL_PEOPLE)

    @classmethod
    def random_y_n():
        return random.choice(MockData.YES_NO)

    