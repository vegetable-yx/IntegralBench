import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi divided by 4 using mpmath's constant
result = mp.pi / 4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))