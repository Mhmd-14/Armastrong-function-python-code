
#Define a function called armstrong number and pass a variable n
#An Armstrong number is a special kind of number in math. It's a number that equals the sum of its digits, each raised to a power. 
#For example, if you have a number like 153, it's an Armstrong number because 1^3 + 5^3 + 3^3 equals 153
def armastrong_number(n):

#Define variable called "arm" with zero value  that will store the value of each digit in number n
    arm =0

#Type cast integer n into string to be iterated via the for loop
    m = str(n)

#Define a variable sum with zero value to accumalate the arm values to it and then compare to n
    sum = 0

#Iterate using a for loop into the provided variable
    for i in range(0,len(m),1):
       arm = int(m[i]) ** len(m)
       sum = sum + arm
#Comapre if sum of the square of digits is equal to the variable n
    if sum == n:
        return ("This is an armastrong number")
    else:
        return ("This is not an armstrong number")
#Call the function armasrtrong_number with a value
print(armastrong_number(153))



