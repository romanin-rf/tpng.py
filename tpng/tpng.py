from io import BufferedReader, BytesIO
from PIL import Image

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
        
        if self.image.mode != "RGB": self.image = self.image.convert("RGB")
        self.use_image = self.image.copy()
    
    @staticmethod
    def to_hex(pixel) -> str:
        color = "#"
        for i in pixel:
            if len(c:=hex(i)[2:]) < 2:
                c = "0" + c
            color += c
        return color
    
    @property
    def size(self): return self.use_image.size
    
    def resize(self, size: tuple) -> None: self.use_image = self.use_image.resize(size)
    def convert(self, mode: str) -> None: self.use_image = self.use_image.convert(mode)
    
    def reset(self) -> None: self.use_image = self.image.copy()
    
    def to_rich_image(
        self,
        pixel: str="█",
        error_pixel: str="?",
        alpha_pixel: str=" ",
        alpha_colors: list=[]
    ) -> str:
        timg = ""
        img = self.use_image if self.use_image.mode == "RGB" else self.use_image.convert("RGB")
        
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                try:
                    pix = img.getpixel((x, y))
                    if pix not in alpha_colors: timg += f"[{self.to_hex(pix)}]{pixel}[/]"
                    else: timg += alpha_pixel
                except: timg += error_pixel
            timg += "\n"
        
        return timg
