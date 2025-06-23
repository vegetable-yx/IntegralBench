import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate e^(-2 using mpmath's exponential function)
exp_neg2 = mp.exp(-2)

# Calculate (1 - e^(-2))
one_minus_exp = 1 - exp_neg2

# Multiply by π/2 to get the final result
result = (mp.pi / 2) * one_minus_exp

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))