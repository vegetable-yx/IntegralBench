import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π squared
pi_squared = mp.pi ** 2

# Divide π² by 2
half_pi_squared = pi_squared / 2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply the components together
result = half_pi_squared * ln2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))