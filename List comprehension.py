#Vedanth M
x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
N = int(raw_input())
a = [[X, Y, Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X+Y+Z!=N]
print(a)
