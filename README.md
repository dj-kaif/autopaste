# autopaste 🚀

A minimalist, privacy-focused command-line utility for instantly uploading text snippets, logs, and source code to `paste.c-net.org` directly from your terminal.

[![PyPI version](https://img.shields.io/pypi/v/autopaste.svg)](https://pypi.org/project/autopaste/)
[![Python Support](https://img.shields.io/pypi/pyversions/autopaste.svg)](https://pypi.org/project/autopaste/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- **File Uploads** — Upload any file by providing its path.
- **Pipe Support** — Accept input from standard Unix pipes.
- **Interactive Mode** — Paste or write text directly when no input source is provided.
- **Zero Configuration** — Works immediately after installation.
- **Lightweight** — Minimal dependencies and fast execution.

---

## 📦 Installation

### From PyPI

```bash
pip install --upgrade autopaste
```

---

## 🚀 Quick Start

### Upload a File

```bash
autopaste main.py
```

### Upload Piped Input

```bash
echo "Hello from terminal!" | autopaste
```

```bash
cat application.log | autopaste
```

### Interactive Input

```bash
autopaste
```

Example prompt:

```text
Paste or Write:
```

After submitting your content, `autopaste` returns the generated paste URL.

---

## 🎛️ Command Options

```text
options:
  -h, --help     Show this help message and exit
  -v, --version  Show the program version and exit
```

---

## 📂 Examples

Upload a Python script:

```bash
autopaste bot.py
```

Upload command output:

```bash
python main.py | autopaste
```

Upload a log file:

```bash
autopaste latest.log
```

---

## 🛡️ Privacy

`autopaste` sends content directly to `paste.c-net.org`.

Any data retention, logging, or privacy policies are determined by the paste service itself.

---

## 📄 License

Distributed under the MIT License. See the `LICENSE` file for details.

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome.

If you discover an issue, please open an issue on GitHub.

---

## ⭐ Support

If autopaste saves you time, consider starring the repository.
