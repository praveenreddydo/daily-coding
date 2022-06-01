# You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.


# Solution: 
# we run level after level, starting by level 1 and finishing at last level, the highest wall
# for each level we run through the array 
# when we discover a wall we can start keeping bucket of water
# when we get en empty space we fill one bucket of water
# when we find another wall we bank, all water in "waiting list" 
# will indeed be kept between 2 walls 
def get_water_stored(arr)
  max = 1
  j = 1
  validated = 0
  while j <= max 
    p "j: #{j}, max:#{max}"
    waiting_list = 0
    start_filling = false
    arr.each do |wall|  
      max = wall if wall > 0
      if wall >= j
        validated += waiting_list
        waiting_list = 0
        start_filling = true
      elsif start_filling
        waiting_list += 1
      end
      p "wall: #{wall} - wl #{waiting_list} - valid: #{validated}"
    end
    j += 1
  end
  validated
end

get_water_stored([3,0,1]) == 1
get_water_stored([1,0,3]) == 1
get_water_stored([3,0,1,3,0,5]) == 8
get_water_stored([3,0,0]) == 0
get_water_stored([0,1,3,1,0]) == 0
