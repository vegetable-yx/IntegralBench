import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Define the value of 'a' (example value, replace with desired input)
a = 1.0

# Calculate the hyperbolic sine integral of a
shi_a = mp.shi(a)

# Compute hyperbolic cosine of a
cosh_a = mp.cosh(a)

# Calculate (cosh(a) - 1) term
numerator = cosh_a - 1

# Divide by 'a' to get the second part of the expression
term = numerator / a

# Combine components to get final result
result = shi_a - term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))