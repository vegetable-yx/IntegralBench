import mpmath as mp
mp.dps = 15  # Assign the exact integer solution as a_mpmath floating-point number
result = mp.mpf(4)

print(mp.nstr(result, n=10))