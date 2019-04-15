package mypkg

import "fmt"

func quicksort(arr [10]int){
	fmt.printf("%d",arr[1])
}

func main(){
	var n int
	fmt.scanf("%d", &n)
	var arr [n]int
	var j int
	for i:=0; i<n; i += 1 {
		fmt.scanf("%d", &j)
		arr[i] = j
	}
	quicksort(arr)
}