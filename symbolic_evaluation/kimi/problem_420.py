import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the value inside the outermost square root: (-1 + sqrt(5)) / 2
sqrt5 = mp.sqrt(5)
numerator = -1 + sqrt5
fraction = numerator / 2

# Compute the square root of that fraction
inner_sqrt = mp.sqrt(fraction)

# This inner_sqrt is sin(theta) where theta = arcsin(inner_sqrt)
sin_theta = inner_sqrt

# Compute cos(theta) = sqrt(1 - sin^2(theta)) [since theta in [0, pi/2]]
cos_theta = mp.sqrt(1 - sin_theta**2)

# Calculate the two terms: 1 - cos(theta) and ln(sin(theta))
term1 = 1 - cos_theta
term2 = mp.log(sin_theta)  # natural logarithm

# Combine the terms: 1 - cos(theta) - ln(sin(theta))
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))