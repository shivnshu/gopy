package main

import "fmt"

func main() {
  var a int
  fmt.printf("Enter the number(less than 1024):")
  fmt.scanf("%d", &a)
  fmt.printf("Binary representation of the %d is:\n", a)

  var binary [10]int

  var i int
  var tmp int
  for i = 0; a>0; i += 1 {
    tmp = a % 2
    binary[i] = tmp
    a = a / 2
  }

  var j int
  for j = i-1; j>=0; j += -1 {
    fmt.printf("%d", binary[j])
  }
}
