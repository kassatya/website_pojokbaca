from PIL import Image

def analyze_png(path):
    img = Image.open(path)
    print(f"Path: {path}")
    print(f"Size: {img.size}")
    print(f"Mode: {img.mode}")
    if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
        print("Has alpha/transparency channel")
    else:
        print("NO alpha/transparency channel")
        
    img_rgba = img.convert("RGBA")
    # check corner color
    print("Top-left pixel:", img_rgba.getpixel((0, 0)))
    print("Middle pixel:", img_rgba.getpixel((img.size[0] // 2, img.size[1] // 2)))
    print("-" * 40)

analyze_png("logo_kkn.png")
analyze_png("logo_upn.png")
