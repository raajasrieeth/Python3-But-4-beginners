 import math

vi = float(input("Enter the initial velocity"))
theta = float(input("Enter the angle at which the projectile was launched in degrees."))
height = (vi**2 * (math.sin(theta)*math.sin(theta)))/ (2*9.8)

print(height)
