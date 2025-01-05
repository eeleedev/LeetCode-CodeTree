secret_code, meeting_point, time = input().split()
time = int(time)

# Write your code here!
class ID:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

ID1 = ID(secret_code, meeting_point, time)
print("secret code :", ID1.secret_code)
print("meeting point :", ID1.meeting_point)
print("time :", ID1.time)