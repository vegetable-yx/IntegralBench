import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the value of pi
pi_val = mp.pi

# Compute the Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Calculate the numerator: 28 * pi - 105
numerator = 28 * pi_val - 105

# Divide the numerator by 64
fraction = numerator / 64

# Multiply by zeta(3) to get the final result
result = fraction * zeta_3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))