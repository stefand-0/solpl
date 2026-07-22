/*
Better* example for an online shop
* = not really
*/

templ User
  id: int32
  name: string
  basket: list
end

data Shop
  name: string
  products: list
end

fun register(): User
  imm username: string -> std.in("--- Username: ")
  imm loginID: int32 -> std.in("--- Login ID: ")
  imm New: User -> User(loginID, username, [])
  ret New
end

fun openShop(input: string): Shop
  if (input == "Sol")
    imm NewShop: Shop -> Shop("Sol", ["Statue", "Guy", "Dolphin with 1 eye"])
  end
  ret NewShop
end

fun addToBasket(product: string): list
  imm newUser: User -> register()
  list.push(newUser.basket, product)
end

fun main(): nothing
  std.outln("--- Shops: Sol")
  imm shopInput: string -> std.in("What shop would you like to enter?")
  imm Sol: Shop -> openShop("Sol")
  addToBasket(Sol.products[1])
  std.outln("In Basket: " + type.toString(Sol.products))
end
