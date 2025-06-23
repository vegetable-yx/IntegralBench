import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the input value (replace with desired x value in radians)
x = mp.pi / 4  # Example: compute at x = π/4

# Compute sin(x)
sx = mp.sin(x)

# Compute sin(x)^2 for hypergeometric argument
sx2 = sx**2

# Compute sin(x)^100
sx_100 = sx**100

# Compute the hypergeometric function _2F_1(-50, -50, 3/2, sin(x)^2)
hyp_val = mp.hyp2f1(-50, -50, mp.mpf('3/2'), sx2)

# Compute the main term: - [sin(x)^100 / 101] * hypergeometric value
term = - (sx_100 / 101) * hyp_val

# Result is the computed term (constant C omitted as per typical evaluation)
result = term

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))