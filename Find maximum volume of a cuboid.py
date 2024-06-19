import math

class Solution:
    def maxVolume(self, perimeter, area):
        part1 = (perimeter - math.sqrt(perimeter ** 2 - 24 * area)) / 12
        part2 = (perimeter / 4) - (2 * part1)
        volume = (part1 ** 2) * part2
        return round(volume, 2)
