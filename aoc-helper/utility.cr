require "./day"

def get_puzzle_dirs
  Dir.children(".").select(/^day_/)
end

def get_python_code(day : Day) : String
  input = day.solution.split "\n"
  i = 0
  beginning = 0
  ending = 0
  input.each do |line|
    if line.includes? "def part1"
      puts i
      beginning = i
    elsif line.includes? "if __main__"
      puts i
      ending = i - 1
    end
    i += 1
  end
  puts beginning, ending
  input[beginning..ending].join "\n"
end

def generate_readme(day : Day)
  readme = "# Day 1" # {day.day}"
  readme += "## Code\n```#{day.filetype}\n#{get_python_code(day)}\n```\n"
  readme += "## Input\n```\n#{day.readable_input}\n```"
  readme += "## Output\n```\n#{day.output}\n```"
end

s = Day.new "day_1", "py"
puts generate_readme(s)
