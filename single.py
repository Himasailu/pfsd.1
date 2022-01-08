class parent:
    def function1(selfself):
        print("this is function one")
class child(parent):
    def function2(selfself,a):
        print("this is function 2")
        print(a)
    b=20
y=child()
y.function1()
y.function2(10)
print(y.b)