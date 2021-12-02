class Day
  getter :day
  getter :solution
  getter :output
  getter :input
  getter :filetype

  def initialize(dir_name : String, filetype : String)
    # @day = dir_name.gsub("day_", "")
    @filetype = filetype
    @input = File.read "#{dir_name}/input.txt"
    @output = File.read "#{dir_name}/output.txt"
    @solution = File.read "#{dir_name}/solution.#{filetype}"
  end

  def readable_input : String
    input = @input.split "\n"
    if input.size > 7
      input = input[0..7]
      input.push "..."
    end
    input.join "\n"
  end
end
