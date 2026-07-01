from pathlib import Path
from PIL import Image, ImageOps

# 透過更改解析度、照片品質達到保持比例且肉眼乍看下無太大傷害

src = Path(r"要將照片減肥的存放資料夾路徑")
dst = Path(r"照片減肥後存放的資料夾路徑")

dst.mkdir(exist_ok=True)

for file in src.glob("*.jpg"):
    img = Image.open(file)
    w, h = img.size
    
    # 套用 EXIF 旋轉資訊
    img = ImageOps.exif_transpose(img) #避免照片沒有真的旋轉，只是靠 EXIF 標記
    img.thumbnail((w // 2, h // 2)) # 限制最大尺寸，並保持比例

    # 縮放倍率
    '''
    img = img.resize(
        (w // 2, h // 2),
        Image.Resampling.LANCZOS
    )
    '''
    
    out = dst / file.name

    img.save(
        out,
        quality=70,
        optimize=True
    )

print("完成")