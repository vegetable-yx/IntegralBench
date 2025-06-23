import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi raised to the power of 3/2
pi_power = mp.pi ** (3/2)

# Compute Gamma(3/4)
gamma_val = mp.gamma(3/4)

# Square the Gamma function value
gamma_squared = gamma_val ** 2

# Divide pi_power by gamma_squared
result = pi_power / gamma_squared

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))