import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the numerator as -1 in mpmath format
numerator = mp.mpf(-1)

# Define the denominator as 2022 in mpmath format
denominator = mp.mpf(2022)

# Compute the result: -1 / 2022
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))