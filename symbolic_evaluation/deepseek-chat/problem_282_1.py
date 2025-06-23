import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Step 1: Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Step 2: Compute the hyperbolic cosine of 2
cosh_2 = mp.cosh(2)

# Step 3: Multiply the results to get the final value
result = sqrt_pi * cosh_2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))