a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
def triangle_type(a,b,c):
    if a==b==c:
        print("Триъгълникът е равностранен")
    if a==b or b==c or a==c:
        print("Триъгълникът е равнобедрен")
    else:
        print("Триъгълникът е разностранен")
triangle_type(a,b,c)

