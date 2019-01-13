package main

import (
	"fmt"
	"math"
	"strings"
)

var love string

func main() {
	if love == "" {
		love = "Love"
	}
	lines := []string{}
	for y := 30.0; y > -30; y-- {
		arr := []string{}
		for x := -30.0; x <= 30; x++ {
			result := " "
			if math.Pow(math.Pow(x*0.05, 2)+math.Pow(y*0.1, 2)-1, 3)-math.Pow(x*0.05, 2)*math.Pow(y*0.1, 3) <= 0 {
				result = string(love[modPy(int(x-y), len(love))])
			}
			arr = append(arr, result)
		}
		lines = append(lines, strings.Join(arr, ""))
	}
	fmt.Println(strings.Join(lines, "\n"))
	var exit rune
	fmt.Scanf("%c", &exit)
}

func modPy(d, m int) int {
	var res = d % m
	if (res < 0 && m > 0) || (res > 0 && m < 0) {
		return res + m
	}
	return res
}
