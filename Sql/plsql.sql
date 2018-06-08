-- run everything in the background
DECLARE
   CURSOR c IS
      SELECT * FROM dual;

   l_x c%ROWTYPE;

BEGIN
   FOR x IN c LOOP
      l_x := x;
   END LOOP;
END;
/
