import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator as mpmath floats
numerator = mp.mpf(2023)
denominator = mp.mpf(2022)

# Compute the result: -2023/2022
result = -numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))