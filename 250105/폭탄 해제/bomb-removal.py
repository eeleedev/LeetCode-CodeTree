unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Write your code here!
class Code:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

code1 = Code(unlock_code, wire_color, seconds)

print("code :", code1.code)
print("color :", code1.color)
print("second :", code1.second)