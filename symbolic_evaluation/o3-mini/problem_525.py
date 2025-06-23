import mpmath as mp

# Set internal decimal places for high precision calculations
mp.dps = 15

# The analytical expression is a constant: 1/2
# Directly assign the value using mpmath floating-point representation
result = mp.mpf(1) / 2

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))