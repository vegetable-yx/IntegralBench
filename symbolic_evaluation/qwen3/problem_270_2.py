import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate each term of the expression separately
# First term: π^4 / 49
pi_4 = mp.pi**4
term1 = pi_4 / 49

# Second term: 5π^3 / 1024 (subtracted)
pi_3 = mp.pi**3
term2 = (5 * pi_3) / 1024

# Third term: π√3 / 15
sqrt3 = mp.sqrt(3)
term3 = (mp.pi * sqrt3) / 15

# Fourth term: 13/512 (subtracted)
term4 = mp.mpf(13)/512

# Combine all terms
result = term1 - term2 + term3 - term4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))