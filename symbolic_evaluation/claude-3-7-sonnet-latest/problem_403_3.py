import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate factorial of 7 using mpmath's factorial function
result = mp.factorial(7)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))