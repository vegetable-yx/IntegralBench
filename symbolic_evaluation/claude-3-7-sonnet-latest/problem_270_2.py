import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi^4 and pi^2
pi_squared = mp.power(mp.pi, 2)
pi_fourth = mp.power(mp.pi, 4)

# Compute the first term: π^4 / 720
term1 = mp.fdiv(pi_fourth, 720)

# Compute the second term: π^2 / 216
term2 = mp.fdiv(pi_squared, 216)

# Combine the terms: term1 - term2
result = mp.fsub(term1, term2)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))