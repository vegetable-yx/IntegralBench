import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is 1/2
# Compute numerator and denominator as mpmath floats
numerator = mp.mpf(1)
denominator = mp.mpf(2)

# Perform division
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))