import machine
#pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]
pins = [0, 2, 4, 5, 12, 13, 14, 15]
html = """<!DOCTYPE HTML>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Simply</title>
    <!--[if lt IE 9]>
    <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
</head>
 
<body>
    <!--img src="http://codeskulptor-demos.commondatastorage.googleapis.com/GalaxyInvaders/back05.jpg" alt="alt"/-->
     <header>
        <div class="wrapper">
            <h1></h1>
            <nav></nav>
        </div>
    </header>
    
    <div id="hero-image">
        <div class="wrapper">
            <h2></h2>
            <a></a>
        </div>
    </div>
    
    <div id="features">
        <div class="wrapper">
            <ul>
                <li></li>
                <li></li>
                <li></li>
            </ul>
        </div>
    </div>
    
    <div id="primary-content">
        <div class="wrapper">
            <article></article>
        </div>
    </div>
    
    <div id="secondary-content">
        <div class="wrapper">
            <article></article>
            <article></article>
        </div>
    </div>
    
    <div id="cta">
        <div class="wrapper">
        </div>
    </div>
    
    <footer>
        <div class="wrapper">
            <div id="footer-info"></div>
            <div id="footer-links">
                <ul></ul>
                <ul></ul>
                <ul></ul>
            </div>
        </div>
    </footer>
</body>
</html>
"""
#
import socket
addr = socket.getaddrinfo('0.0.0.0', 1028)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    rows = ['<tr><td>%d</td><td>%d</td></tr>' % (p, p) for p in pins]
    response = html #% '\n'.join(rows)
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()