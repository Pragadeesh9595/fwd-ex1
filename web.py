 http.server import HTTPServer, BaseHTTPRequestHandler
contefromnt = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>IP + TCP Port Validator</title>
  <style>
    body { font-family: system-ui, Arial; max-width: 720px; margin: 40px auto; padding: 0 16px; }
    input { padding: 8px; font-size: 16px; width: 100%; box-sizing: border-box; margin-bottom: 8px;}
    .row { display: flex; gap: 8px; }
    .row input { flex: 1; }
    .ok { color: green; }
    .err { color: red; }
  </style>
</head>
<body>
  <h1>Enter IP address and TCP port</h1>

  <div class="row">
    <input id="ip" placeholder="IP address (IPv4 or IPv6)" />
    <input id="port" placeholder="TCP port (1–65535)" />
  </div>
  <button id="check">Validate</button>

  <p id="message"></p>

  <script>
    const isIPv4 = s => {
      const parts = s.split('.');
      if (parts.length !== 4) return false;
      return parts.every(p => {
        if (!/^\d+$/.test(p)) return false;
        const n = Number(p);
        return n >= 0 && n <= 255;
      });
    };

    const isIPv6 = s => {
      // Basic IPv6 pattern (doesn't cover every corner case but OK for validation)
      return /^[0-9a-fA-F:]+$/.test(s) && s.includes(':') && s.length <= 39;
    };

    const isValidPort = p => {
      if (!/^\d+$/.test(p)) return false;
      const n = Number(p);
      return n >= 1 && n <= 65535;
    };

    document.getElementById('check').addEventListener('click', () => {
      const ip = document.getElementById('ip').value.trim();
      const port = document.getElementById('port').value.trim();
      const msg = document.getElementById('message');

      if (!ip) return msg.innerHTML = '<span class="err">Enter an IP address.</span>';
      if (!port) return msg.innerHTML = '<span class="err">Enter a port number.</span>';

      const ipOk = isIPv4(ip) || isIPv6(ip);
      const portOk = isValidPort(port);

      if (!ipOk && !portOk) {
        msg.innerHTML = '<span class="err">Invalid IP and port.</span>';
      } else if (!ipOk) {
        msg.innerHTML = '<span class="err">Invalid IP address.</span>';
      } else if (!portOk) {
        msg.innerHTML = '<span class="err">Invalid port (1–65535).</span>';
      } else {
        msg.innerHTML = <span class="ok">Valid — IP: ${ip}, Port: ${port}</span>;
      }
    });
  </script>
</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()