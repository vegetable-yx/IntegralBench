import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate pi cubed
pi_cubed = mp.pi ** 3

# Divide by 24 to get the final result
result = pi_cubed / 24

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))