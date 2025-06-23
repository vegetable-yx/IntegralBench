import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant pi
pi_val = mp.pi

# Compute the numerator: π + 2
numerator = pi_val + 2

# Compute the denominator: 8
denominator = 8

# Compute the fraction: (π + 2)/8
fraction = numerator / denominator

# Apply the negative sign: -(π + 2)/8
result = -fraction

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))