import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the first part: 0.5*(I_0(2) - I_2(2))
term_i0 = mp.besseli(0, 2)
term_i2 = mp.besseli(2, 2)
part_bessel = 0.5 * (term_i0 - term_i2)

# Define the integrand for the integral part
def integrand(x):
    return mp.besseli(1, x) * mp.besselk(1, 2 - x)

# Compute the integral from 0 to 2
integral_part = mp.quad(integrand, [0, 2])

# Combine both parts for final result
result = part_bessel - integral_part

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))