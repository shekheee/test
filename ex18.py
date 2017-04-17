def func1(*args) :
    argv1,argv2=args
    print("arg1: %s ,arg2:%s") %(argv1,argv2)

def func2(arg1,arg2):
    print ("argv1: %r ,argv2: %r")%(arg1,arg2)

def func3(arg):
    print("arg: Only one parameter %s")%arg

def func4():
    print("NO parameters")

func1(1,2)
func2("Ajay","Kailash")
func3("Shekhu")
func4()
