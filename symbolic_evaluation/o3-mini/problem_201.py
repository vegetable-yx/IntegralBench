import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Calculate Bessel function J0 at 1
j0_1 = mp.besselj(0, 1)

# Calculate Bessel function J1 at 1
j1_1 = mp.besselj(1, 1)

# Calculate Struve function H_{-1} at 1
h_minus1_1 = mp.struveh(-1, 1)

# Calculate Struve function H_0 at 1
h0_1 = mp.struveh(0, 1)

# Compute the expression inside the brackets: J0(1)*H_{-1}(1) - J1(1)*H_0(1)
inner_expr = j0_1 * h_minus1_1 - j1_1 * h0_1

# Multiply by pi to get the final result
result = mp.pi * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))