import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the sum of pi and 2
pi_plus_2 = mp.pi + 2

# Divide the sum by 2 to get the final result
result = pi_plus_2 / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))