"""
Author: Michael Thompson (mjt106@case.edu)
Date: 9/22/2020
Brief: This file shall hold all commands to be handled by the client_commander as functions
"""

import inspect


class ClientCommandList:
    def __init__(self):
        self._commands = {}

    def exit(self):
        return None

    def list(self):
        print("Available commands:")
        for element in inspect.getmembers(self):
            if element[0][0] is not "_":
                print(element[0])

    def list_servers(self):
        return None