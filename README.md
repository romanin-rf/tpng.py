# tpng.py
## Description
The library has the ability to convert `image` to `string` for [rich](https://pypi.org/project/rich). 

**TPNG** - is a library for converting images into a colour-coded string. Mapping is implemented via the [rich](https://pypi.org/project/rich) library.

[More information...](https://github.com/romanin-rf/tpng.py)

## Installation
```
pip install --upgrade tpng.py
```

## Examples
```python
import tpng
from rich.console import Console

c = Console()
t = tpng.TPNG("image.png")

string = t.get_rich_string()

c.print(string)
```

<div id="header" align="center"><img src="https://romanin-rf.github.io/tpng.py/data/tpng_with_rich.gif" width="800"></div>

## Author
- Roman Slabicky
    - [Vkontakte](https://vk.com/romanin2)
    - [GitHub](https://github.com/romanin-rf)
