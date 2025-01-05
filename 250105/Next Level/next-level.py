user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Write your code here!
class modifier:
    def __init__(self, ID='codetree', level=10): # 초기화
        self.ID = ID
        self.level = level

user1 = modifier()
user2 = modifier('hello',28)
print("user",user1.ID,"lv",user1.level)
print("user",user2.ID,"lv",user2.level)