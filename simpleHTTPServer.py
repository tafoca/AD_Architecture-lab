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
        <h1>Simply<span class="color">.</span></h1>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Portfolio</a></li>
                <li><a href="#">Contact</a></li>
                <li><a href="#">Blog</a></li>
            </ul>
        </nav>
    </div>
    </header>
    
    <div id="hero-image">
        <div class="wrapper">
            <h2><strong>A Minimal, clean</strong><br/>
            layout for web design.</h2>
            <a href="#" class="button-1">Get Started</a>
        </div>
    </div>
    
    <div id="features">
        <div class="wrapper">
            <ul>
                <li class="feature-1">
                    <h4>Easy to Edit</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam mollis turpis ac libero interdum, id fringilla purus feugiat. Etiam malesuada mattis nibh at bibendum.</p>
                </li>
                <li class="feature-2">
                    <h4>Layered PSD</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam mollis turpis ac libero interdum, id fringilla purus feugiat. Etiam malesuada mattis nibh at bibendum.</p>
                </li>
                <li class="feature-3">
                    <h4>Ready to Go</h4>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam mollis turpis ac libero interdum, id fringilla purus feugiat. Etiam malesuada mattis nibh at bibendum.</p>
                </li>
                <div class="clear"></div>
            </ul>
        </div>
    </div>
    
    <div id="primary-content">
        <div class="wrapper">
            <article>
                <h3>Featured Content</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod leo a nibh dignissim tincidunt. Nam ultricies odio ac neque suscipit volutpat. Ut dictum adipiscing felis sed malesuada. Integer porta sem nec nibh hendrerit imperdiet. </p>
                <a href="#"><img src="images/video-placeholder.jpg" alt="video placeholder" /></a>
            </article>
        </div>
    </div>
    
    <div id="secondary-content">
        <div class="wrapper">
            <article style="background-image: url('images/article-image-1.jpg');">
                <div class="overlay">
                    <h4>Secondary Content</h4>
                    <p><small>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod leo a nibh dignissim tincidunt nam.</small></p>
                    <a href="#" class="more-link">View more</a>
                </div>
            </article>
            <article style="background-image: url('images/article-image-2.jpg');">
                <div class="overlay">
                    <h4>Secondary Content</h4>
                    <p><small>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod leo a nibh dignissim tincidunt nam.</small></p>
                    <a href="#" class="more-link">View more</a>
                </div>
            </article><div class="clear"></div>
        </div>
    </div>
    
    <div id="cta">
        <div class="wrapper">
            <h3>Heard Enough?</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec euismod leo a nibh dignissim tincidunt. Nam ultricies odio ac neque suscipit volutpat. Ut dictum adipiscing felis sed malesuada. Integer porta sem nec nibh hendrerit imperdiet. </p>
            <a href="#" class="button-2">Get Started</a>
        </div>
    </div>
    
    <footer>
        <div class="wrapper">
            <div id="footer-info">
                <p>Copyright 2014 CompanyName. All rights reserved.</p>
                <p><a href="#">Terms of Service</a> I <a href="#">Privacy</a></p>
            </div>
            <div id="footer-links">
                <ul>
                    <li><h5>Company</h5></li>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Meet The Team</a></li>
                    <li><a href="#">What We Do</a></li>
                    <li><a href="#">Careers</a></li>
                </ul>
                <ul>
                    <li><h5>Company</h5></li>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Meet The Team</a></li>
                    <li><a href="#">What We Do</a></li>
                    <li><a href="#">Careers</a></li>
                </ul>
                <ul>
                    <li><h5>Company</h5></li>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Meet The Team</a></li>
                    <li><a href="#">What We Do</a></li>
                    <li><a href="#">Careers</a></li>
                </ul>
            </div>
            <div class="clear"></div>
        </div>
    </footer>

</body>
</html>
"""
#
import socket
addr = socket.getaddrinfo('0.0.0.0', 1025)[0][-1]

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