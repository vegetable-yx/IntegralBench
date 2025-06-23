import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the arguments for the error functions
arg1 = mp.sqrt(3) / 2
arg2 = 1 / (2 * mp.sqrt(3))

# Evaluate the error functions
erf_val1 = mp.erf(arg1)
erf_val2 = mp.erf(arg2)

# Compute the difference between the two error function values
diff_erf = erf_val1 - erf_val2

# Multiply by π/2 to get the final result
result = (mp.pi / 2) * diff_erf

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))