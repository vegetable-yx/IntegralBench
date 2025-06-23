import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate modified Bessel functions of the first kind
I0 = mp.besseli(0, 2)  # I_0(2)
I1 = mp.besseli(1, 2)  # I_1(2)

# Calculate modified Struve functions
L_minus1 = mp.struvel(-1, 2)  # L_{-1}(2)
L0 = mp.struvel(0, 2)         # L_0(2)

# Compute individual terms from the expression
term1 = 2 * I0 * L_minus1    # 2*I0(2)*L_{-1}(2)
term2 = 2 * I1 * L0          # 2*I1(2)*L_0(2)
term3 = -I0                  # -I0(2)
term4 = I1                   # I1(2)

# Sum all terms inside the brackets
bracket_sum = term1 + term2 + term3 + term4

# Multiply by pi/4 to get the final result
result = (mp.pi / 4) * bracket_sum

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))