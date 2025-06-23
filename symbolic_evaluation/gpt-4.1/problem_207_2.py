import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute the fourth roots: 10^(1/4) and 2^(1/4)
ten_to_quarter = mp.root(10, 4)
two_to_quarter = mp.root(2, 4)

# Compute the angle for the first sine: arctan(1/3)
atan_val = mp.atan(1/mp.mpf(3))

# Half of the arctan result
half_atan = atan_val / 2

# Compute sin(half_atan)
sin_half_atan = mp.sin(half_atan)

# Compute sin(pi/8)
sin_pi_eighth = mp.sin(mp.pi / 8)

# Compute the expression inside the brackets: 10^(1/4)*sin(half_atan) - 2^(1/4)*sin(pi/8)
bracket_value = ten_to_quarter * sin_half_atan - two_to_quarter * sin_pi_eighth

# Multiply by 2 * sqrt(pi)
result = 2 * sqrt_pi * bracket_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))