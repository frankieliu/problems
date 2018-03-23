// http://www.scala-lang.org/docu/files/packageobjects/packageobjects.html

// in file gardening/package.scala
package gardening
package object fruits {
  val planted = List(apple, plum, banana)               
  def showFruit(fruit: Fruit) {
    println(fruit.name +"s are "+ fruit.color)
  }
}
