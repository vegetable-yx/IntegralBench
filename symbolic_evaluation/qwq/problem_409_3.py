import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π/2
pi_half = mp.pi / 2

# Calculate natural logarithm of 2
ln_two = mp.log(2)

# Compute final result by subtraction
result = pi_half - ln_two

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))