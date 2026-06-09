# autopaste

A lightweight command-line utility for instantly uploading text snippets, logs, source code, and file contents to [`paste.c-net.org`](https://paste.c-net.org) directly from your terminal.

`autopaste` is designed for situations where you need to share something quickly without creating a Git repository, uploading a file manually, or opening a browser.

[![PyPI version](https://img.shields.io/pypi/v/autopaste.svg)](https://pypi.org/project/autopaste/)
[![Python Support](https://img.shields.io/pypi/pyversions/autopaste.svg)](https://pypi.org/project/autopaste/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

---

## 📦 Installation

Install the latest version from PyPI:

```bash
pip install --upgrade autopaste
```

Verify the installation:

```bash
autopaste --version
```

---

## 🚀 Quick Start

**Upload a file**

```bash
autopaste main.py
```

**Upload piped input**

```bash
echo "Hello from terminal!" | autopaste

cat application.log | autopaste

python script.py 2>&1 | autopaste
```

**Interactive mode**

Run without arguments to enter interactive mode:

```bash
autopaste
```

Prompt:

```
Paste or Write:
```

After submitting your content, `autopaste` returns a shareable paste URL.

---

## 🎛️ Command Options

```text
usage: autopaste [-h] [-v] [file]

positional arguments:
  file           File to upload

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

Upload program output:

```bash
python main.py | autopaste
```

Upload logs:

```bash
autopaste latest.log
```

Upload package information:

```bash
pip list | autopaste
```

Upload error output:

```bash
journalctl -xe | autopaste
```

---

## 🛡️ Privacy

`autopaste` sends content directly to `paste.c-net.org`.

The tool does not store uploads locally or maintain user accounts. Any data retention, logging, moderation, or privacy policies are controlled by the paste service itself.

> **Warning:** Avoid uploading secrets, passwords, API keys, or other sensitive information.

---

## ❓ Why autopaste?

Sometimes you just need to quickly share:

- Error logs
- Stack traces
- Configuration files
- Terminal output
- Source code snippets
- Debugging information

Instead of creating a repository, committing files, and pushing changes, simply run:

```bash
autopaste your_file.log
```

and share the generated link.

---

## ✨ Features

- **Instant Uploads** — Share text, code, logs, and file contents in seconds.
- **File Support** — Upload content directly from a file path.
- **Pipe Support** — Works seamlessly with Unix pipelines.
- **Interactive Mode** — Paste or type content directly into your terminal.
- **Zero Configuration** — No setup required after installation.
- **Lightweight** — Fast startup and minimal dependencies.
- **Terminal First** — Built for developers who live in the command line.


---

## 🤝 Contributing

Contributions are welcome.

If you'd like to improve the project, feel free to:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

Bug reports, feature requests, and documentation improvements are greatly appreciated.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## ⭐ Support

If `autopaste` saves you time, consider giving the repository a star. It helps others discover the project and supports future development.
