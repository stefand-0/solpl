; _fetch() example: HTTP GET requests

main()
  ; Fetch a simple API
  data -> _fetch("https://httpbin.org/get")
  _out -> "=== httpbin.org/get ==="
  _out -> data
  
  ; Fetch with a timeout (built-in 5 seconds)
  ; _fetch() returns the raw response body as a string
  ; If the request fails, it returns "Error: ..."
  
  ; You can also fetch local files with file://
  ; local -> _fetch("file:///path/to/file.txt")
end
