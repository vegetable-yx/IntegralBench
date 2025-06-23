import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the golden ratio (1 + sqrt(5))/2
golden_ratio = (1 + mp.sqrt(5)) / 2

# Compute the natural logarithm of the golden ratio
log_golden = mp.log(golden_ratio)

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * log_golden

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))