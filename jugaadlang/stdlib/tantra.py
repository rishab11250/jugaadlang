"""
tantra — JugaadLang System and Environment Module.
"""
import sys
import os

# System attributes
path = sys.path
argv = sys.argv
exit = sys.exit
platform = sys.platform
environment = os.environ

# OS attributes
folder_ka_naam = os.getcwd
badlo_folder = os.chdir
shell_chalao = os.system
name = os.name
pid = os.getpid
