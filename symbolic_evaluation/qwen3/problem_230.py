import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi to the fourth power
pi_fourth = mp.power(mp.pi, 4)

# Divide by 1440
result = pi_fourth / 1440

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))