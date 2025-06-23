import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π^4
pi_power4 = mp.pi ** 4

# Compute numerator: 35 * π^4
numerator = 35 * pi_power4

# Compute final result by dividing numerator by 41472
result = numerator / 41472

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))