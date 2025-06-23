import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/2
half_pi = mp.pi / 2

# Retrieve Euler's constant (γ)
euler_gamma = mp.euler

# Compute the result: π/2 - γ
result = half_pi - euler_gamma

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))