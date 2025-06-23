import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute sinh(4)
sinh_val = mp.sinh(4)

# Multiply by 2 to get 2*sinh(4)
result = 2 * sinh_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))