class User:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = 5
arr = [tuple(input().split()) for _ in range(n)]
users = [User(name, int(height), float(weight)) for name, height, weight in arr]

users.sort(key=lambda x: x.name)
print('name')
for user in users:
    print(user.name, user.height, round(user.weight,1))
print()
users.sort(key=lambda x: (-x.height))
print('height')
for user in users:
    print(user.name, user.height, round(user.weight,1))