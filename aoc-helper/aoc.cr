require "option_parser"
require "./puzzle"
require "./utility"

day : Int32 = 0
language : String = "rb"
generate_template : Bool = true

OptionParser.parse do |parser|
  parser.banner = "Usage: aoc [arguments]"

  parser.on "-h", "--help", "Show help" do
    puts parser
    exit
  end

  parser.on "-l [LANG]", "--lang=[LANG]", "Set the language you want to use" do |lang|
    if !["go", "rb", "py", "cr"].includes?(lang)
      puts "Please enter a valid language short. (e.g. rb, py)"
      exit
    end
    language = lang
  end

  parser.on "-d [DAY]", "--day=[DAY]", "Set the day you want to work on" do |d|
    selected_day = d.to_i
    if selected_day > 25 || selected_day < 0
      puts "Please use a day between 0 and 25"
      exit
    end
    day = selected_day
  end
  parser.on "-nt", "--no-template", "Don't generate a template" { generate_template = false }

  parser.on "gen-doc", "Generate a README for every AOC-day" do
    # Make sure the `day` and `lang` flag are parsed
    parser.parse

    if day == 0
      count = 0
      get_puzzles.each do |puzzle|
        puzzle.create_file "README.md", generate_readme(puzzle)
        count += 1
      end
      puts "Generated #{count} README's"
    else
      puzzle = Puzzle.new "day_#{day}", language
      puzzle.create_file "README.md", generate_readme(puzzle)
      puts "Generated README for Day #{day}"
    end
    exit
  end
end

# Execute the command

dir_name = "day_" + day.to_s
if !Dir.exists?(dir_name)
  Dir.mkdir dir_name
end
puzzle = Puzzle.new(dir_name, language)
if generate_template
  puzzle.create_file "input.txt", ""
  puzzle.create_file "output.txt", ""
  puzzle.create_file "solution.#{language}", File.read("res/template.#{language}").gsub("{{ROOT}}", dir_name)
  if ["py"].includes?(language)
    puzzle.create_file "test_solution.#{language}", File.read("res/test_template.#{language}").gsub("{{ROOT}}", dir_name)
    puzzle.create_file "example_input.txt", ""
    puzzle.create_file "example_output.txt", ""
  end
end
