#!/usr/bin/env python3
import argparse
from email.message import EmailMessage
from email.mime.text import MIMEText
import os
import smtplib
import sys

subject = "Test"
body = "This is a test."

SOURCE_EMAIL = os.getenv('SOURCE_EMAIL')
DESTINATION_EMAILS = os.getenv('DESTINATION_EMAILS')
RELAY_HOST = os.getenv('RELAY_HOST')

parser=argparse.ArgumentParser()
parser.add_argument(
    "-r", "--relay-host", default=RELAY_HOST, required=True,
    help="Specify the relay host IP or FQDN.")
parser.add_argument(
    "-d", "--destination-emails", default=DESTINATION_EMAILS, required=True,
    help="Specify the destination email address.")
parser.add_argument(
    "-s", "--source-email", default=SOURCE_EMAIL, required=True,
    help="Specify the from email address")
args=parser.parse_args()


def send_email(relay_host, email_from, recipients, subject, body, email_port=25, use_smtpauth=False, email_username=None, email_password=None):

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_from
    msg['To'] = recipients
    msg = msg.as_string()

    if use_smtpauth:
        print("Sending authenticated TLS relay test message.")
        if email_username is None or email_password is None:
            print("Requires username and password")
            return
        session = smtplib.SMTP(relay_host, email_port)
        session.ehlo()
        session.starttls()
        session.login(email_username, email_password)
        session.sendmail(email_username, recipients, msg)
        session.quit()
    else:
        print("Sending non-authenticated non-TLS relay test message.")
        session = smtplib.SMTP(relay_host, email_port)
        session.ehlo()
        session.sendmail(email_from, recipients, msg)
        session.quit()


send_email(args.relay_host, args.source_email, args.destination_emails, subject, body, email_port=25, use_smtpauth=False, email_username=None, email_password=None)
