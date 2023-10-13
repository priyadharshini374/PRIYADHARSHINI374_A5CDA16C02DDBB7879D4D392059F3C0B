#Implement a recursive function to calculate the factoriel of a given number.


def fact(n):
  if n ==0 or n ==1:
    return 1
  else:
    return n * fact(n - 1)
                  
   
number = int(input("Enter a value:"))

res = fact(number)
print("the factorial of {} is{}.".format(number, res))
