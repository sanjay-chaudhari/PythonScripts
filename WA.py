from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'accountSid'
auth_token = 'authToken'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there - Sending msg using PYTHON & TWILIO - NEW !',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+919966649483'
                          )

print(message.sid)
