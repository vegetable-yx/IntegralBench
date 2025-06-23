import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate e (base of natural logarithm)
e = mp.e

# Calculate 1/e term
inv_e = 1 / e

# Compute (e - 1/e)
e_minus_inve = e - inv_e

# Multiply by sqrt(2)
result = mp.sqrt(2) * e_minus_inve

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))