import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi squared
pi_sq = mp.pi**2

# Multiply by 3
three_pi_sq = 3 * pi_sq

# Divide by 4 to get the final result
result = three_pi_sq / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))