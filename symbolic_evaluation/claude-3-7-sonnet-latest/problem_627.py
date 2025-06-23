import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Calculate (1/2) * ln(2)
half_ln2 = 0.5 * ln2

# Get Euler-Mascheroni constant γ
gamma = mp.euler

# Combine terms: π/4 - (1/2)ln(2) + γ
result = pi_over_4 - half_ln2 + gamma

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))