"""
tantra — JugaadLang System and Environment Module.
"""

import sys
import os
import subprocess

# System attributes
path = sys.path
argv = sys.argv
exit = sys.exit
platform = sys.platform
environment = os.environ

# OS attributes
folder_ka_naam = os.getcwd
badlo_folder = os.chdir
name = os.name
pid = os.getpid


def shell_chalao(command: str) -> int:
    """Run a shell command and return exit code."""
    result = subprocess.run(command, shell=True)  # noqa: S603
    return result.returncode

