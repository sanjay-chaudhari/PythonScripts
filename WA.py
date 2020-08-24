from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACdb753b826870e21ef72327cbd4621f2b'
auth_token = '3a450bea33b063e33d5916837fcbcfa9'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there - Sending msg using PYTHON & TWILIO - NEW !',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+919766649483'
                          )

print(message.sid)