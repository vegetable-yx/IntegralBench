import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Multiply by 4 to get 4 * ln(2)
term1 = 4 * ln2

# Get the constant pi
pi_val = mp.pi

# Add pi to term1: (4 * ln(2) + pi)
inner_sum = term1 + pi_val

# Multiply by pi: pi * (4*ln(2) + pi)
numerator = pi_val * inner_sum

# Divide by 32: numerator / 32
fraction = numerator / 32

# Apply the negative sign to get the final result
result = -fraction

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))