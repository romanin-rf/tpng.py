import os
import json
import base64
from collections import namedtuple
from PIL import Image

class _func:
	def named_tuple(name: str, data: dict) -> namedtuple:
		"""Accepts the `name` of a future `namedtuple` and `data` in the form of a `dict`"""
		return namedtuple(name, data.keys())(*data.values())

	def ascii_handler(ascii_lines: str, *, _pass: str=" ") -> list[str]:
		ascii_lines = ascii_lines.split("\n")
		x = 0
		for line in ascii_lines:
			if len(line) > x:
				x = len(line)

		# Convert
		ascii_lines_done = []
		for line in ascii_lines:
			ascii_lines_done.append(line + (_pass * (x - len(line))))

		return ascii_lines_done
	
	def get_image_size(lines_list: list) -> tuple[int, int]:
		width, height = 0, len(lines_list)
		for i in lines_list:
			width += len(i)
		width = int(width / height)
		return width, height

class _data:
	tpnginfo = namedtuple("tpnginfo", ["datatype", "mode", "size"])

class TPNG():
	def __init__(self, filename: str) -> None:
		self.filename = filename
		defult = "tpng|rgb|1x1|ffffff,*"
		if os.path.exists(filename):
			with open(filename, "rb") as tpngfile:
				self.filedata = tpngfile.read().decode()
		else:
			with open(filename, "wb") as tpngfile:
				self.filedata = defult
				tpngfile.write(defult.encode())

	def get_info(self) -> _data.tpnginfo:
		info = self.filedata.split("|")
		size = info[2].split("x")
		return _func.named_tuple("tpnginfo", {"datatype": info[0], "mode": info[1], "size": [int(size[0]), int(size[1])]})

	def get_data(self) -> list[list[str]]:
		data = self.filedata.split("|")[-1]
		pixels = data.split("*")
		wag = 0
		for i in pixels:
			pixels[wag] = i.split(",")
			wag += 1
		return pixels

	def upload_data(self, data: list[list[str]]) -> bool:
		data_for_upload = ["tpng", "rgb", "", ""]
		x, y = 0, len(data)
		for i in data:
			x += len(i)
		if x % y == 0:
			x = int(x / y)
			data_for_upload[2] = "x".join([str(x), str(y)])
			wag_line = 1
			for line in data:
				wag_pixel = 1
				for pixel in line:
					data_for_upload[-1] += pixel + ("," if (wag_pixel != x) else "")
					wag_pixel += 1
				data_for_upload[-1] += ("*" if (wag_line != y) else "")
				wag_line += 1
			data_for_upload = "|".join(data_for_upload)
			with open(self.filename, "wb") as tpngfile:
				tpngfile.write(data_for_upload.encode())
			return True
		else:
			return False

	def upload_from_ascii(self, _ascii: str, *, _pass: str=" ", ctw: dict=None, progress_adaptive=None) -> bool:
		lines = _func.ascii_handler(_ascii, _pass=_pass)
		image = []
		pixels_wag = 0
		width, height = _func.get_image_size(lines)

		for line in lines:
			lline = []
			for pixel in line:
				if pixel == _pass:
					lline.append("000000")
				else:
					if ctw == None:
						lline.append("ffffff")
					else:
						if pixel in list(ctw.keys()):
							lline.append(str(ctw[pixel]))
						else:
							lline.append("ffffff")
				pixels_wag += 1
				progress_adaptive(pixels_wag, width * height) if (progress_adaptive != None) else None
			image.append(lline)
		return self.upload_data(image)
	
	def upload_from_png(self, ipath: str, *, progress_adaptive=None) -> bool:
		image = Image.open(ipath)
		width, height = image.size
		pixels = []
		pixels_wag = 0

		for y in range(height):
			line = []
			for x in range(width):
				pixel = bytearray(image.getpixel((x, y))).hex()
				if len(pixel) > 6:
					pixel = pixel[:-2]
				line.append(pixel)
				pixels_wag += 1
				progress_adaptive(pixels_wag, width * height) if (progress_adaptive != None) else None
			pixels.append(line)

		return self.upload_data(pixels)

	def get_image_rich(self, pixel_format: str="██") -> str:
		pixels = self.get_data()
		text = ""
		for line in pixels:
			for pixel in line:
				text += f"[#{pixel}]{pixel_format}[/]"
			text += "\n"
		return text

# "5x2|rgb|tpng|data"
# [["ffffff"]]