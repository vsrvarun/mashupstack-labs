# Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
value = int(input("Enter the value of n \n"))
if value < 0:
    print("Enter a positive integer")
else:
    def sum_of_serires(n):
        if n <= 0:
            return 0
        else:
            return (n + sum_of_serires(n - 2))
    result = sum_of_serires(value)
    print("Sum of series:", result)