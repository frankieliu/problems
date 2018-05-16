
// DataFrame
val df = List((1,"one"),(2,"two")).toDF

// Array[Row]
val rdd = df.rdd

case class numStr(num: Int, s: String);
val ds = rdd.as[numStr]
