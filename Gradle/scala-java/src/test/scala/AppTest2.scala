import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner
import org.scalatest.FunSpec

@RunWith(classOf[JUnitRunner])
class AppTest2 extends FunSpec{
  describe("Main") {
    it("should have greeting") {
      assert(Main.getGreeting() == "Hello, world4.0 9.2");
    }
  }
}
