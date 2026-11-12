<p align="center">
  <svg width="100%" height="80" viewBox="0 0 800 80" xmlns="http://www.w3.org/2000/svg">
    <style>
      .bg { fill: #0d1117; }
      .text-glow {
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
        font-weight: 900;
        font-size: 38px;
        fill: url(#gradient);
        filter: drop-shadow(0px 0px 8px rgba(0, 242, 254, 0.6));
        animation: pulse 3s infinite alternate;
      }
      @keyframes pulse {
        0% { opacity: 0.85; transform: scale(1); }
        100% { opacity: 1; transform: scale(1.02); }
      }
    </style>
    <rect width="100%" height="100%" class="bg" rx="10"/>
    <defs>
      <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00f2fe" />
        <stop offset="50%" stop-color="#4facfe" />
        <stop offset="100%" stop-color="#00c6ff" />
      </linearGradient>
    </defs>
    <text x="50%" y="52%" dominant-baseline="middle" text-anchor="middle" class="text-glow">
      HxN × E.L.V ULTIMATE v2.0
    </text>
  </svg>
</p>

> A collaborative, high-performance Python toolkit proudly built by **HxN × E.L.V**, designed to streamline your workflow, boost productivity, and elevate your development experience to the next level.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Team](https://img.shields.io/badge/Team-HxN%20%C%20E.L.V-purple.svg)](https://github.com/HxN-ELV)
[![Version](https://img.shields.io/badge/version-2.0.0-green.svg)](https://github.com/HxN-ELV/elv-ultimate-v2)
[![Python Version](https://img.shields.io/badge/python-%3E%3D%203.8-brightgreen.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-success.svg)](https://github.com/HxN-ELV/elv-ultimate-v2/graphs/commit-activity)

---

## 🌟 Overview

**HxN × E.L.V Ultimate v2.0** is an exclusive, feature-rich utility suite born from the collaboration between **HxN** and **E.L.V**. Building upon previous versions, this major release brings a completely overhauled architecture, lightning-fast execution speeds, enhanced security protocols, and an extensive arsenal of powerful tools to handle complex automation and penetration tasks effortlessly.

---

## 🛠️ Arsenal List (The Complete Suite)

Here is the complete catalog of high-performance modules and tools included in your **HxN × E.L.V Ultimate v2.0** arsenal:

### 1. 🔍 Recon & Information Gathering
- **Target Profiler (`recon.profiler`)**: Deep-scans target endpoints and aggregates metadata.
- **Subdomain Enumerator (`recon.subdom`)**: High-speed multi-threaded subdomain discovery tool.
- **Port Scanner Pro (`recon.portscan`)**: Advanced TCP/UDP port mapping with service version detection.
- **ASN & IP Intelligence (`recon.intel`)**: Gathers autonomous system numbers, GeoIP data, and hosting provider info.

### 2. ⚡ Web Exploitation & Testing
- **SQLi Auditor (`web.sqli`)**: Automated scanner for detecting SQL injection vulnerabilities.
- **XSS Payload Injector (`web.xss`)**: Tests reflection points and injects customized XSS vectors.
- **Directory Brute-Forcer (`web.dirbuster`)**: Asynchronous path and file finder using custom wordlists.
- **Header Security Analyzer (`web.headers`)**: Audits HTTP security headers (CSP, HSTS, X-Frame-Options, etc.).

### 3. 🔐 Cryptography & Hashing
- **Hash Cracker Suite (`crypto.cracker`)**: Supports MD5, SHA-256, bcrypt, and Argon2 brute-forcing/dictionary matching.
- **JWT Inspector & Forger (`crypto.jwt`)**: Decodes, verifies, and tests JSON Web Tokens for security flaws.
- **AES/RSA Vault (`crypto.vault`)**: Encrypts and decrypts sensitive configuration payloads securely.

### 4. 🤖 Automation & Workflow
- **Macro Script Runner (`auto.macro`)**: Executes complex multi-step automated workflows.
- **API Request Fuzzers (`auto.fuzzer`)**: Sends randomized payloads to endpoints to discover unexpected behavior.
- **Webhook Dispatcher (`auto.webhook`)**: Integrates seamlessly with Discord, Telegram, and Slack for alerts.

### 5. 📊 Reporting & Utility
- **HTML/PDF Report Generator (`utils.reporter`)**: Compiles scan logs and vulnerability findings into executive-ready reports.
- **Log Streamer & Sanitizer (`utils.logger`)**: Real-time console color logging with output sanitization.

---

## 📦 Prerequisites

Before you begin, ensure you have Python installed on your system:
- **Python** (v3.8 or higher recommended)
- **pip** (Python package manager)

---

## 📥 Installation

Clone the repository and install the required dependencies:

```bash
# Clone the repository
git clone https://github.com/HxN-ELV/elv-ultimate-v2.git

# Navigate to the project directory
cd elv-ultimate-v2

# Install required dependencies
pip install -r requirements.txt
```

---

## 🚀 Quick Start & Usage

Get **HxN × E.L.V Ultimate v2.0** up and running in your environment instantly using the appropriate command for your operating system:

### For Linux / macOS:
```bash
python3 elv-ultimate.py --help
```

### For Windows:
```cmd
python elv-ultimate.py --help
```

---

## 💻 Example Code Integration

Here is a quick example of how to import and utilize an arsenal module inside your custom Python scripts:

```python
from core.arsenal import ELVToolkit

def main():
    # Initialize the toolkit suite
    toolkit = ELVToolkit(mode="pro", debug=False)
    
    # Run a specific arsenal module (e.g., Recon Profiler)
    target = "https://example.com"
    print(f"[*] Launching target profiling on: {target}")
    
    result = toolkit.execute_module("recon.profiler", target=target)
    print("[+] Execution completed successfully:", result)

if __name__ == "__main__":
    main()
```

---

## 🗺️ Roadmap

- [x] Core architecture refactoring (v2.0)
- [x] Comprehensive HxN × E.L.V Arsenal module integration
- [ ] Web-based graphical dashboard interface
- [ ] Cloud synchronization for custom macro configurations
- [ ] Native support for additional scripting runtimes

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

<p align="center">
  Crafted with ❤️ by <b>HxN × E.L.V Team</b>
</p>