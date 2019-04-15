
package mypkg

import "fmt"

func main() {
  var q bool
  q = true
  var w bool
  w = false
  e := q && (!w)
  fmt.printf("e: %d\n", e)
}
