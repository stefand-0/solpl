account{}
  name = ""
  id = 566
  cvv = 123
  amount = -1
end

get_amount()
  _return -> account.amount
end

verify_cvv()
  _get("solstd/std/extdata/Boolean.sol")
  temp -> account.cvv
  if temp = 123
    _return -> Boolean.true()
  end
end

main()
  verify_cvv()
  balance = get_amount()
  if balance < 0
    debt = 0 - balance
    _out -> "You are in debt! Please pay: " + debt + "!" 
  end
end