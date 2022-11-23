from io import BufferedReader, BytesIO
from PIL import Image
from .Types import ImageInfo as ImageInfo

class TPNG:
    def __init__(
        self,
        fp,
        mode=None,
        size=None,
        *args,
        **kwargs
    ) -> None:
        if isinstance(fp, str):
            self.image = Image.open(fp, *args, **kwargs)
        elif isinstance(fp, bytes):
            self.image = Image.frombytes(mode, size, fp, *args, **kwargs)
        elif isinstance(fp, BufferedReader):
            self.image = Image.frombuffer(mode, size, fp, *args, **kwargs)
        elif isinstance(fp, BytesIO):
            self.image = Image.frombuffer(mode, size, fp, *args, **kwargs)
        elif isinstance(fp, Image.Image):
            self.image = fp
        else:
            raise TypeError(f"Type parameter for 'fp' cannot be a '{type(fp)}'")
        self.image = self.image.convert("RGBA")
    
    def resize(self, new_size) -> None:
        if self.image.size != new_size:
            self.image = self.image.resize(new_size)
    
    def get_info(self):
        return ImageInfo(self.image.fp.name if hasattr(self, "fp") else None, self.image.size, self.image.info.get("dpi", (-1, -1)), self.image.mode)
    
    @staticmethod
    def to_hex(pixel) -> str: return "#"+"".join([hex(i)[2:] for i in pixel])
    
    def get_rich_string(
        self,
        pixel="█",
        error_pixel="?",
        alpha_pixel=" ",
        alpha_colours=None
    ) -> str:
        string, img, alpha_colours = "", self.image.convert("RGB"), alpha_colours or []
        alpha_colours = [tuple(i) for i in alpha_colours]
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                try:
                    if (p:=img.getpixel( (x, y) )) not in alpha_colours:
                        string += f"[{self.to_hex(p)}]{pixel}[/]"
                    else:
                        string += alpha_pixel
                except:
                    string += error_pixel
            string += "\n"
        return string
