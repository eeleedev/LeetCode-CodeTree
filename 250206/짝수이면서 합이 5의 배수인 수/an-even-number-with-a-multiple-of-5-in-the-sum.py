n = int(input())

# Write your code here!
def magic_num(n):
    if n%2 == 0:
        dec = n // 10
        figure = n%10
        temp = dec + figure
        if temp%5 == 0:
            print("Yes")
        else:
            print("No")

magic_num(n)