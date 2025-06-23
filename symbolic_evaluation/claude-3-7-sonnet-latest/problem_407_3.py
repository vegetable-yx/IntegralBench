import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute the first argument for erf: sqrt(3)/2
arg1 = mp.sqrt(3) / 2

# Compute the second argument for erf: 1/(2*sqrt(3))
arg2 = 1 / (2 * mp.sqrt(3))

# Calculate error function values
erf_val1 = mp.erf(arg1)
erf_val2 = mp.erf(arg2)

# Compute the difference between erf values
diff_erf = erf_val1 - erf_val2

# Multiply by pi/2 to get final result
result = (mp.pi / 2) * diff_erf

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))