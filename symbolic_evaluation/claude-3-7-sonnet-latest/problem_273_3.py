import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate each term of the expression separately
# Term1: π^3 / 64
pi_cubed = mp.pi ** 3
term1 = pi_cubed / 64

# Term2: (4π - π^2) * ln(2) / 32
# First compute the coefficient (4π - π^2)
coeff = 4 * mp.pi - mp.pi ** 2
# Multiply by ln(2) and divide by 32
term2 = (coeff * mp.log(2)) / 32

# Term3: 3πG / 16 (where G is Catalan's constant)
# This term is subtracted, so we compute it as positive
term3 = (3 * mp.pi * mp.catalan) / 16

# Combine the terms: term1 + term2 - term3
result = term1 + term2 - term3

# Print the final result rounded to exactly 10 decimal places
print(mp.nstr(result, n=10))