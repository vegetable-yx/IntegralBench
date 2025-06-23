import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the square root of 2 using mpmath's sqrt function
result = mp.sqrt(2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))