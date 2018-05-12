import org.junit.runner.RunWith
import org.scalatest.junit.JUnitRunner
import org.scalatest.FunSpec

@RunWith(classOf[JUnitRunner])
class MyTest extends FunSpec{
  describe("A Set") {
    describe("when empty"){
      it("should have size 0") {
        assert(Set.empty.size == 0)
      }
      it("should produce NoSuchElementException when head is invoked"){
        assertThrows[NoSuchElementException]{
          Set.empty.head
        }
      }
    }
  }
}
