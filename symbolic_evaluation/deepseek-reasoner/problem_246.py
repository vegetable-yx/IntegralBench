import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π^4
pi_power4 = mp.power(pi_value, 4)

# Calculate numerator: 567 * π^4
numerator = 567 * pi_power4

# Compute final result by dividing by 32
result = numerator / 32

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))