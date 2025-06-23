import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's constant
pi_val = mp.pi

# Compute π squared
pi_squared = mp.power(pi_val, 2)

# Calculate the term (π²/12)
pi_squared_over_12 = mp.fdiv(pi_squared, 12)

# Compute (1 - π²/12)
inner_expression = mp.fsub(1, pi_squared_over_12)

# Multiply by π and divide by 48 for final result
result = mp.fdiv(mp.fmul(pi_val, inner_expression), 48)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))