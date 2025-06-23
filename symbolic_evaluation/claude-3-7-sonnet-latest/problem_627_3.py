import mpmath as mp

# Set internal decimal places for calculations
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Retrieve Euler-Mascheroni constant γ
gamma = mp.euler

# Combine the terms: π/4 + γ
result = pi_over_4 + gamma

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))