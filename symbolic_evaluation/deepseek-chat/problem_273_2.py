import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate each term of the expression separately

# Term 1: π² / 96
term1 = mp.power(mp.pi, 2) / 96

# Term 2: π / 24
term2 = mp.pi / 24

# Term 3: -π√2 / 48
term3 = -mp.pi * mp.sqrt(2) / 48

# Term 4: ln(1 + √2) / 12
# First compute the argument: 1 + √2
arg = 1 + mp.sqrt(2)
term4 = mp.log(arg) / 12

# Sum all terms to get the result
result = term1 + term2 + term3 + term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))