import sys
import subprocess


def start_api():
    subprocess.run(["python3", "-m", "app"])


def format():
    result = subprocess.run(["python3", "-m", "black", "."])
    exit(result.returncode)


def lint():
    result = subprocess.run(["python3", "-m", "ruff", "check", "."] + sys.argv[1:])
    exit(result.returncode)
