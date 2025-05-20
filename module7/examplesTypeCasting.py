age=25
age_As_string=str(age)
print(age_As_string, " of type", type(age_As_string))

print(bool(0))#false
print(bool(42))#true


print(bool(""))
print(bool("hello"))

x=32
y=5.3
resultati=x+y
print(resultati, "of type", type(resultati))

a=5
b="3"
resultati1=a*int(b)
print(resultati1, "of type", type(resultati1))

c=4
resultati2="Hello"*c
print(resultati2, "of type", type(resultati2))

#get two numbers from user input and sum them up

nr1=int(input("first number:"))
nr2=int(input("second number:"))
sum=nr1+nr2
print(sum)