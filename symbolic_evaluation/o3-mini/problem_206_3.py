import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute constants and components
gamma = mp.euler  # Euler-Mascheroni constant
ln2 = mp.log(2)   # Natural logarithm of 2
ln10 = mp.log(10) # Natural logarithm of 10
pi_over_8 = mp.pi / 8  # π/8 in radians

# Compute the coefficient: √π / (2^{1/4})
sqrt_pi = mp.sqrt(mp.pi)
two_power = mp.power(2, mp.mpf('0.25'))  # 2^(1/4)
coefficient = sqrt_pi / two_power

# Compute the expression inside the brackets:
# term1 = (γ + 3*ln2 - 0.5*ln10) * cos(π/8)
inner_const = gamma + 3*ln2 - 0.5*ln10
cos_term = mp.cos(pi_over_8)
term1 = inner_const * cos_term

# term2 = arctan(3) * sin(π/8)
atan3 = mp.atan(3)
sin_term = mp.sin(pi_over_8)
term2 = atan3 * sin_term

# Combine terms: brackets = term1 - term2
brackets = term1 - term2

# Final result: coefficient multiplied by brackets
result = coefficient * brackets

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))