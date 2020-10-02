import math

vi = float(input("Enter the initial velocity"))
theta = float(input("Enter the angle at which the projectile was launched in degrees."))
Range = vi**2 * 2*math.sin(theta)/ 9.8

print("Max Range, " Range )
