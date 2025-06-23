import mpmath as mp
mp.dps = 15  # Compute Bessel function J_1 at 1
j1_value = mp.besselj(1, 1)

# Calculate the integral using the known identity for J_2(2cosθ)cosθ
integral_part = (mp.pi / 2) * (j1_value ** 2)

# Multiply by 1/2 as per the original expression
result = 0.5 * integral_part

# Print the final result with 10 decimal precision
print(mp.nstr(result, n=10))