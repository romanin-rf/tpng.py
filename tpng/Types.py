from dataclasses import dataclass
from typing import Tuple, Literal, Optional

@dataclass
class ImageInfo:
    name: Optional[str]
    size: Tuple[int, int]
    dpi: Tuple[int, int]
    mode: Literal["RGB", "RGBA", "RGBX", "CMYK", "L", "P", "I"]