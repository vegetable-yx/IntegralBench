import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π^4
pi_power4 = mp.pi ** 4

# Calculate numerator (31 * π^4)
numerator = 31 * pi_power4

# Calculate final result by dividing numerator by 13440
result = numerator / 13440

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))