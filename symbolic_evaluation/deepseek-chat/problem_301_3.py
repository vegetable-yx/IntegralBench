import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi squared
pi_sq = mp.power(mp.pi, 2)

# Divide by 6
frac = pi_sq / 6

# Apply negative sign
result = -frac

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))