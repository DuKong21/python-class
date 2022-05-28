def addone():
    global i
    print("\t 전역변수i읽기, i+1:", i + 1)
    i+= 1

i = 20
print("i=",i)
addone()
print("i=",i)