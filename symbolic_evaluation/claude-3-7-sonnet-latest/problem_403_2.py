import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate 7! (factorial of 7) using mpmath's factorial function
result = mp.factorial(7)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))