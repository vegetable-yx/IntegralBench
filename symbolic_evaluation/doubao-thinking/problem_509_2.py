import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 2π/3
term1 = (2 * mp.pi) / 3

# Calculate 4√3
term2 = 4 * mp.sqrt(3)

# Sum the terms for final result
result = term1 + term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))