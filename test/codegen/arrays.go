package mypkg

import "fmt"

func main() {
  var a [2][3]int
  a[1][2] = 6
  fmt.printf("%d\n", a[1][2])
  a[1][1] = 5
  fmt.printf("%d\n", a[1][1])
}
