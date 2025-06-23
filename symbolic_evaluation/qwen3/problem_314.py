import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Li_3(1/2)
term1 = mp.polylog(3, 0.5)

# Calculate Li_3(-1/2)
term2 = mp.polylog(3, -0.5)

# Compute the terms difference and apply the negative sign
result = -(term1 - term2)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))