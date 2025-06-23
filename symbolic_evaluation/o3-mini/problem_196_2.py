import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the complex exponentials for e^(iπ/3) and e^(-iπ/3)
z1 = mp.exp(1j * mp.pi / 3)  # e^(iπ/3)
z2 = mp.exp(-1j * mp.pi / 3) # e^(-iπ/3)

# Compute the dilogarithms for each complex point
L1 = mp.polylog(2, z1)  # Li₂(e^(iπ/3))
L2 = mp.polylog(2, z2)  # Li₂(e^(-iπ/3))

# Compute the expression: (π² - 6*L1 - 6*L2) / 48
pi_sq = mp.pi ** 2
combined_dilog = 6 * L1 + 6 * L2
numerator = pi_sq - combined_dilog
result = numerator / 48

# Extract the real part to eliminate any residual imaginary noise (the expression is real-valued)
result_real = mp.re(result)

# Print the result to 10 decimal places
print(mp.nstr(result_real, n=10))