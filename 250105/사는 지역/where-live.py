n = int(input())
users = []
name_order = []

class User:
    def __init__(self, name, post_num, loc):
        self.name = name
        self.post_num = post_num
        self.loc = loc

for _ in range(n):
    name, post, loc = input().split()
    users.append(User(name,post,loc))

for i in range(n):
    name_order.append(users[i].name)

name_order.sort()
last_name = name_order.pop()
last_index = 0

for i in range(n):
    if last_name == users[i].name:
        last_index = i

print('name',users[last_index].name)
print('addr',users[last_index].post_num)
print('city',users[last_index].loc)