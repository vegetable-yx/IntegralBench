import mpmath as mp

# Set internal decimal precision to 15 to ensure 10 decimal places in output
mp.dps = 15

# Define numerator and denominator using mpmath types
numerator = mp.mpf(128)
denominator = mp.mpf(153)

# Compute the fraction
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))