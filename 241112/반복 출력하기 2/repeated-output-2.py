N = int(input())

def printing(N):
    if N == 0:
        return
    printing(N-1)
    print("HelloWorld")

printing(N)
