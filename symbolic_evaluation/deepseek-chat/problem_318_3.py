import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate e^{-2}
exp_neg2 = mp.exp(-2)

# Compute the factor (1 - e^{-2})
factor = 1 - exp_neg2

# Compute π/2
pi_over_2 = mp.pi / 2

# Multiply to get the final result: (π/2) * (1 - e^{-2})
result = pi_over_2 * factor

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))