![PyPI](https://img.shields.io/pypi/v/cd-hibp?style=for-the-badge)
![PyPI - License](https://img.shields.io/pypi/l/cd-hibp?style=for-the-badge)

# chibp

## A package for interacting with the Haveibeenpwned API

Install package:

```
pip install chibp
```

Import the package:

```
import chibp
```

Example string request:

```
chibp.get("example@chrisdunne.net", API_KEY)
```

Example list request:

```
chibp.get(["example@chrisdunne.net", "example2@chrisdunne.net"], API_KEY)
```