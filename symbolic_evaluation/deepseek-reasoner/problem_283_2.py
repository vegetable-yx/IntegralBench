import mpmath as mp
mp.dps = 15

# Calculate Ti_2(2) using polylogarithms for inverse tangent integral
term1 = mp.polylog(2, 2j)  # Li_2(2i)
term2 = mp.polylog(2, -2j)  # Li_2(-2i)
ti2_imag = (term1 - term2) / (2j)  # Extract real part from imaginary components
result = 0.5 * ti2_imag  # Multiply by 1/2 from original expression

print(mp.nstr(result, n=10))