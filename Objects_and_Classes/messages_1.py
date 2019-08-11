class User:
    def __init__(self, username):
        self.user = username
        self.msgs = []
        self.show_user()

    def show_user(self):
        return f'{self.user}'


class Message:
    def __init__(self, content, sender: User):
        self.content = content
        self.sender = sender
        self.show_msg()

    def show_msg(self):
        return f'{self.content}'


users_dict = {}

while True:
    command_list = input().split()
    if command_list[0] == 'exit':
        break
    if command_list[0] == 'register':
        new_user = User(command_list[1])
        users_dict[command_list[1]] = new_user
    elif command_list[1] == 'send':
        if command_list[0] in users_dict.keys() and command_list[2] in users_dict.keys():
            message = Message(content=command_list[3], sender=users_dict.get(command_list[0]))
            users_dict.get(command_list[2]).msgs.append(message)


user_1, user_2 = input().split()

u_1_msgs = list(filter(lambda msgs: msgs.sender.user == user_1, users_dict.get(user_2).msgs))
u_2_msgs = list(filter(lambda msgs: msgs.sender.user == user_2, users_dict.get(user_1).msgs))

chat_lenght = 0

if len(u_1_msgs) == 0 and len(u_2_msgs) == 0:
    print('No messages')
    exit(0)
elif len(u_1_msgs) >= len(u_2_msgs):
    chat_lenght = len(u_1_msgs)
elif len(u_1_msgs) <= len(u_2_msgs):
    chat_lenght = len(u_2_msgs)


for m_index in range(chat_lenght):
    if len(u_1_msgs) > m_index:
        message = u_1_msgs[m_index]
        print (f'{message.sender.show_user()}: {message.show_msg()}')
    if len(u_2_msgs) > m_index:
        message = u_2_msgs[m_index]
        print (f'{message.show_msg()} :{message.sender.show_user()}')