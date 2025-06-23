import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the arguments for the error functions
arg1 = mp.sqrt(3) / 2
arg2 = 1 / (2 * mp.sqrt(3))

# Compute the error function values
erf1 = mp.erf(arg1)
erf2 = mp.erf(arg2)

# Compute the difference between the two erf values
diff_erf = erf1 - erf2

# Multiply by pi/2
result = (mp.pi / 2) * diff_erf

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))