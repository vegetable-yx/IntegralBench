import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Define constant parameters as exact mpf values
half = mp.mpf('0.5')
three_halves = mp.mpf('1.5')
one = mp.mpf('1')

# Compute first hypergeometric function: 3F2(1/2, 1/2, 3/2; 1, 3/2; 1/2)
F1 = mp.hyp3f2(half, half, three_halves, one, three_halves, half)

# Compute second hypergeometric function: 3F2(1/2, 1/2, 3/2; 3/2, 3/2; 1/2)
F2 = mp.hyp3f2(half, half, three_halves, three_halves, three_halves, half)

# Calculate the expression inside the brackets: π*F1 - 2*F2
bracket_term = mp.pi * F1 - 2 * F2

# Multiply by 1/4 to get final result
result = bracket_term / 4

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))