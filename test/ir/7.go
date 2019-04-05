package mypkg

var d int = 4

func test(a int, b float) (int, int) {
	f := 10
	return 2, 3
}

func main() {
	c, d := test(1, 2.3)
}
