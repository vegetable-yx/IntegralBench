import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the exact value of the fraction 1/5
numerator = mp.mpf(1)  # Numerator of the fraction
denominator = mp.mpf(5)  # Denominator of the fraction
result = numerator / denominator  # Compute the division

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))