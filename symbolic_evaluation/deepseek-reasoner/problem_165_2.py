import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate exponential term e^(-2)
exp_term = mp.exp(-2)

# Calculate the (1 - e^(-2)) component
one_minus_exp = 1 - exp_term

# Multiply by 1/2π
pi_half = mp.pi / 2
result = pi_half * one_minus_exp

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))