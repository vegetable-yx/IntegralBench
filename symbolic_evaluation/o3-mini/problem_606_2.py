import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Multiply by 3
three_pi_sq = 3 * pi_sq

# Divide by 8
fraction = three_pi_sq / 8

# Subtract 1
result = fraction - 1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))