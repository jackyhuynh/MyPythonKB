# My Python KB

## Getting Started

- **Python Fundamental**

## Resources

- **Textbook:** Starting out with Python – Fifth Edition, by Tony Gaddis. ISBN-13: 978-0-592903-2.

## Python Development Environment Setup

We'll use Python for programming. Download the Python interpreter to your computer for free. Any version from 3.8 and
higher is acceptable, avoid 2.x.xx versions. Online students must also download IDLE or another Python IDE.

- [Python IDLE](https://docs.python.org/3/library/idle.html)
- [Example of Python IDE](https://www.jetbrains.com/pycharm/download/?section=mac)

### Test linter local before push:

Run these for install pylint if you don't have one

```bash
python3 -m ensurepip --upgrade
python3 -m pip install --upgrade pip
python3 -m pip install pylint
cd /path/to/your/project

pylint $(git ls-files '*.py')
```

Run this for local check

```bash
pylint $(git ls-files '*.py')
```
