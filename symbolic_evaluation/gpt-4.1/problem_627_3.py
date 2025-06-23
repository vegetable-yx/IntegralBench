import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Euler's constant (γ)
euler_gamma = mp.euler

# Compute π/4
pi_over_4 = mp.pi / 4

# Compute the constant term 1/2
half = mp.mpf(1)/2

# Combine terms: γ - π/4 + 1/2
result = euler_gamma - pi_over_4 + half

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))