import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi = mp.pi

# Compute π squared
pi_squared = mp.power(pi, 2)

# Calculate the first term: π²/12
term1 = pi_squared / 12

# Calculate natural logarithm of 2
log2 = mp.log(2)

# Calculate the second term: (π * log2)/4
term2 = (pi * log2) / 4

# Combine terms to get final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))