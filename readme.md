
* MicroPython  - JSON & Network Modules + Practical Example 

help("modules")
__main__          mip/__init__      ucryptolib        uselect
_thread           mip/__main__      uctypes           usocket
_uasyncio         termios           uerrno            ussl
argparse          uarray            uhashlib          ustruct
btree             uasyncio/__init__ uheapq            usys
builtins          uasyncio/core     uio               utime
cmath             uasyncio/event    ujson             utimeq
ffi               uasyncio/funcs    umachine          uwebsocket
framebuf          uasyncio/lock     uos               uzlib
gc                uasyncio/stream   urandom
math              ubinascii         ure
micropython       ucollections      urequests
Plus any modules on the filesystem

* Help about one module, functions
help("ujson")
object ujson is of type str
  find -- <function>
  rfind -- <function>
  index -- <function>
  rindex -- <function>
  join -- <function>
  split -- <function>
  splitlines -- <function>
  rsplit -- <function>
  startswith -- <function>
  endswith -- <function>
  strip -- <function>
  lstrip -- <function>
  rstrip -- <function>
  format -- <function>
  replace -- <function>
  count -- <function>
  partition -- <function>
  rpartition -- <function>
  center -- <function>
  lower -- <function>
  upper -- <function>
  isspace -- <function>
  isalpha -- <function>
  isdigit -- <function>
  isupper -- <function>
  islower -- <function>
  encode -- <function>

# This should retrieve the webpage and print the HTML to the console.
* htp_get.py
# Simple HTTP server
* The following code creates an simple HTTP server 
* which serves a single webpage that contains a
* table with the state of all the GPIO pins: