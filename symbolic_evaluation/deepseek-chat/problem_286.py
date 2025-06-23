import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate π (using mpmath constant)
pi_val = mp.pi

# Calculate π squared divided by 16
term1 = mp.power(pi_val, 2) / 16

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Calculate (π/4) multiplied by ln(2)
term2 = (pi_val / 4) * ln2

# Combine the terms: π²/16 - (π/4)*ln(2)
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))