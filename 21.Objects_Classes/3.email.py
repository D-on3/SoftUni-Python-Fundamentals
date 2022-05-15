class Email:

    def __init__(self,sender,reciever,content):
        self.sender = sender
        self.reciever = reciever
        self.content = content
        self.is_sent = False
    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.reciever}: {self.content}. Sent: {self.is_sent}"

emails = []
command = input()

while command != 'Stop':
    token= command.split(' ')
    sender = token[0]
    reciever = token[1]
    content = token[2]
    email = Email(sender,reciever,content)
    emails.append(email)
    command = input()

send_emails = list(map(lambda x:int(x),input().split(', ')))

for x in send_emails:
    emails[x].send()

for email in emails:
        print(email.get_info())