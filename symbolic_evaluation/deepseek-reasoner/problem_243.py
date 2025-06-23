import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π squared
pi_squared = mp.power(pi_value, 2)

# Multiply by 7 to get 7π²
seven_pi_squared = mp.fmul(7, pi_squared)

# Divide by 8 to get the final result
result = mp.fdiv(seven_pi_squared, 8)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))