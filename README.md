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

string = t.to_rich_image()

c.print(string)
```


![Новый проект.webm](https://user-images.githubusercontent.com/60302782/235365202-fd944bbc-9605-4bc6-b596-7528ac55b9ed.webm)


## Author
- Roman Slabicky
    - [Vkontakte](https://vk.com/romanin2)
    - [GitHub](https://github.com/romanin-rf)
