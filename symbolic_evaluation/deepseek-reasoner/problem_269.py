import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate each term of the expression separately
pi_cubed = mp.pi ** 3
term1 = pi_cubed / 288

term2 = mp.pi / 32

sqrt3 = mp.sqrt(3)
term3 = (mp.pi * sqrt3) / 48

# Combine all terms according to the formula: π³/288 - π/32 + π√3/48
result = term1 - term2 + term3

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))