#!/usr/bin/env python3
import argparse
import logging
import paramiko
import sys


logging.basicConfig()
logging.getLogger("paramiko").setLevel(logging.WARNING)  # INFO, DEBUG

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", default='myuser', required=False,
        help="Username for ssh")
parser.add_argument("-p", "--password", default="mypassword", required=False, help="Password for ssh username")
parser.add_argument("-P", "--port", default=22, required=False, help="ssh tcp port")
parser.add_argument("-H", "--host", default='192.168.1.1', required=False, help="Host fqdn or ip address.")
parser.add_argument("-c", "--cmd", required=True, help="Command to run")
args = parser.parse_args()


def main():
  run_cmd(args.cmd)


def run_cmd(cmd, host=args.host, port=args.port, username=args.username, password=args.password):
  try:
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password, allow_agent=False, look_for_keys=False)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    outlines=stdout.readlines()
    resp=''.join(outlines)
    print(resp) # Output
  except Exception as e:
    print(f'Exception: {e}')


if __name__ == '__main__':
    main()
