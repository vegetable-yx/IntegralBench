import mpmath as mp

# Set internal precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate pi squared
pi_sq = mp.power(mp.pi, 2)

# Divide by 128
result = pi_sq / 128

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))