import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the natural logarithm of 2
ln2_val = mp.log(2)

# Compute the constant pi divided by 2
half_pi = mp.pi / 2

# Multiply the results to obtain the final value
result = half_pi * ln2_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))