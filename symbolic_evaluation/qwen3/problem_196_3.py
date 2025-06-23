import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate each term of the expression separately
# Term 1: (π * √3) / 8
term1 = (mp.pi * mp.sqrt(3)) / 8

# Term 2: π² / 18 (to be subtracted)
term2 = (mp.pi ** 2) / 18

# Term 3: ln(3) / 16
term3 = mp.log(3) / 16

# Combine the terms: π√3/8 - π²/18 + ln(3)/16
result = term1 - term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))