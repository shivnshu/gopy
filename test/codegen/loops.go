package mypkg

import "fmt"

func main() {
  var i int
  sum := 0
  for i = 0; i<10; i += 1 {
    sum += i
  }

  var break_continue_sum = 0
  for i = 0; i<10; i = i+1 {
    if (i == 10) {
      break
    }
    if (i == 9) {
      continue
    }
    break_continue_sum = break_continue_sum + i
  }

  fmt.printf("Sum: %d, Break Continue Sum: %d\n", sum, break_continue_sum)
}
