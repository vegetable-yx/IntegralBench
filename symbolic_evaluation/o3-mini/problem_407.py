import mpmath as mp

# Set internal decimal places for calculations
mp.dps = 15

# Calculate the arguments for the error functions
sqrt3 = mp.sqrt(3)  # Compute square root of 3
arg1 = sqrt3 / 2    # First argument: √3 / 2
arg2 = 1 / (2 * sqrt3)  # Second argument: 1/(2√3)

# Compute error function values
erf_val1 = mp.erf(arg1)  # erf(√3/2)
erf_val2 = mp.erf(arg2)  # erf(1/(2√3))

# Calculate the difference between error function values
diff_erf = erf_val1 - erf_val2

# Multiply by π/2 to get final result
result = (mp.pi / 2) * diff_erf

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))