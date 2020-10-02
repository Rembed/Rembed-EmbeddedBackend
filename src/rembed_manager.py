"""
Author: Michael Thompson (mjt106@case.edu)
Date: 10/2/2020
Brief: This file is the main manager for the rembed application as it pertains to the core functionality
       described in the proposal
"""

import yaml
import subprocess


class RembedManager:
    def __init__(self, _server_alias):
        self._server_list = {}
        with open("src/servers.yaml", "r") as file:
            self._server_list = yaml.safe_load(file)

        self._server_ip = self._server_list[_server_alias]["IP"]
        self._server_port = self._server_list[_server_alias]["Port"]

    def start(self):
        subprocess.call("../STLinkInternetBridge.sh")
