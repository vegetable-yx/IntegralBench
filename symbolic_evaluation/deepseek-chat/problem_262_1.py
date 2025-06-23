import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Parameters for the hypergeometric function 1F2: 
#   Numerator: [3/2]
#   Denominator: [2, 5/2]
#   Argument: z = -1
a1 = mp.mpf('3/2')  # Numerator parameter 3/2
b1 = mp.mpf(2)      # First denominator parameter
b2 = mp.mpf('5/2')  # Second denominator parameter
z = mp.mpf(-1)      # Argument

# Compute the hypergeometric function value
F_val = mp.hyper([a1], [b1, b2], z)

# The integral expression: \int_0^1 \frac{x J_1(2x)}{\sqrt{1-x^2}} dx = \frac{\pi}{4} \cdot {}_1F_2\left(\frac{3}{2}; 2, \frac{5}{2}; -1\right)
# The original expression is half of this integral
result = (mp.pi / 8) * F_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))