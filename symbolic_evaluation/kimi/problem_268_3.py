import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the components of the expression
pi_term = 7 * mp.pi  # Compute 7π
numerator = 21 - pi_term  # Compute (21 - 7π)
coefficient = numerator / 16  # Divide by 16 to get the coefficient
zeta_3 = mp.zeta(3)  # Compute ζ(3)

# Multiply coefficient by ζ(3) to get the final result
result = coefficient * zeta_3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))