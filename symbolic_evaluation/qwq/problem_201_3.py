import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Struve H function of order 0 at 1
struve_value = mp.struveh(0, 1)

# Multiply by π to get the final result
result = mp.pi * struve_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))