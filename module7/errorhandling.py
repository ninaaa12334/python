#try:
   # print("pjeseto dy numra")
   # nr1=int(input("shkruani nr1:"))
   # nr2=int(input("shkruani nr2:"))
   # resultati=nr1/nr2
  #  print("rezultati", resultati)
#except ZeroDivisoinError:
   # print("ke gabu per shkak qe je duke pjestuar me 0")

    #second exmaple

    fruits={
        "apples":5,
        "banana": 6,
        "orange":7
    }
try:
    print(fruits["cherry"])
except KeyError:
    print("The key does not exist in the dictionary")

text="this is not  number"
#third example

try:
    text_to_int=int(text)
except Exception as e:
    print("An error occorred while parsing the data", e)

#fourth example

try:
    resultati=10/2
except ZeroDivisionError:
    print("division by zero error occorred")
else:
    print("division successful, Result:", resultati)


#fifth example


try:
    resultati =10/5
except ZeroDivisionError:
    print("Division by zero error occorred")
finally:
    print("This part of code always runs")
