# -*- coding: utf8 -*-
import sys
import email
from twilio.rest import TwilioRestClient

from settings import *


class Email(object):
    def __init__(self, message_string):
        self.email = email.message_from_string(message_string)
    
    @property
    def body(self):
        return self.email.get_payload()

    @property
    def subject(self):
        return self.email.get('subject')

    @property
    def from_address(self):
        return self.email.get('from')

    @property
    def sms_subject(self, length=30):
        return "%s" % self.subject[:length]

msg = Email(sys.stdin.read())


client = TwilioRestClient(account_sid, auth_token)

body = "New email from %s. Subject: %s" % (msg.from_address, msg.subject)

message = client.sms.messages.create(body=body,
    to="+447985409504",    # Replace with your phone number
    from_="+442476101255") # Replace with your Twilio number