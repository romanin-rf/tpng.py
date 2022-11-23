from PIL import Image
from .Types import ImageInfo as ImageInfo

class TPNG(Image.Image):
    def get_info(self): return ImageInfo(self.fp.name if hasattr(self, "fp") else None, self.size, self.info.get("dpi", (0, 0)), self.mode)
    def __str__(self) -> str: i = self.get_info(); i.__name__ = "TPNG"; return str(i)
    def __repr__(self) -> str: return self.__str__()
    @staticmethod
    def _tohex(pixel) -> str: return "#"+"".join([hex(i)[2:] for i in pixel])
    def get_rich_string(self, pixel: str="█") -> str:
        string, img = "", self.convert("RGB")
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                string += f"[{self._tohex(self.getpixel((x, y)))}]{pixel}[/]"
            string += "\n"
        return string

# ! Functions
def open(*args, **kwargs):
    return TPNG.frombytes(Image.open(*args, **kwargs).tobytes())
def frombytes(*args, **kwargs):
    return TPNG.frombytes(*args, **kwargs)
def frombuffer(*args, **kwargs):
    return TPNG.frombytes(Image.frombuffer(*args, **kwargs).tobytes())
def fromarray(*args, **kwargs):
    return TPNG.frombytes(Image.fromarray(*args, **kwargs).tobytes())
def fromqimage(*args, **kwargs):
    return TPNG.frombytes(Image.fromqimage(*args, **kwargs).tobytes())
def fromqpixmap(*args, **kwargs):
    return TPNG.frombytes(Image.fromqpixmap(*args, **kwargs).tobytes())