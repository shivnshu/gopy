package mypkg

import "fmt"

const x = 3

func main() {
  var b int
  b = 1
  x := 2
	switch x {
	case 1:
		{
      b = 2
		}
	case 2:
		{
      b = 3
		}
	case 3:
		{
      b = 4
		}
	}
  fmt.Printf("%d\n", b)
}
