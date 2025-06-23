import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi squared
pi_sq = mp.power(mp.pi, 2)

# Multiply by 7: 7 * pi^2
seven_pi_sq = 7 * pi_sq

# Subtract 16: (7 * pi^2 - 16)
inner_expr = seven_pi_sq - 16

# Multiply by 32: 32 * (7 * pi^2 - 16)
numerator = 32 * inner_expr

# Divide by 315 to get the final result
result = numerator / 315

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))