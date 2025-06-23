import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2 using mpmath's sqrt function
result = mp.sqrt(2)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))