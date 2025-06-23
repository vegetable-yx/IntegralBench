import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π/2 using mpmath's constant
pi_half = mp.pi / 2

# Subtract 1 from π/2
result = pi_half - 1

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))