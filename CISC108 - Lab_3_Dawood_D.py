# Name: Dina Dawood
# Lab 3: Function, Iteration and Selection

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available

# Problem 1
def root():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    n = (b**2 - (4*a*c))
    if n==0:
        pquad = (-b + math.sqrt(n))/(2*a)
        print("Quadratic have equal root: ",pquad)
    elif n>0:
        pquad = (-b + math.sqrt(n))/(2*a)
        nquad = (-b - math.sqrt(n))/(2*a)
        print("There are two roots: ", nquad, " and", pquad)
    else:
        print("No root exist")

# Problem 2
def reciprocals():
    for i in range(2, 11):
        print((1/i), end= ", ")

# Problem 3
def triangular_numbers():
    n = 10
    triangular = 0
    for i in range(1, n+1):
        triangular = triangular + i
    print("Triangular number", n, "via loop:", triangular)
    print("Triangular number", n, "via formula:", n*(n+1)/2)

# Problem 4
def factorial(n):
    n = 10
    factorial = 1 
    for i in range(1, n+1):
        factorial = factorial * i 
    print("Factorial of number", n," via loop:", factorial)

# Problem 5
def multiple_factorial(numlines):
    factorial = 1
    result = {}
    for i in range(1, n+1):
            factorial = factorial * i
            result[i] = factorial
    for i in range(1, n+1):
        print(result[11-i])

# Problem 6
def sums_of_reciprocals_of_factorials(numlines):
    sum_of_reciprocal = 1 
    factorial = 1
    for i in range(numlines):
            factorial = factorial * (i+1)
            sum_of_reciprocal = (sum_of_reciprocal + 1)/ factorial
    return sum_of_reciprocal

# Problem 7
def divisible_by_number(lst):
    for i in lst:
        if i > 150:
            break
        elif i%5 ==0:
            print(i)

# Problem 8
def prime_numbers(start, end):
    for i in range(start, end + 1):
        if(i%2==0):
            print(i, end=" ")
        else:
            for i in range(start, end + 1):
                if(i%2==1):
                    print(i, end = " ")


# Problem 9
# def sum_of_series(n, number_of_terms):
#     y = str(n)
#     sum = n
#     for i in range(number_of_terms-1):
# 




# All your functions go here. Follow the Beginner's Design Recipe to build your function

if __name__ == "__main__":
    # Problem 1
    root()

    # Problem 2
    reciprocals()

    # Problem 3
    triangular_numbers()

    # Problem 4
    n = 10
    factorial(n)

    # Problem 5
    multiple_factorial(n)

    # Problem 6
    sumOfReciprocal = sums_of_reciprocals_of_factorials(n)
    print("The sum of reciprocals of factorial = ",sumOfReciprocal)

    # Problem 7
    list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
    divisible_by_number(list1)

    # Problem 8
    start = 25
    end = 50
    prime_numbers(start,end)

    # Problem 9
    n = 2
    number_of_terms = 5
    sum_of_series(n,number_of_terms)

    # Problem 10
#     n = 5
#     pattern(n)
# 
#     # Problem 11
#     bmi = 21.5
#     age = 44
#     print(bmi_risk(bmi,age))
# 
#     # Problem 12
#     grading_system()
# 
#     # Problem 13
#     rock_paper_scissor()
