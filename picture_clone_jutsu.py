import cv2
import os
import albumentations as A
import pandas as pd

print(os.getcwd())
# -----------------------------
# 參數設定
# -----------------------------

input_image_path = r'D:\Codes\VS\PY\small-tools\picture_copy\picts\right_2.png'   # 原始圖片
output_dir = r'D:\Codes\VS\PY\small-tools\picture_copy\result\r'       # 存放增強圖片的資料夾
num_augmented = 20                   # 要生成的圖片數量
label_name = 'right_arrow'             # 標籤名稱 (可以改成右轉或其他)

# 建立資料夾
os.makedirs(output_dir, exist_ok=True)

# -----------------------------
# 定義增強策略
# -----------------------------
transform = A.Compose([
    A.Rotate(limit=30, p=0.5),                  # 隨機旋轉 ±30°
    # A.HorizontalFlip(p=0.5),                    # 隨機水平翻轉
    A.RandomBrightnessContrast(p=0.5),          # 隨機亮度/對比度
    A.ShiftScaleRotate(shift_limit=0.1, scale_limit=0.1, rotate_limit=20, p=0.5),  # 平移+縮放+旋轉
    A.GaussNoise(p=0.2),                        # 隨機加高斯噪聲
    A.Resize(64, 64)                            # 新增：直接生成 64x64
])

# -----------------------------
# 讀取原始圖片
# -----------------------------
image = cv2.imread(input_image_path)
if image is None:
    raise FileNotFoundError(f"找不到圖片: {input_image_path}")

# -----------------------------
# 生成增強圖片並建立 CSV
# -----------------------------
csv_data = []
for i in range(num_augmented):
    augmented = transform(image=image)
    aug_image = augmented['image']
    filename = f'right_{i+1+20}.jpg'
    cv2.imwrite(os.path.join(output_dir, filename), aug_image)
    csv_data.append({'filename': filename, 'label': label_name})

# 建立 CSV
df = pd.DataFrame(csv_data)
csv_path = os.path.join(output_dir, 'labels.csv')
df.to_csv(csv_path, index=False)
print(f"生成完成，共 {num_augmented} 張增強圖片與標籤 CSV，存放於 '{output_dir}'")
