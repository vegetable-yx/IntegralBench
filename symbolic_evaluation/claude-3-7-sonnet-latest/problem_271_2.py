import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_squared = mp.power(mp.pi, 2)

# Calculate pi to the fourth power
pi_fourth = mp.power(pi_squared, 2)

# Compute numerator: π^4 - 4π^2
numerator = pi_fourth - 4 * pi_squared

# Divide by 384 to get final result
result = numerator / 384

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))