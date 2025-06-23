import mpmath as mp

# Set internal precision to 15 decimal places for calculations
mp.dps = 15

# Compute the analytical expression: 1/5
# Break into numerator and denominator for clarity
numerator = mp.mpf(1)
denominator = mp.mpf(5)
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))