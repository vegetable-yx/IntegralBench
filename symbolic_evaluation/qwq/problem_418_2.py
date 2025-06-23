import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π squared
pi_squared = mp.power(pi_value, 2)

# Divide π² result by 6
pi_squared_over_6 = mp.fdiv(pi_squared, 6)

# Subtract 1 from the previous result to get final value
result = mp.fsub(pi_squared_over_6, 1)

# Print the final value with 10 decimal places precision
print(mp.nstr(result, n=10))