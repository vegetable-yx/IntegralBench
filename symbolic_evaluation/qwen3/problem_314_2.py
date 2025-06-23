import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Li_3(-1/2)
term1 = mp.polylog(3, -0.5)

# Compute Li_3(1/2)
term2 = mp.polylog(3, 0.5)

# Combine the terms: Li_3(-1/2) - Li_3(1/2)
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))