import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Define the integrand function
def integrand(theta):
    # Compute sin(theta)
    sin_theta = mp.sin(theta)
    # Compute cos(2*theta)
    cos_2theta = mp.cos(2 * theta)
    # Compute sin(2*theta)
    sin_2theta = mp.sin(2 * theta)
    # Compute ln(sin(theta))
    ln_sin_theta = mp.log(sin_theta)
    # Compute the denominator: 1 + sin^2(2*theta)
    denominator = 1 + sin_2theta**2
    # Return the integrand: cos(2*theta) * ln(sin(theta)) / denominator
    return cos_2theta * ln_sin_theta / denominator

# Perform the numerical integration from 0 to pi/2
integral_result = mp.quad(integrand, [0, mp.pi/2])

# Multiply by the constant factor -4
result = -4 * integral_result

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))