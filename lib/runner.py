import subprocess
import sys

def exec_command(cmd):
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    print(stdout.decode())
    print(stderr.decode())

def get_output(cmd):
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    return stdout.decode(), stderr.decode()