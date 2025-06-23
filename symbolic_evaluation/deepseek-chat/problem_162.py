import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters (replace with desired values)
a = 1.0
b = 1.0

# Compute sqrt(a)
sqrt_a = mp.sqrt(a)

# Compute inner term: b * sqrt(a)
inner = b * sqrt_a

# Compute argument for cosh: (b * sqrt(a)) / 2
arg_cosh = inner / 2

# Compute numerator: 2 * pi * cosh(arg_cosh)
numerator = 2 * mp.pi * mp.cosh(arg_cosh)

# Compute denominator: sqrt(b * sqrt(a)) = sqrt(inner)
denominator = mp.sqrt(inner)

# Compute final result: numerator / denominator
result = numerator / denominator

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))