#!/usr/bin/env python3
"""A deliberately vulnerable practice web app for the OWASP ZAP guide.

Run it on loopback only:

    python3 vulnapp.py            # serves http://127.0.0.1:18923/

It is a teaching target, not a real application. Everything wrong
with it is wrong on purpose:

- no security headers on any response (no Content-Security-Policy,
  no X-Content-Type-Options, no anti-clickjacking header)
- an X-Powered-By header that names the app's version
- /hello and /search reflect their parameter into the page with no
  escaping (cross-site scripting, found by the active scanner)
- /item answers a quote in the id with a fake database error page
  (error messages that disclose internals)
- /login sets a session cookie with no HttpOnly and no Secure flag,
  and its password field allows the browser to autocomplete
- the home page carries an HTML comment it should not carry

Nothing here touches the network beyond the loopback address it
binds, and it stores nothing.
"""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

HOST = "127.0.0.1"
PORT = 18923


def page(title, body):
    return ("<!DOCTYPE html>\n<html>\n<head><title>" + title +
            "</title></head>\n<body>\n" + body + "\n</body>\n</html>\n")


HOME = page("Seed Store", """
<h1>The Seed Store</h1>
<p>A tiny practice shop, built to be scanned.</p>
<ul>
  <li><a href="/hello?name=guest">Say hello</a></li>
  <li><a href="/item?id=1">Item 1</a></li>
  <li><a href="/search?q=tomato">Search for tomato</a></li>
  <li><a href="/login">Staff login</a></li>
</ul>
<!-- TODO before launch: remove the test account (admin / admin123) -->
""")

LOGIN = page("Staff login", """
<h1>Staff login</h1>
<form method="post" action="/login">
  <label>User name <input type="text" name="user"></label><br>
  <label>Password <input type="password" name="pass"></label><br>
  <input type="submit" value="Log in">
</form>
""")


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    # BaseHTTPRequestHandler already sends a verbose Server header;
    # the lab adds X-Powered-By on top, on purpose.
    def send_response(self, code, message=None):
        super().send_response(code, message)
        self.send_header("X-Powered-By", "LabApp/1.0")

    def _send(self, code, body, extra=None):
        data = body.encode()
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        if extra:
            for k, v in extra:
                self.send_header(k, v)
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        u = urlparse(self.path)
        q = parse_qs(u.query)
        if u.path == "/":
            self._send(200, HOME)
        elif u.path == "/hello":
            name = q.get("name", ["world"])[0]
            # Reflected without escaping, on purpose.
            self._send(200, page("Hello", "<h1>Hello, " + name + "!</h1>"))
        elif u.path == "/search":
            term = q.get("q", [""])[0]
            # Reflected without escaping, on purpose.
            self._send(200, page("Search",
                                 "<h1>Results for " + term + "</h1>"
                                 "<p>3 packets found.</p>"))
        elif u.path == "/item":
            item = q.get("id", ["1"])[0]
            if "'" in item:
                self._send(500, page("Error",
                                     "<h1>Database error</h1>"
                                     "<p>You have an error in your SQL "
                                     "syntax; check the manual that "
                                     "corresponds to your MariaDB server "
                                     "version for the right syntax to use "
                                     "near '" + item + "'</p>"))
            else:
                self._send(200, page("Item",
                                     "<h1>Item " + item + "</h1>"
                                     "<p>One packet of seeds.</p>"))
        elif u.path == "/login":
            self._send(200, LOGIN)
        else:
            self._send(404, page("Not found", "<h1>Not found</h1>"))

    def do_POST(self):
        u = urlparse(self.path)
        length = int(self.headers.get("Content-Length", 0))
        self.rfile.read(length)
        if u.path == "/login":
            # A session cookie with no HttpOnly and no Secure, on purpose.
            self._send(200, page("Welcome",
                                 "<h1>Welcome back.</h1>"
                                 "<p><a href=\"/\">Home</a></p>"),
                       extra=[("Set-Cookie", "session=lab-session-42; Path=/")])
        else:
            self._send(404, page("Not found", "<h1>Not found</h1>"))

    def log_message(self, fmt, *args):
        pass  # keep the terminal quiet; ZAP's transcripts are the record


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print("Practice app listening on http://%s:%d/" % (HOST, PORT))
    server.serve_forever()
