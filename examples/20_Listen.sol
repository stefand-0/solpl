; _listen() example: HTTP server in Sol

; Handler function - receives the path and returns a response
handle(path)
  path = "/" ? _return -> "<h1>Welcome to Sol Server!</h1>"
  path = "/hello" ? _return -> "Hello from Sol!"
  path = "/json" ? _return -> "{status:ok}"
  _return -> "404: " + path + " not found"
end

main()
  ; Start HTTP server on port 8080
  ; _listen(port, handler_function_name)
  _listen(8080, handle)
  _out -> "Server running on http://localhost:8080"
  _out -> "Try: curl http://localhost:8080/"
  _out -> "     curl http://localhost:8080/hello"
  _out -> "     curl http://localhost:8080/json"
  
  ; The server runs in a daemon thread
  ; The program will keep running until interrupted
end
