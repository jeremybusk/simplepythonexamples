#!/usr/bin/env python3
import argparse
import logging
import paramiko
import sys


logging.basicConfig()
logging.getLogger("paramiko").setLevel(logging.WARNING)  # INFO, DEBUG

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", default='zadm', required=False,
        help="Username for ssh")
parser.add_argument("-p", "--password", default="demodemo", required=False, help="Password for ssh username")
parser.add_argument("-P", "--port", default=22, required=False, help="ssh tcp port")
parser.add_argument("-H", "--host", default='10.1.1.104', required=False, help="Host fqdn or ip address.")
parser.add_argument("-c", "--cmds", action='append', required=True, help="Commands to run")
args = parser.parse_args()


def main():
  run_cmd(args.cmds)


def run_cmd(cmds, host=args.host, port=args.port, username=args.username, password=args.password):
  for cmd in cmds:
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
