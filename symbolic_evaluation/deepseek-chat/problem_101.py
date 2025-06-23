import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# First term: π² / 72
term1 = pi_squared / 72

# Compute arcsin(1/4)
arcsin_val = mp.asin(1/4)

# Square the arcsin value
arcsin_squared = arcsin_val ** 2

# Second term: [arcsin(1/4)]² / 2
term2 = arcsin_squared / 2

# Final result: term1 - term2
result = term1 - term2

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))