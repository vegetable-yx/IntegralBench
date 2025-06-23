import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator and denominator as mpmath floats
numerator = mp.mpf(-2023)
denominator = mp.mpf(2022)

# Perform the division to compute the result
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))