import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the complex argument (1+i)/2
z = mp.mpc(1, 1) / 2

# Compute the trilogarithm Li_3(z)
trilog = mp.polylog(3, z)

# Extract the imaginary part of the trilogarithm
imag_part = mp.im(trilog)

# Compute pi^3
pi_cubed = mp.pi ** 3

# Calculate the expression inside the brackets: pi^3 - 16 * imag_part
inner_expr = pi_cubed - 16 * imag_part

# Multiply by sqrt(2)/8
result = (mp.sqrt(2) / 8) * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))