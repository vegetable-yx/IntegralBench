import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate pi to the fourth power
pi_fourth = mp.pi ** 4

# Divide by 320 to obtain the final result
result = pi_fourth / 320

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))