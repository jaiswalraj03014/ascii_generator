from PIL import Image
import os

ASCII_CHARS = "@%#*+=-:. "  # dark → light

def image_to_ascii(path, width=50):
    if not os.path.exists(path):
        print(f"❌ File not found: {path}")
        return ""

    try:
        img = Image.open(path).convert("L")
        w, h = img.size
        img = img.resize((width, int(h / w * width * 0.55)))
        pixels = img.getdata()
        chars = "".join(ASCII_CHARS[p * (len(ASCII_CHARS)-1) // 255] for p in pixels)
        ascii_img = "\n".join(chars[i:i+img.width] for i in range(0, len(chars), img.width))
        return ascii_img
    except Exception as e:
        print(f"❌ Error: {e}")
        return ""

def save_ascii(ascii_str, out_path="ascii_logo.txt", color=False):
    if color:
        ascii_str = f"\033[94m{ascii_str}\033[0m"
    with open(out_path, "w") as f:
        f.write(ascii_str)
    print(f"✅ Saved to {out_path}")

if __name__ == "__main__":
    ascii_art = image_to_ascii("assets/trigslink-logo.png", width=50)
    if ascii_art:
        print("🔹 Preview:\n")
        print(ascii_art[:1500])  # preview only first 1500 characters
        save_ascii(ascii_art, "ascii_logo.txt", color=True)