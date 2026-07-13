; This demonstrates launching a group of threads:

func()
  _return -> 1
end

main()
  _get("async/Group.sol")
  Group.launch(func, 2, "done")
  ; prints "done" when both are done launching
end