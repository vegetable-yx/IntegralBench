import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute fundamental constants
sqrt_pi = mp.sqrt(mp.pi)  # Square root of pi
gamma_const = mp.euler  # Euler-Mascheroni constant
ln2 = mp.log(2)  # Natural logarithm of 2

# Compute denominator: 2^(1/4)
denominator = mp.power(2, 0.25)  # Fourth root of 2

# Compute angle pi/8 (22.5 degrees)
angle = mp.pi / 8

# Compute trigonometric values for pi/8
sin_pi8 = mp.sin(angle)  # sin(π/8)
cos_pi8 = mp.cos(angle)  # cos(π/8)

# Compute the expression inside the brackets
gamma_plus_2ln2 = gamma_const + 2 * ln2  # γ + 2ln2
term1 = gamma_plus_2ln2 * sin_pi8  # (γ + 2ln2) * sin(π/8)
term2 = (mp.pi / 2) * cos_pi8  # (π/2) * cos(π/8)
bracket = term1 - term2  # Combined bracket expression

# Compute the full expression
result = (sqrt_pi / denominator) * bracket

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))