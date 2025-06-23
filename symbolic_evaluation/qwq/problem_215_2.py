import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Calculate pi divided by the square root of 2
result = mp.pi / sqrt_2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))