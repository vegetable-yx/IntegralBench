import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the complex argument: e^(i * 2*pi/3)
theta = 2 * mp.pi / 3
z = mp.exp(1j * theta)  # Complex exponential

# Compute the dilogarithm (polylog of order 2) at z
li2_val = mp.polylog(2, z)

# Extract the real part
real_part = mp.re(li2_val)

# Multiply by -2
result = -2 * real_part

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))