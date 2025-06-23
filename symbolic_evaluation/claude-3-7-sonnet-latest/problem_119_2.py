import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute pi squared (π²)
pi_sq = mp.power(mp.pi, 2)

# Multiply by 2
two_pi_sq = 2 * pi_sq

# Divide by 3 to get the result
result = two_pi_sq / 3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))