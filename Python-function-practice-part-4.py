#1.Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

#print (max_num(3, 6, 9))

def max_num(a, b, c):
    return max(a, b, c)

print (max_num(15, 30, 2))

#2. Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(numbers):
    #base case:
    if not numbers:
        return 1
    else:
        #recursive case
        return numbers[0] * mult_list(numbers[1:])

print (mult_list([1,2,3]))

#3. Write a Python function called rev_string() to reverse a string.

def rev_string(str):
    if len(str) == 1:
        return str
    else:
        return rev_string(str[1:]) + str[0]

print (rev_string("hello"))

#4. Write a Python function called num_within() to check whether a number falls in a given range.
#The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
#Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(num, start, end):
    return start <= num <= end

print (num_within(3, 2, 4))
print (num_within(3, 1, 3))
print (num_within(10, 2, 5))   

#5.Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
#The function accepts the number n, the number of rows to print
#Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.


triangle=[[1],[1,1]]
def pascal(n):
    if n < 1:
        print("Incorrect input")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]

            for i in range(len(row_prev)+1):
                if i == 0:
                    row.append(1)
                elif i == len(row_prev):
                    row.append(1)
                else:
                    row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
            triangle.append(row)
            row_number += 1

            for row in triangle:
                print(row)

pascal(5)
pascal(10)