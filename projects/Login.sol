/* 
Login example for an online shop...
*/

data User
  name: string
  id: int32
  productsID: list
end

fun login(): boolean
  imm User1: User -> User("Stefan", 12345, [1, 2, 10]
  if (User1.id == 12345)
    match (User1.name)
      "Stefan" -> ret true
    end
    match (User1.productsID)
      User1.productsID -> ret true
    end
  end
end

fun main(): nothing
  if (login())
      std.outln("Login successful!")
  end
end
