import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Compute the constant 3/2
three_halves = mp.mpf(3)/2

# Compute the expression inside the brackets: ln2 - 3/2
bracket_term = ln2 - three_halves

# Multiply by pi/2: (pi/2) * bracket_term
result = (mp.pi / 2) * bracket_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))