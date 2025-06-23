import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of a (here we use a = 1 as an example)
a = mp.mpf(1)

# Calculate cosine of a
cos_a = mp.cos(a)

# Calculate sine of a
sin_a = mp.sin(a)

# Compute the product a * sin_a
a_sin_a = a * sin_a

# Calculate the numerator: 1 - cos(a) - a * sin(a)
numerator = 1 - cos_a - a_sin_a

# Calculate the denominator: a^3
denominator = a**3

# Compute the final result
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))