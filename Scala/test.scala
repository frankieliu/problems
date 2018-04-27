val a = 0;
val b = a match {
  case 0 => (x: Int) => x*x
  case 1 => (x: Int) => x+x
}
print(b(10))
