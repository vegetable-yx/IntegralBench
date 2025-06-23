import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Compute the arguments for the dilogarithms and logarithm
a = (sqrt3 - 1) / 2  # Argument for first dilogarithm (positive)
b = (1 - sqrt3) / 2  # Argument for second dilogarithm (negative)
c = (sqrt3 + 1) / 2  # Argument for the natural logarithm

# Evaluate each term of the expression
# First dilogarithm term: 4 * Li2(a)
term1 = 4 * mp.polylog(2, a)

# Second dilogarithm term: -4 * Li2(b)
term2 = -4 * mp.polylog(2, b)

# Logarithmic term: -3*pi*ln(c)
term3 = -3 * mp.pi * mp.log(c)

# Logarithmic term: pi * ln(2)
term4 = mp.pi * mp.log(2)

# Pi squared term: (2 * pi^2) / 3
term5 = (2 * mp.pi**2) / 3

# Sum all terms and multiply by 1/8
result = (term1 + term2 + term3 + term4 + term5) / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))