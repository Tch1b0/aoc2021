# returns the puzzle input
def get_input
  File.open("{{ROOT}}/input.txt").read.chomp
end

# write the solution to the output file
def output(str)
  File.open("{{ROOT}}/output.txt", "w") do |f|
    f.write str
  end
end

# Solution goes here