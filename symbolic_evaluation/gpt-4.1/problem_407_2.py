import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Compute the argument for the first error function: sqrt(3)/2
arg1 = sqrt3 / 2

# Compute the argument for the second error function: 1/(2*sqrt(3))
arg2 = 1 / (2 * sqrt3)

# Evaluate the error functions
erf1 = mp.erf(arg1)
erf2 = mp.erf(arg2)

# Calculate the difference of the error functions
diff_erf = erf1 - erf2

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * diff_erf

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))