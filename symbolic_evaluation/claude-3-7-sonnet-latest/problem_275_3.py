import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute sinh(3) using mpmath
sinh_val = mp.sinh(3)

# Multiply by 3
numerator = 3 * sinh_val

# Divide by 2 to get the result
result = numerator / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))