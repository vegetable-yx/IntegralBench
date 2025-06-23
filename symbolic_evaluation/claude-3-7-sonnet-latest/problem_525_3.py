import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# The analytical expression is 1/2
# Represent the fraction exactly using mpmath
result = mp.mpf(1) / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))