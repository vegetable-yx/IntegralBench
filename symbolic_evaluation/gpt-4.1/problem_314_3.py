import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute ζ(3) using mpmath's zeta function
zeta_3 = mp.zeta(3)

# Multiply by 7/8
product = (7/8) * zeta_3

# Apply the negative sign
result = -product

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))