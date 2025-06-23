import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Compute the argument for the arcsine: sqrt(3)/8
arg = mp.sqrt(3) / 8

# Compute the arcsine of the argument
asin_val = mp.asin(arg)

# Multiply by pi/6
term1 = (mp.pi / 6) * asin_val

# Compute the square root of 61
sqrt61 = mp.sqrt(61)

# Divide by 64 to get the second term
term2 = sqrt61 / 64

# Sum the two terms
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))