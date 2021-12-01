# returns the puzzle input
def get_input
  File.open("day_1/input.txt").read.chomp.split
end

# write the solution to the output file
def output(str)
  File.open("day_1/output.txt", "w") do |f|
    f.write str
  end
end

def part1
  recent_depth = 0
  increments = 0
  get_input.each do |current_depth|
    current_depth = current_depth.to_i
    if current_depth > recent_depth and recent_depth != 0
      increments += 1
    end
    recent_depth = current_depth
  end

  output increments
end

def part2
  get_input.each do
  end
end