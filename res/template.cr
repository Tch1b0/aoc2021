# returns the puzzle input
def get_input : String
  File.read "{{ROOT}}/input.txt"
end

# write the solution to the output file
def output(str : String)
  File.write "{{ROOT}}/output.txt", str
end

# Solution goes here
