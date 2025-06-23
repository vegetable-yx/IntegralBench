import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the upper limit T = 7 + 5*sqrt(2)
T = 7 + 5 * mp.sqrt(2)

# Compute each term of the integrated expression at upper limit T
term1 = (3/8) * (T ** (4/3))
term2 = (-3/4) * (T ** (-2/3))
term3 = (-3/4) * (T ** (2/3))
term4 = (3/8) * (T ** (-4/3))

# Combine terms and add the lower limit contribution (3/4)
result = (term1 + term2 + term3 + term4) + 3/4

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))