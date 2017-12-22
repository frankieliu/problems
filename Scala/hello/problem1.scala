
object myfunctions {

  def last[A](l:List[A]):A = {
    l.last
  }
  // myfunctions.last(List(1,2,4))

  def last1[A](l:List[A]):A = l match {
    case h :: Nil => h
    case _ :: tail => last1(tail)
    case _ => throw new NoSuchElementException
  }

  /** Returns reversed @param x and also the number of digits
    *
    *  For example: reverse_size(10) returns (01, 2)
    */

  def reverse_size (x :Int): (Int, Int) = {
    x match {
      case a if a < 10 => return (x, 1)
      case _ => {
        val xr = x % 10
        val xq = reverse_size(x/10)
        if (xq._2 == 9 && (xr > 2 || xq._1 > 147483647)) {
          return (0,0)
        } else {
          return ( scala.math.pow(10,xq._2).toInt * xr + xq._1, xq._2 + 1)
        }
      }
    }
  }

  def reverse1 (x: Int): Int = {
    x match {
      case Int.MinValue => return 0
      case a if a < 0 => return -1 * reverse1(-x)
      case _ => return reverse_size(x)._1
    }
  }

  def reverse (x: Int): Int = {
    var ans:Int = 0
    var y:Int = x
    while (y != 0) {
      var tmp:Int = ans * 10 + y % 10
      if (tmp / 10 != ans) return 0
      ans = tmp
      y = y / 10
    }
    return ans
  }

  def addTwoNumbers(args: Array[String]) {
        println(io.Source.stdin.getLines().take(2).map(_.toInt).sum)
  }



}

/* 
 * https://alvinalexander.com/scala/sbt-how-to-compile-run-package-scala-project
 */
