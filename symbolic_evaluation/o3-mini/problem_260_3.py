import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate Bessel functions of the first kind at x=1
j0 = mp.besselj(0, 1)  # J_0(1)
j1 = mp.besselj(1, 1)  # J_1(1)

# Calculate Struve functions at x=1
h0 = mp.struveh(0, 1)  # \mathbf{H}_0(1)
h1 = mp.struveh(1, 1)  # \mathbf{H}_1(1)

# Compute the expression inside the brackets: J0(1)*H0(1) - J1(1)*H1(1)
inner_term = j0 * h0 - j1 * h1

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * inner_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))