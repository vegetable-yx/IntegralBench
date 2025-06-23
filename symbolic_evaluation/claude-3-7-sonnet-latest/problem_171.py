import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate pi squared
pi_sq = mp.power(mp.pi, 2)

# Divide by 12 to get the result
result = pi_sq / 12

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))