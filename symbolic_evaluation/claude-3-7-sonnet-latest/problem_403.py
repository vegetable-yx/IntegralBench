import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate factorial of 7
result = mp.factorial(7)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))