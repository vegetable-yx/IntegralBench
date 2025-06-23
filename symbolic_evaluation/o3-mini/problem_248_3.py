import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant square root of 5
sqrt5 = mp.sqrt(5)

# Compute the argument for the first dilogarithm: (√5 - 1)/4
arg1 = (sqrt5 - 1) / 4

# Compute the argument for the second dilogarithm: -(√5 + 1)/4
arg2 = -(sqrt5 + 1) / 4

# Compute the argument for the logarithm: (3 + √5)/2
arg3 = (3 + sqrt5) / 2

# Calculate the first term: 8 * Li₂((√5 - 1)/4)
term1 = 8 * mp.polylog(2, arg1)

# Calculate the second term: 8 * Li₂(-(√5 + 1)/4)
term2 = 8 * mp.polylog(2, arg2)

# Calculate the third term: π * ln((3 + √5)/2)
term3 = mp.pi * mp.log(arg3)

# Combine terms: (term1 - term2 - term3) / 16
result = (term1 - term2 - term3) / 16

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))