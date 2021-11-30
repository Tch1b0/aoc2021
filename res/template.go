package main

import (
	"fmt"
	"io/ioutil"
)

// returns the puzzle input
func get_input() string {
	data, err := ioutil.ReadFile("{{ROOT}}/input.txt")
	if err != nil {
		fmt.Println(err)
	}
	return string(data)
}

// write the solution to the output file
func output(str string) error {
	return ioutil.WriteFile("{{ROOT}}/output.txt", []byte(str), 0777)
}

func main() {
	// Solution goes here
}
