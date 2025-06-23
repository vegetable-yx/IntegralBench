import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Calculate the arguments for the error functions
arg1 = mp.sqrt(3) / 2
arg2 = 1 / (2 * mp.sqrt(3))

# Compute the error function values
erf_val1 = mp.erf(arg1)
erf_val2 = mp.erf(arg2)

# Compute the difference of the error functions
diff_erf = erf_val1 - erf_val2

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * diff_erf

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))