import mpmath as mp

mp.dps = 15  # Compute pi squared
pi_squared = mp.pi ** 2

# Compute the argument for the complete elliptic integral of the second kind
a = mp.mpf('0.5')  # Example value for 'a' (replace with actual input value)
argument = a / 2

# Calculate the complete elliptic integral of the second kind E(argument)
E_value = mp.ellipe(argument)

# Combine components to compute final result
result = (pi_squared / 2) * E_value

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))