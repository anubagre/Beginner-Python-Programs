#FizzBuzz Game from 1 to 50
for i in range(1,51):
    if(i%3==0 and i%5!=0):
        print("Fizz")
    elif(i%3!=0 and i%5==0):
        print("Buzz")
    elif(i%3==0 and i%5==0):
        print("FizzBuzz")
    else:
        print(i)