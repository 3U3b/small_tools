from PIL import Image
import qrcode
import os

nowpath = os.getcwd()

def setQRcode(data="testing",name="qrcode.png",saveing=nowpath,logo=None):
    # PIL for logo img     ".png"
    qr_data = data # "<test text>"
    qr_name = name 
    save_path = saveing
    logo_data = logo # "<your img>.png"
        
    qr = qrcode.QRCode(
        version=10,  # 控制 QR Code 的大小
        error_correction=qrcode.constants.ERROR_CORRECT_L,   # 錯誤修正級別L<M<Q<H
        box_size=5,  # 每個小方塊的像素大小
        border=1,  # 邊框大小
    )
    # 添加數據
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    return qr,qr_name,save_path,logo_data

def createQRcode(qr,qr_name,save_path,logo_data):

    # 創建圖像
    # img = qr.make_image(fill_color="darkgray", back_color="white") # 白底 (填黑色會造成logo是黑白的)
    img = qr.make_image(fill_color="white", back_color="black")

    # 要嵌入的圖片logo
    if logo_data:
        logo = Image.open(logo_data).convert("RGBA")
        qr_width, qr_height = img.size
        logo_size = 80
        # logo_size = int(qr_width / 4)  # 使 logo 大小為 QRcode 的 1/4
        logo = logo.resize((logo_size, logo_size), Image.NEAREST) # LANCZOS>BILINEAR>NEAREST 抗鋸齒濾波器 在縮小圖像時保持清晰度
        # 定位
        logo_position = (
            (qr_width - logo_size) // 2,
            (qr_height - logo_size) // 2,
        )
        # img.paste(logo, (int((qr_width - logo_size) / 2), int((qr_height - logo_size) / 2))) # 貼上(透明背景被填滿)
        img.paste(logo, logo_position,logo) # 背景保持透明
    # 保存圖像
    img.save(rf"{save_path}\{qr_name}") # 使用原始字串： 將字串前面加上 r

    print(f"QR code 已成功生成 => {qr_name}至{save_path}資料夾")

