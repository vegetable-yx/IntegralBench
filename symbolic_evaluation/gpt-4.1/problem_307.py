Based on the analysis, the integral simplifies to a closed-form expression involving Catalan's constant and logarithmic terms. Here's the Python code to compute it:

import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Get Catalan's constant
catalan_constant = mp.catalan

# Get pi constant
pi = mp.pi

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Compute term: 2 * Catalan's constant
term1 = 2 * catalan_constant

# Compute term: (pi/2) * ln(2)
term2 = (pi / 2) * ln2

# Sum both terms to get final result
result = term1 + term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))