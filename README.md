# Flask Password Security Demo 🔓

A deliberately insecure Flask login application designed to demonstrate how **Wireshark** can be used to intercept plain text passwords over HTTP connections.


## 🚀 Quick Start - Using Docker 🐳

```bash

docker run --rm -p 5000:5000 ghcr.io/mavi0/flask-password-demo:latest
```

➡️ Visit `http://localhost:5000` in your browser.

### Demo Credentials
- **Username:** `admin` | **Password:** `password123`
- **Username:** `user` | **Password:** `secret456`  
- **Username:** `demo` | **Password:** `plaintext`


**Remember:** Always use HTTPS in production and never transmit sensitive data over plain HTTP! 🔐 