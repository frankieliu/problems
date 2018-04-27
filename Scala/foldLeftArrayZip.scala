//pprV3 = pprV2()
val a = Seq(
  Array((1,2),
    (2,3)),
  Array((1,4),
    (2,5)),
  Array((1,6),
    (1,7))
);

val b = a.map( x =>
  x.map(_._2));

val c = b.foldLeft(Array.fill[Array[Int]](3)(Array[Int]()))(
  (cum :Array[Array[Int]], x :Array[Int]) => {
    cum.zip(x).map(x => x._1 :+ x._2) });


