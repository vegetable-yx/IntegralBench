import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute hyperbolic functions at 5
sinh_5 = mp.sinh(5)
cosh_5 = mp.cosh(5)

# Calculate individual terms in the numerator
term_55sinh = 55 * sinh_5
term_25cosh = 25 * cosh_5

# Combine terms and divide by 4
numerator = term_55sinh - term_25cosh
result = numerator / 4

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))