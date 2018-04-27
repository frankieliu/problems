import java.io.PrintWriter;
import java.io.File;

// Test speed for interpreter
val xl : List[Int] = List.range(1,100);
val xll : Seq[List[Int]] = (1 to 10).map(x => xl);

// This takes very long
if (true) {
  val st = System.nanoTime();
  val pw = new PrintWriter(new File("test1.out"));
  for (x <- xll) {
    var delim = "";
    for (y <- x) {
      pw.write(delim+y);
      delim = ",";
    }
    pw.write("\n");
  }
  pw.close();
  println("Time for for loops " + (System.nanoTime() - st));
}

if (false) {
  val st = System.nanoTime();
  val pw = new PrintWriter(new File("test.out"));
  pw.write(xll.mkString("[",",","]\n"));
  pw.close();
  println("Time for mkString " + (System.nanoTime() - st));
}

if (true) {
  val st = System.nanoTime();
  val pw = new PrintWriter(new File("test.out"));
  xll.foreach(l =>
    { var delim = "";
      l.foreach(m => {
        pw.write(delim+m.toString);
        delim=",";
      })
      pw.write("\n");
    })
  pw.close();
  println("Time for foreach "+ (System.nanoTime() - st));
}
