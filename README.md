# tpng.py
## Description
A special file format for displaying images in the terminal. The library has the ability to convert `.png` to `.tpng`. **_TPNG_** - its own format of pictures for the terminal and `tpng.py` allows you to display them in the terminal, it is better to use it together with the [rich](https://pypi.org/project/rich/) library. Examples will be below.

## Installation
```
pip install tpng.py pillow
```

## Examples
```python
import tpng.tpng as tpng
from rich.console import Console

c = Console()
t = tpng.TPNG("youtube.tpng")

t.upload_from_png(ipath="youtube.png") # Convert image from .png to .tpng

c.print(t.get_image_rich())
```
![tpng_with_rich](https://romanin-rf.github.io/tpng.py/data/tpng_with_rich.gif)

## Author
- Roman Slabicky
    - [Vkontakte](https://vk.com/romanin2)
    - [GitHub](https://github.com/romanin-rf)