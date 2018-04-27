// http://www.scala-lang.org/docu/files/packageobjects/packageobjects.html

// in file PrintPlanted.scala
import gardening.fruits._
object PrintPlanted {
  def main(args: Array[String]) {
    for (fruit: Fruit <- planted) {
      showFruit(fruit)
    }
  }
}
