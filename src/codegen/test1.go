package mypkg

import "fmt"

func test(b [2]int) {
  fmt.printf("%d\n", b[1])
}

func main() {
  var a[4]int
  a[0] = 1
  fmt.printf("%d\n", a[0])
}
