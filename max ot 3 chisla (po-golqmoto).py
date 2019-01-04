a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
def max3(a,b,c):
    if c > b > a or c > a > b:
        print(c)
    if b > a > c or b > c > a:
        print(b)
    if a > b > c or a > c > b:
        print(a)
    if a == b == c:
        print("Равни са")
max3(a,b,c)
