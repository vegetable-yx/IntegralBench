import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Get Euler's constant (γ)
euler_gamma = mp.euler

# Compute π/4
pi_over_4 = mp.pi / 4

# Calculate the result: γ - π/4
result = euler_gamma - pi_over_4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))