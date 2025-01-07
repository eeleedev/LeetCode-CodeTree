class Number:
    def __init__(self, order, x, y):
        self.order = order
        self.x = x
        self.y = y

n = int(input())
arr = [(i+1, *map(int, input().split())) for i in range(n)]
numbers = [Number(order, x, y) for order, x, y in arr]

numbers.sort(key=lambda x: (abs(x.x+x.y), x.order))


for number in numbers:
    print(number.order)

