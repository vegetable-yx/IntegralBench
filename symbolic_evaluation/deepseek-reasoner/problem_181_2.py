import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the reciprocal of pi
pi_value = mp.pi
result = 1 / pi_value

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))