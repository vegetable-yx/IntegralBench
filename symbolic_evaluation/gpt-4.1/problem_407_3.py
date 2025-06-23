import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the argument for the first error function: sqrt(3)/2
arg1 = mp.sqrt(3) / 2

# Compute erf(sqrt(3)/2)
erf1 = mp.erf(arg1)

# Calculate the argument for the second error function: 1/(2*sqrt(3))
arg2 = 1 / (2 * mp.sqrt(3))

# Compute erf(1/(2*sqrt(3)))
erf2 = mp.erf(arg2)

# Compute the difference of the two error functions
diff = erf1 - erf2

# Multiply by pi/2
result = (mp.pi / 2) * diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))