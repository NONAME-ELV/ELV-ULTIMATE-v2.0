<p align="center">
  <svg width="100%" height="80" viewBox="0 0 700 80" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="gradient" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00ffff" />
        <stop offset="50%" stop-color="#ff00ff" />
        <stop offset="100%" stop-color="#00ff41" />
      </linearGradient>
      <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="3" result="blur" />
        <feComposite in="SourceGraphic" in2="blur" operator="over" />
      </filter>
    </defs>
    <style>
      .text-title {
        font-family: 'Consolas', 'Courier New', monospace;
        font-weight: 900;
        font-size: 32px;
        fill: url(#gradient);
        filter: url(#glow);
        animation: pulse 3s infinite alternate;
      }
      @keyframes pulse {
        0% { opacity: 0.85; transform: scale(1); }
        100% { opacity: 1; transform: scale(1.02); }
      }
    </style>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" class="text-title">HxN × E.L.V ULTIMATE v2.0</text>
  </svg>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/VERSION-2.0-cyan?style=for-the-badge&logo=python&logoColor=00ffff&color=121212" alt="Version">
  <img src="https://img.shields.io/badge/AUTHOR-HxN-magenta?style=for-the-badge&logo=telegram&logoColor=ff00ff&color=121212" alt="Author">
  <img src="https://img.shields.io/badge/STATUS-LOCKED%20&%20PATEN-green?style=for-the-badge&color=121212" alt="Status">
</p>

---

## ⚡ Overview

**HxN × E.L.V Ultimate v2.0** is an advanced, high-performance cybersecurity toolkit and multi-threaded automation suite engineered for security research, red teaming operations, reconnaissance, and penetration testing. Built with a cyberpunk neon aesthetic interface and powered by robust Python scripting.

---

## 🛠️ Complete Arsenal & Modules

| Module / Tool | Description |
| :--- | :--- |
| **Dork Maker & Generator** | Advanced search query generator with combinatorics (Simple, Advanced, Ultimate patterns & categories). |
| **Dork Scanner** | Multi-threaded search engine crawler (Google, Bing, Yahoo, AltaVista) with smart domain filtering & proxy support. |
| **WP Brute Force Engine** | Intelligent WordPress brute-force engine with XML-RPC checks, smart username extraction (`wp-json`), and password generators. |
| **SQLi Exploit Engine** | Automated SQL injection scanner and extractor supporting Union-based, Error-based, Boolean-based, and Time-based techniques. |
| **Param Finder** | Discovers hidden parameters, input fields, and query strings from target URLs, HTML forms, and JavaScript files. |
| **Subdomain Finder** | Enumerates subdomains via Certificate Transparency logs (crt.sh) and high-speed DNS brute-forcing. |
| **URL Filter & Cleaner** | Cleans, filters, deduplicates URL lists, removes common noise domains, and extracts clean endpoints. |
| **Web Vuln Checker** | Scans web applications for common misconfigurations, backup files, config exposures, and version disclosures. |
| **CVE WP Exploiter** | Exploits known WordPress vulnerabilities and plugin flaws for research and assessment. |
| **Backdoor Manager** | Manages web shells, payloads, and post-exploitation entry points. |
| **Mass Deface** | Multi-threaded file management and deployment utility. |
| **Advanced Recon** | Deep target profiling, technology fingerprinting, and asset discovery. |
| **Proxy Rotator** | Manages and rotates HTTP/Socks proxies to bypass rate-limiting and blocks. |
| **Data Exfiltration** | Securely packs and extracts structured data or credentials. |
| **Session Hijacking** | Cookie and token analysis toolkit. |
| **Email Spamming** | Automated mail dispatch utility for notification and stress testing. |
| **Ransomware Dropper** | Payload staging and simulation utility. |
| **DDoS Attack Suite** | Multi-threaded network stress testing module. |

---

## 🚀 Installation & Usage

### Prerequisites
* Python 3.x
* Required libraries (`requests`, `beautifulsoup4`, `pyttsx3`, etc.)

### 1. Clone & Setup
```bash
git clone https://github.com/NONAME-ELV/elv-ultimate.git
cd elv-ultimate
pip install -r requirements.txt
```

### 2. Execution

* **Linux / macOS:**
  ```bash
  python3 elv-ultimate.py
  ```

* **Windows:**
  ```cmd
  python elv-ultimate.py
  ```

---

## 📞 Contact & Channels

* **Author:** HxN
* **Telegram Channel / Group:** [@WEBSHELL999](https://t.me/WEBSHELL999) / [@allaboutcve](https://t.me/allaboutcve)
* **Personal Telegram:** [@HxNoname](https://t.me/HxNoname)

<p align="center">
  <b>⚡ ROOT ACCESS GRANTED — STAY SECURE ⚡</b>
</p>