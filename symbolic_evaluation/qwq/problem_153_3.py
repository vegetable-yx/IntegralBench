import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π^2
pi_squared = mp.power(mp.pi, 2)

# Divide π^2 by 8
term = mp.fdiv(pi_squared, 8)

# Subtract 1 from the result
result = mp.fsub(term, 1)

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))