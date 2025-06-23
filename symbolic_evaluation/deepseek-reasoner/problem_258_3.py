import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute exponential term e^(-1/4)
exp_term = mp.exp(-mp.mpf(1)/4)

# Multiply components together
result = 2 * sqrt_pi * exp_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))