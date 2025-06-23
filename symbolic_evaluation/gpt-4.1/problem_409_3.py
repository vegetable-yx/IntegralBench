import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Evaluate the antiderivative at the upper limit (x=1)
term1_1 = -0.5 * mp.log(1**2 + 1)     # -0.5 * ln(1^2 + 1) = -0.5*ln(2)
term2_1 = 0.5 * mp.log(1**2 - 2*1 + 2) # 0.5 * ln(1 - 2 + 2) = 0.5*ln(1) = 0
term3_1 = mp.atan(1 - 1)               # atan(0) = 0
F1 = term1_1 + term2_1 + term3_1       # F(1) = -0.5*ln(2)

# Evaluate the antiderivative at the lower limit (x=0)
term1_0 = -0.5 * mp.log(0**2 + 1)     # -0.5 * ln(1) = 0
term2_0 = 0.5 * mp.log(0**2 - 2*0 + 2) # 0.5 * ln(2)
term3_0 = mp.atan(0 - 1)               # atan(-1) = -π/4
F0 = term1_0 + term2_0 + term3_0       # F(0) = 0.5*ln(2) - π/4

# Compute the definite integral (F(1) - F(0))
integral_val = F1 - F0

# Compute the full expression: π/4 - integral
result = mp.pi / 4 - integral_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))