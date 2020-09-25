"""
Author: Michael Thompson (mjt106@case.edu)
Date: 9/22/2020
Brief: This file shall hold all commands to be handled by the client_commander as functions
"""

import inspect


class ClientCommandList:
    def __init__(self):
        None

    def exit(self, args):
        return None

    def list(self, args):
        try:
            if args[1] == "help":
                print("Lists all of the available commands")
                return None
        except IndexError:
            print("Available commands:")
            for element in inspect.getmembers(self):
                if element[0][0] is not "_":
                    print(element[0])

    def server_add(self, args):
        try:
            if args[1] == "help":
                print("Adds a server to the known list\n"
                      "arguments: <alias>, the alias the server shall be known by\n"
                      "           <ip>, the ip address of the server\n"
                      "           <port>, the port for connecting to the server")
                return None
            # check to make sure enough arguments are given
            elif args[3]:
                None
            else:
                return None
        except IndexError:
            print("Not enough arguments given, type \"server_add help\" for more")

    def server_list(self, args):
        try:
            if args[1] == "help":
                print("Lists all known servers as their alias, ip, and port")
                return None
        except IndexError:
            return None

    def server_ping(self, args):
        try:
            if args[1] == "help":
                print("Pings server from the given alias\n"
                      "arguments: <alias>, the alias of the server you want to ping")
                return None
            else:
                None

        except IndexError:
            print("No alias given")
