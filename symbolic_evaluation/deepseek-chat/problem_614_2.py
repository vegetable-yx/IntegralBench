import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Define the numerator and denominator of the fraction
numerator = 1
denominator = 2

# Calculate the exact fraction: 1/2
result = mp.mpf(numerator) / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))