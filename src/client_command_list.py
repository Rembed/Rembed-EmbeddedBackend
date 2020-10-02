"""
Author: Michael Thompson (mjt106@case.edu)
Date: 9/22/2020
Brief: This file shall hold all commands to be handled by the client_commander as functions
"""

import inspect
import yaml
from src import rembed_manager


class ClientCommandList:
    def __init__(self):
        self._servers = None
        self._load_yaml()
        if self._servers is None:
            self._servers = {}

    def _dump_yaml(self):
        with open("src/servers.yaml", "w") as file:
            yaml.safe_dump(self._servers, file)

    def _load_yaml(self):
        with open("src/servers.yaml", "r") as servers:
            self._servers = yaml.safe_load(servers)

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
                if element[0][0] != "_":
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
                self._servers[args[1]] = {}
                self._servers[args[1]]["IP"] = args[2]
                self._servers[args[1]]["Port"] = args[3]
                self._dump_yaml()

        except IndexError:
            print("Not enough arguments given, type \"server_add help\" for more")

    def server_list(self, args):
        try:
            if args[1] == "help":
                print("Lists all known servers as their alias, ip, and port")
                return None

        except IndexError:
            for server in self._servers:
                print("Alias: " + server + "\n" +
                      "IP: " + self._servers[server]["IP"] + "\n" +
                      "Port: " + self._servers[server]["Port"] + "\n")
            return None

    def server_remove(self, args):
        try:
            if args[1] == "help":
                print("Removes a server from the list by its alias\n"
                      "arguments: <alias>, the alias used to remove the saved server")
            else:
                try:
                    self._servers.pop(args[1])
                except KeyError:
                    print("Server alias not found, type \"list_server\" for all saved servers")
                    self._load_yaml()
                self._dump_yaml()

        except IndexError:
            print("No alias given, type \"server_remove help\" for more")

    def server_ping(self, args):
        try:
            if args[1] == "help":
                print("Pings server from the given alias\n"
                      "arguments: <alias>, the alias of the server you want to ping")
                return None
            else:
                print("P")

        except IndexError:
            print("No alias given, type \"server_ping help\" for more")

    def start_rembed(self, args):
        try:
            if args[1] == "help":
                print("Starts the rembed client for remote embedded operations\n"
                      "arguments: <alias>, the server alias to connect to")
            else:
                _rembed_manager = rembed_manager.RembedManager(args[1])
                _rembed_manager.start()
        except IndexError:
            print("No alias given, type \"server_remove help\" for more")
