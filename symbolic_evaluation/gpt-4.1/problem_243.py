import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π squared
pi_sq = mp.pi**2

# Calculate the trigamma function at 1/4
trigamma_value = mp.polygamma(1, mp.mpf(1)/4)

# Compute the expression: (1/8) * [ψ₁(1/4) - π²]
result = (trigamma_value - pi_sq) / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))