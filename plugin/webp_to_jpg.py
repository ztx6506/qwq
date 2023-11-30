from PIL import Image
def webp_to_jpg(input_path, output_path):
    try:
        # 打开 WebP 图像
        with Image.open(input_path) as img:
            # 将 WebP 图像保存为 JPEG
            img.convert("RGB").save(output_path, "JPEG")
        print(f"Conversion successful: {output_path}")
    except Exception as e:
        print(f"Error converting WebP to JPEG: {e}")

