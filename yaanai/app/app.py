from wand.image import Image as WandImage

from PIL import Image as PILImage

from pytesseract import image_to_string
import pytesseract

# # with open('/app/app/sample_ms.pdf', 'rb+') as fo:
# with WandImage(filename='/app/app/sample_ms.pdf', resolution=300) as img:
#     img.units = 'pixelsperinch'
#     img.compression_quality = 70
#     # img.convert('png')
#     img.save(filename='/app/app/sample_ms_out.png')


with PILImage.open('/app/app/sample_ms_out-0.png') as fo:
    print(image_to_string(fo, config='--psm 6'))

