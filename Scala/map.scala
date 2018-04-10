val a = List((1,2),(2,3),(3,4));
val b = a.toMap;

// List of id's
val c = List(3,4,5);

// Corresponding index in array
val d = List.range(1,c.length+1);

// Create a reverse mapping from id's to index
val e = c.zip(d).toMap;
