import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Calculate π squared
pi_squared = mp.power(pi_val, 2)

# Calculate π²/2 term
term1 = mp.fdiv(pi_squared, 2)

# Final result calculation: π²/2 - π
result = mp.fsub(term1, pi_val)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))