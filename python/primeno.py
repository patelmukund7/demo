# Program to check if a number is prime or not

num = int(input("Enter a number: ")) #input

if num == 0 or num == 1: #predefined non-prime numbers
    print(num, "is not a prime number")
elif num > 1:
   for i in range(2,num):
       if (num % i) == 0: #check for factors
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number") 
else:
   print(num,"is not a prime number")