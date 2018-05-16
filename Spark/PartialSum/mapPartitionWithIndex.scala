val data = sc.parallelize((1 to 5))  // sc is the SparkContext
val partialSums = data.mapPartitionsWithIndex{ (i, values) =>
    Iterator((i, values.sum))
}.collect().toMap  // will in general have size other than data.count
val cumSums = data.mapPartitionsWithIndex{ (i, values) =>
    val prevSums = (0 until i).map(partialSums).sum
    values.scanLeft(prevSums)(_+_).drop(1)
}
