import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate the constant π
pi_val = mp.pi

# Compute π divided by 2
pi_over_2 = pi_val / 2

# Compute the natural logarithm of (π/2)
result = mp.log(pi_over_2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))