class User:
    def __init__(self, username, inbox_msgs = []):
        self.user = username
        self.msgs = inbox_msgs


class Message:
    def __init__(self, content, sender: User):
        self.content = content
        self.sender = sender


def new_message(data_list):
    return Message(data_list[3], data_list[0])

def format_messages(user_1: User, user_2: User, message_1, message_2):
    return f'{user_1.user}: {message_1}\n{message_2} :{user_2.user}'

def check_messages(user_1: User, user_2: User):
    user_1_msgs_dict = {}
    user_2_msgs_dict = {}

    chat_list = user_1_msgs_dict, user_2_msgs_dict
    for check in user_1.msgs:
        if check.sender == user_2.user:
            user_1_msgs_dict[check.sender] = check.content

    for check in user_2.msgs:
        if check.sender == user_1.user:
            user_2_msgs_dict[check.sender] = check.content

    if len(user_1_msgs_list) == 0 and len(user_2_msgs_list) == 0:
        return ['No messages']
    else:
        return chat_list

users_dict = {}

while True:
    command_list = input().split()
    if command_list[0] == 'exit':
        break

    if command_list[0] == 'register':
        new_user = User(command_list[1])
        users_dict[command_list[1]] = new_user

    if command_list[1] == 'send':
        sender = command_list[0]
        recipient = command_list[2]
        if sender in users_dict.keys() and recipient in users_dict.keys():
            new_msg = new_message(command_list)
            users_dict.get(recipient).msgs.append(new_msg)


user_1, user_2 = input().split()

for chat in check_messages(users_dict.get(user_1), users_dict.get(user_2)):
    if chat == 'No messages':
        print 'No messages'
        break

    while len(chat[0].values()) == 0 and len(chat[1].values()) == 0

