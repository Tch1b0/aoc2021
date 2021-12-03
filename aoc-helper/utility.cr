require "./day"

def get_puzzles
  dirs = Dir.children(".").select(/^day_/)
  days = [] of Day
  dirs.each do |dir|
    days.push(Day.new(dir, "py"))
  end
  days
end

def get_python_code(day : Day) : String
  input = day.solution.split "\n"
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

def generate_readme(day : Day)
  readme = "# Day #{day.day}\n"
  readme += "#### [Task](https://adventofcode.com/2021/day/#{day.day})\n"
  readme += "## Code\n```#{day.filetype}\n#{get_python_code(day)}\n```\n"
  readme += "## Input\n```\n#{day.readable_input}\n```\n"
  readme += "## Output\n```\n#{day.output}\n```"
end
