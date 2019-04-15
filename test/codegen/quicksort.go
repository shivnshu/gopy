package mypkg

import "fmt"

func partition(arr [10]int, left int, right int) int {
  pivot := arr[right]
  i := left - 1
  var tmp int
  for j:=left; j<=right-1; j+=1 {
    if (arr[j] <= pivot) {
      i += 1
      tmp = arr[i]
      arr[i] = arr[j]
      arr[j] = tmp
    }
  }
  tmp = arr[i+1]
  arr[i+1] = arr[right]
  arr[right] = tmp
  return i + 1
}

func quicksort(arr [10]int, left int, right int) {
  if (left >= right) {
    return
  }
  pi := partition(arr, left, right)

  quicksort(arr, left, pi-1)
  quicksort(arr, pi+1, right)
}

func main(){
	var arr [10]int
	var j int
	for i:=0; i<10; i += 1 {
		fmt.scanf("%d", &j)
		arr[i] = j
	}
	quicksort(arr, 0, 9)
  fmt.printf("Sorted numbers are:\n")
  for j=0; j<10; j+=1 {
    fmt.printf("%d ", arr[j])
  }
}
