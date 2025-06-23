import mpmath as mp

# Set internal decimal precision to 15 digits for calculations
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate e raised to the power of -1
exp_neg1 = mp.exp(-1)

# Multiply the two components together
result = sqrt_pi * exp_neg1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))