// https://stackoverflow.com/questions/596467/how-do-i-convert-a-float-number-to-a-whole-number-in-javascript

// Positive
value = 5.5

Math.floor(value) //  5
Math.ceil(value)  //  6
Math.round(value) //  6
Math.trunc(value) //  5
parseInt(value)   //  5
~~value           //  5
value | 0         //  5
value >> 0        //  5
value >>> 0       //  5
value - value % 1 //  5

// Negative
value = -5.5

Math.floor(value) // -6
Math.ceil(value)  // -5
Math.round(value) // -5
Math.trunc(value) // -5
parseInt(value)   // -5
value | 0         // -5
~~value           // -5
value >> 0        // -5
value >>> 0       // 4294967291
value - value % 1 // -5

// Positive - Larger numbers
value = Number.MAX_SAFE_INTEGER/10 // 900719925474099.1

Math.floor(value) //  900719925474099
Math.ceil(value)  //  900719925474100
Math.round(value) //  900719925474099
Math.trunc(value) //  900719925474099
parseInt(value)   //  900719925474099
value | 0         //  858993459
~~value           //  858993459
value >> 0        //  858993459
value >>> 0       //  858993459
value - value % 1 //  900719925474099

// Negative - Larger numbers
value = Number.MAX_SAFE_INTEGER/10 * -1 // -900719925474099.1

Math.floor(value) // -900719925474100
Math.ceil(value)  // -900719925474099
Math.round(value) // -900719925474099
Math.trunc(value) // -900719925474099
parseInt(value)   // -900719925474099
value | 0         // -858993459
~~value           // -858993459
value >> 0        // -858993459
value >>> 0       //  3435973837
value - value % 1 // -900719925474099
