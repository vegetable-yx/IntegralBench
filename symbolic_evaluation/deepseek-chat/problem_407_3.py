import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the first argument for erf: sqrt(3)/2
arg1 = mp.sqrt(3) / 2

# Calculate the second argument for erf: 1/(2*sqrt(3))
arg2 = 1 / (2 * mp.sqrt(3))

# Evaluate erf at the first argument
erf1 = mp.erf(arg1)

# Evaluate erf at the second argument
erf2 = mp.erf(arg2)

# Compute the difference between the two erf values
diff_erf = erf1 - erf2

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * diff_erf

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))