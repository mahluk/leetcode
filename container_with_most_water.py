#!/usr/local/bin/python3.7

def maxArea(height):
	"""
	:type height: List[int]
	:rtype: int
	"""
	max_area = 0

	for i,h in enumerate(height):
		for j,r in enumerate(height[i+1:],i+1):
			area = abs(i - j) * min(h,r)
			max_area = area if area > max_area else max_area
		
	return max_area

if __name__ == '__main__':
	a = [1,8,6,2,5,4,8,3,7]
	print(maxArea(a))
