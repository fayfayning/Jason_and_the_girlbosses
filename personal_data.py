"""
Created on 10/23/21

@author: fayfayning
"""

import time

class Status:

    def __init__(self, message):
        self.message = message
        self.time = time.time()
        self.mood = "None"

class User:

    def __init__(self, name, username):
        self.name = name
        self.username = username
        self.mood = "None"
        self.friends = set()
        self.close_friends = set()
        self.statuses = []

if __name__ == '__main__':
    print("end")