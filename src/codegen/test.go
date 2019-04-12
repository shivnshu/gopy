package mypkg

var d int = 4

func test(a int, b int) (int, int) {
	f := 10
	return 2, 10
}

func main() {
	c, d := test(1, 2)
}
