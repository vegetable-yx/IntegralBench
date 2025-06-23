import mpmath as mp

# Set the internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate pi squared: π^2
pi_squared = mp.pi ** 2

# Divide by 4 to get the result: π^2 / 4
result = pi_squared / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))