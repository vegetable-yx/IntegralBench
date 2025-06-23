import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Define numerator and denominator as arbitrary precision floats
numerator = mp.mpf(128)
denominator = mp.mpf(153)

# Compute the fraction
result = numerator / denominator

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))