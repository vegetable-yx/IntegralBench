import mpmath as mp

# Set the decimal places for internal precision to 15 to ensure 10 decimal places accuracy
mp.dps = 15

# Compute gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Raise gamma(1/4) to the 4th power
gamma4 = gamma_val**4

# Compute pi^3
pi_cubed = mp.pi**3

# Multiply by 32 to get the denominator
denominator = 32 * pi_cubed

# Divide gamma^4 by the denominator
result = gamma4 / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))