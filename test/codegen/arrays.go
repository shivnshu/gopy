package mypkg

import "fmt"

func main() {
  var a [2][3]int
  a[1][2] = 6
  fmt.printf("%d\n", a[1][2])
  a[1][1] = 5
  var i int = 1
  fmt.printf("%d\n", a[i][i])
  var b[1][5]float
  b[0][4] = 0 + 4.0
  fmt.float_print(b[0][4])
}
