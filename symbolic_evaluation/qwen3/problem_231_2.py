import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2 using mpmath's sqrt function
result = mp.sqrt(2)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))