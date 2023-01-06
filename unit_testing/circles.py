from math import pi


def calc_area(r):
	"""
	Calculates the area of a circle.
	"""
	if type(r) not in [int, float]:
		raise TypeError("The radius must be a non-negative real number.")

	if r < 0:
		raise ValueError("The radius cannot be negative.")

	return pi*(r**2)

# # Test function
# radii = [2, 0, -3, 2 + 5j, True, "radius"]
# message = "Area of the cicles with r = {radius} is {area}."

# for r in radii:
# 	a = calc_area(r)
# 	print(message.format(radius=r, area=a))
