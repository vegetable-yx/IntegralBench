import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the analytical expression: 1/2
# This is a simple fraction that can be evaluated directly
numerator = 1
denominator = 2
result = mp.mpf(numerator) / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))