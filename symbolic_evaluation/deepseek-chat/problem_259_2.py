import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π
pi_val = mp.pi

# Compute π squared
pi_squared = mp.power(pi_val, 2)

# Calculate π²/4
term1 = mp.fdiv(pi_squared, 4)

# Subtract π from the previous term
result = mp.fsub(term1, pi_val)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))