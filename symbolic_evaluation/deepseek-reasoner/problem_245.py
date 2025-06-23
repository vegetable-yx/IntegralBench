import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Square π
pi_squared = mp.power(pi_val, 2)

# Calculate numerator (7 * π²)
numerator = mp.fmul(7, pi_squared)

# Calculate final result (7π²/256)
result = mp.fdiv(numerator, 256)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))