import mpmath as mp

mp.dps = 15  # Compute each component of the expression

term1 = mp.pi**3 / 486

ln2 = mp.ln(2)
term2 = mp.pi * ln2**2 / 6

cl2_pi3 = mp.clsin(2, mp.pi/3)
term3 = - (ln2 / 2) * cl2_pi3

# Compute the integral part using series expansion
I_part1 = (ln2**2) * (mp.pi / 6)
I_part2 = ln2 * cl2_pi3

N = 200  # Number of terms for series convergence
S = mp.mpf(0)

for k in range(1, N+1):
    for m in range(1, N+1):
        if k == m:
            integral = mp.pi/12 + mp.sin(2*k*mp.pi/3)/(8*k)
            term = (1 / k**2) * integral
        else:
            integral_part1 = mp.sin((k + m)*mp.pi/3) / (4*(k + m))
            integral_part2 = mp.sin((k - m)*mp.pi/3) / (4*(k - m))
            term = (1/(k*m)) * (integral_part1 + integral_part2)
        S += term

I = I_part1 + I_part2 + S

# Sum all terms for the final result
result = term1 + term2 + term3 + I

print(mp.nstr(result, n=10))