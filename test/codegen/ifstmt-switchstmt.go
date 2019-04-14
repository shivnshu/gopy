package mypkg

import "fmt"

func main() {
  a := 1
  if (a == 11) {
    fmt.printf("a is 11\n")
  }
  else  if (a == 12) {
    fmt.printf("a is 12\n")
  }
  else {
    fmt.printf("a is neither 11 or 12\n")
  }

  var b string
  x := 2
	switch x {
	case 1:
		{
      b = "x is 1"
		}
	case 2:
		{
      b = "x is 2"
		}
	case 3:
		{
      b = "x is 3"
		}
	}
  fmt.printf("Switch: %s\n", b)
}
