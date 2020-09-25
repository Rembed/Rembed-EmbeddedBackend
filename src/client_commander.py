"""
Author: Michael Thompson (mjt106@case.edu)
Date: 9/20/2020
Brief: This file navigates commands input from the client physically accessing the device
"""

from src import client_command_list
import inspect


class ClientCommander:
    def __init__(self):
        self._client_command_list = client_command_list.ClientCommandList()
        self._command_list = {}
        self._construct_command_list()

    @staticmethod
    def _get_command():
        return input("Enter command (type list for all commands, <command> help for more)\n").split(" ")

    def _parse_command(self, command):
        try:
            self._command_list[command[0]](command)
        except KeyError:
            print("Command \"" + command[0] + "\" not found")

    def _construct_command_list(self):
        for element in inspect.getmembers(self._client_command_list):
            if element[0][0] is not "_":
                self._command_list[element[0]] = element[1]

    def run(self):
        """
        Runs the core configuration and commands loop
        """
        command = ClientCommander._get_command()
        self._parse_command(command)
        print()
        while command[0] != "exit":
            command = ClientCommander._get_command()
            self._parse_command(command)
            print()
        print("Shutting down")
