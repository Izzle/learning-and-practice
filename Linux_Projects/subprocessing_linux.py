#!/usr/bin/env python3

import subprocess
import getpass

# Proof of concept showing we can capture any output from the shell
output = subprocess.check_output('ls', shell=True)
print(output)

# You can use this to translate between 2 different programming languages
subprocess.call('python3 talktome.py "Abra Kadabra!"', shell=True)

# Depending on your OS you can install modules, run Powershell commands, the
# possibilities are endless! Remember, With Great Power Comes Great Responsibilityd
subprocess.call('sudo apt-get install python-tweepy', shell=True)

