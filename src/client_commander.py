"""
Author: Michael Thompson (mjt106@case.edu)
Date: 9/20/2020
Brief: This file navigates commands input from the client physically accessing the device
"""


class ClientCommander:
    def __init__(self):
        self._command_list = {}

    def run(self):
        """
        Runs the core configuration and commands loop
        """
        command = ClientCommander.get_command()
        self.parse_command(command)
        while command is not 'x':
            command = ClientCommander.get_command()
            self.parse_command(command)

        print("Shutting down")

    @staticmethod
    def get_command():
        return input("Enter command (type list for all commands)\n")

    def parse_command(self, command):
        try:
            self._command_list[command]
        except KeyError:
            print("Command \"" + command + "\" not found\n")
