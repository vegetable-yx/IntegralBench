import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the numerator as an mpmath floating-point number
numerator = mp.mpf(2)

# Define the denominator as an mpmath floating-point number
denominator = mp.mpf(5)

# Compute the result of the fraction 2/5
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))