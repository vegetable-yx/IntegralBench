import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute e^{-2}
exp_neg2 = mp.exp(-2)

# Compute (1 - e^{-2})
one_minus_exp = 1 - exp_neg2

# Compute pi/2
pi_over_2 = mp.pi / 2

# Multiply to get final result: (pi/2) * (1 - e^{-2})
result = pi_over_2 * one_minus_exp

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))