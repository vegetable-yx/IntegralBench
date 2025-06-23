import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate the complex argument: e^(i * 2π/3)
angle = 2 * mp.pi / 3
z = mp.exp(1j * angle)

# Compute the dilogarithm of the complex argument
dilog_val = mp.polylog(2, z)

# Extract the real part of the dilogarithm result
real_dilog = mp.re(dilog_val)

# Multiply the real part by 2
term1 = 2 * real_dilog

# Compute pi squared
pi_sq = mp.pi**2

# Calculate the constant term: (13/9) * pi^2
term2 = (13 * pi_sq) / 9

# Combine the terms: 2*Re[Li_2] - (13/9)π²
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))