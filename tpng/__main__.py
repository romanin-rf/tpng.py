import tpng
from rich.console import Console

c = Console()

try:
    t = tpng.TPNG("D:\\Downloads\\Minecraft_missing_texture_block.svg.png")
    t.resize( (50, 25) )
    text = t.get_rich_string()
    c.print(text)
except:
    c.print_exception(show_locals=True, word_wrap=True)