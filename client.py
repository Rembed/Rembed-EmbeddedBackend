"""
Author: Michael Thompson (mjt106@case.edu)
Date: 9/20/2020
Brief: This is the main application file for the embedded backend client
"""
from src import client_commander

if __name__ == "__main__":
    with open("src/logo.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line, end="")
        print()

    client_commander = client_commander.ClientCommander()
    client_commander.run()