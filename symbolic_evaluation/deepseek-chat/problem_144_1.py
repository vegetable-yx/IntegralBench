import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the integral using the known closed-form expression
# Expression: (π/16) * [I_1(2) * L_0(2) - I_0(2) * L_1(2)]
# Where I_v is the modified Bessel function of the first kind
# and L_v is the modified Struve function

# Step 1: Compute I_1(2) - modified Bessel function of first kind order 1 at 2
bessel_i1_2 = mp.besseli(1, 2)

# Step 2: Compute L_0(2) - modified Struve function of order 0 at 2
struve_l0_2 = mp.struvel(0, 2)

# Step 3: Compute I_0(2) - modified Bessel function of first kind order 0 at 2
bessel_i0_2 = mp.besseli(0, 2)

# Step 4: Compute L_1(2) - modified Struve function of order 1 at 2
struve_l1_2 = mp.struvel(1, 2)

# Step 5: Compute the expression inside the brackets
inner_expr = bessel_i1_2 * struve_l0_2 - bessel_i0_2 * struve_l1_2

# Step 6: Multiply by π/16
result = (mp.pi / 16) * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))