import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate e^{-2}
exp_term = mp.exp(-2)

# Subtract from 1: (1 - e^{-2})
one_minus_exp = 1 - exp_term

# Multiply by pi/2: pi/2 * (1 - e^{-2})
result = (mp.pi / 2) * one_minus_exp

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))