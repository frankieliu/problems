import hello._
import smath._

object Main extends App {

  def getGreeting() :String =
    "Hello, world"+hello.Jmath.sqr(2)+" "+smath.Smath.sqr(3);

  println(getGreeting())

}
