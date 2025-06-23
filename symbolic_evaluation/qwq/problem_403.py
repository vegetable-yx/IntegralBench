import mpmath as mp
mp.dps = 15

# Calculate 7! using mpmath's factorial function
result = mp.factorial(7)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))