from io import BufferedReader, BytesIO
from PIL import Image
from typing import Tuple, overload, Iterable, Literal, List

class TPNG:
    """
    A class for converting an image into text.
    
    Attributes:
        image: `~PIL.Image.Image` - Unchangeable attribute storing the original image.
        use_image: `~PIL.Image.Image` - The image over which changes are being made. It can be overwritten with the original using the ~tpng.TPNG.reset function.
    """
    image: Image.Image
    use_image: Image.Image
    
    @overload
    def __init__(self, fp: str, *args, **kwargs) -> None: ...
    @overload
    def __init__(self, fp: Image.Image, *args, **kwargs) -> None: ...
    @overload
    def __init__(self, fp: bytes, mode: str, size: Tuple[int, int], *args, **kwargs) -> None: ...
    @overload
    def __init__(self, fp: BufferedReader, mode: str, size: Tuple[int, int], *args, **kwargs) -> None: ...
    @overload
    def __init__(self, fp: BytesIO, mode: str, size: Tuple[int, int], *args, **kwargs) -> None: ...
    
    @staticmethod
    def to_hex(pixel: Iterable[int]) -> str: ...
    
    def resize(self, size: Tuple[int, int]) -> None: ...
    def convert(self, mode: Literal["RGB", "RGBA", "RGBX", "CMYK", "L", "P", "I"]) -> None: ...
    
    def reset(self) -> None: ...
    
    def to_rich_image(
        self,
        pixel: str="█",
        error_pixel: str="?",
        alpha_pixel: str=" ",
        alpha_colors: List[Tuple[int, int, int]]=[]
    ) -> str: ...