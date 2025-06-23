import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate π^2
pi_squared = mp.power(mp.pi, 2)

# Divide by 6 to get π^2/6
pi_squared_over_six = pi_squared / 6

# Subtract 1 to get final result
result = pi_squared_over_six - 1

# Print result to 10 decimal places
print(mp.nstr(result, n=10))