import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi^(3/2) as pi * sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)
pi_power = mp.pi * sqrt_pi

# Calculate gamma(3/4)
gamma_val = mp.gamma(3/4)

# Square the gamma value
gamma_squared = gamma_val ** 2

# Compute the final result: pi^(3/2) / gamma(3/4)^2
result = pi_power / gamma_squared

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))