require "./puzzle"

def get_puzzles
  dirs = Dir.children(".").select(/^day_/)
  days = [] of Puzzle
  dirs.each do |dir|
    days.push(Puzzle.new(dir, "py"))
  end
  days
end

def get_python_code(puzzle : Puzzle) : String
  input = puzzle.solution.split "\n"
  i = 0
  beginning = 0
  ending = 0
  input.each do |line|
    if line =~ /def part1/
      beginning = i
    elsif line =~ /if __name__/
      ending = i - 1
    end
    i += 1
  end
  input[beginning..ending].join "\n"
end

def generate_readme(puzzle : Puzzle)
  readme = "# Day #{puzzle.day}\n"
  readme += "### [Task](https://adventofcode.com/2021/day/#{puzzle.day})\n"
  readme += "## Code\n```#{puzzle.filetype}\n#{get_python_code(puzzle)}\n```\n"
  readme += "## Input\n```\n#{puzzle.readable_input}\n```\n"
  readme += "## Output\n```\n#{puzzle.output}\n```"
end
