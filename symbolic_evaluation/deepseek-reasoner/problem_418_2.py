import mpmath as mp
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Compute the Riemann zeta function value at 2 (π²/6)
term = pi_squared / 6

# Subtract 1 to get the final result
result = term - 1

print(mp.nstr(result, n=10))