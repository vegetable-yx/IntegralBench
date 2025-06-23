import mpmath as mp

mp.dps = 15  # Set internal decimal precision

# Calculate 3π/16 using exact symbolic components
pi_term = mp.pi  # Get π constant from mpmath
numerator = 3 * pi_term
result = numerator / 16  # Final division

print(mp.nstr(result, n=10))