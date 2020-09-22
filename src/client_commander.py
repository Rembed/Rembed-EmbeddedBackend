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
        return input("Enter command (type list for all commands)\n")

    def _parse_command(self, command):
        try:
            self._command_list[command]()
        except KeyError:
            print("Command \"" + command + "\" not found\n")

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
        while command is not 'x':
            command = ClientCommander._get_command()
            self._parse_command(command)

        print("Shutting down")
