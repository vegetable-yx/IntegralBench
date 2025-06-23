import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant 1/4 for repeated use
a = mp.mpf(1)/4

# Compute ln(2)
ln2 = mp.log(2)

# Compute hyperbolic functions
sinh_val = mp.sinh(a)
cosh_val = mp.cosh(a)

# Compute hyperbolic sine integral Shi(1/4)
shi_val = mp.shi(a)

# Compute exponential integrals
ei_pos = mp.ei(a)      # Ei(1/4)
ei_neg = mp.ei(-a)     # Ei(-1/4)

# Compute the terms inside the braces
term1 = 8 * ln2 * sinh_val
term2 = -8 * cosh_val * shi_val
term3 = ei_pos
term4 = -ei_neg

# Sum all terms inside the braces
total_inside = term1 + term2 + term3 + term4

# Multiply by 1/16 to get the final result
result = total_inside / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))