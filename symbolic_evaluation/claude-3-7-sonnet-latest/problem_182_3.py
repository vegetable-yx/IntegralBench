import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π (pi)
pi_val = mp.pi

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Multiply π and ln(3)
term1 = pi_val * ln3

# Calculate arctangent of 2
atan2 = mp.atan(2)

# Multiply by 2.5 (which is 5/2)
term2 = 2.5 * atan2

# Combine terms: π*ln(3) - 2.5*atan(2) + 1
result = term1 - term2 + 1

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))