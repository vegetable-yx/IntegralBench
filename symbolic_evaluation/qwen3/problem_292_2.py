import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate pi cubed: π^3
pi_cubed = mp.pi ** 3

# Divide by 4 to get the result: π^3 / 4
result = pi_cubed / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))