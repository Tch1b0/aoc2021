# returns the puzzle input
def get_input() -> str:
    txt = ""
    with open("{{ROOT}}/input.txt", "r")as f:
        txt = f.read()
    
    return txt

# write the solution to the output file
def output(string: str) -> None:
    with open("{{ROOT}}", "w") as f:
        f.write(string)

# Solution goes here