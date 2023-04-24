import tpng
from rich.console import Console

c = Console()

try:
    t = tpng.TPNG("D:\Pictures\Rebecca\g-oIJG0T-b8Fsxm8BUef_Jnxh13Hymp8Gm7GWGrA7y7q2hrejcHOvrtFipRL50qVfxtbomMzb8874YAeVu-b-bCG.jpg")
    t.resize( (50, 25) )
    text = t.to_rich_image()
    c.print(text)
except:
    c.print_exception(show_locals=True, word_wrap=True)