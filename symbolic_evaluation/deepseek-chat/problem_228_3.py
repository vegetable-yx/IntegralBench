import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the two terms in the closed-form expression
term1 = mp.power(mp.pi, 3) / 48  # pi^3 / 48
term2 = (mp.pi * mp.power(mp.log(2), 2)) / 8  # (pi * ln(2)^2) / 8

# Sum the terms to get the final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))