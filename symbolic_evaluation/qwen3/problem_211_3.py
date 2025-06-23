import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate square root of 3 using mpmath's sqrt function
result = mp.sqrt(3)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))