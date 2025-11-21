# ASCII Art Generator

A Python script that converts images to ASCII art using the Pillow library.

## Features

- Convert any image to ASCII art
- Adjustable output width
- Optional colored output (blue)
- Preview functionality
- Save ASCII art to text files

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Install the required dependency:
```bash
pip install Pillow
```

2. Clone or download the script to your local machine.

## Usage

### Basic Usage

The script is configured to convert an image from the `assets/dp.png` path by default:

```bash
python script_name.py
```

### Customization

To use with your own images, modify the main section of the script:

```python
if __name__ == "__main__":
    # Replace "your_image.png" with your image path
    ascii_art = image_to_ascii("your_image.png", width=50)
    
    if ascii_art:
        print("🔹 Preview:\n")
        print(ascii_art[:1500])  # preview only first 1500 characters
        save_ascii(ascii_art, "output.txt", color=True)
```

### Parameters

- `path`: Path to the input image file
- `width`: Width of the ASCII output (default: 50 characters)
- `out_path`: Output file path (default: "ascii_logo.txt")
- `color`: Whether to add color to the output (default: False)

## Functions

### `image_to_ascii(path, width=50)`
Converts an image to ASCII art.

### `save_ascii(ascii_str, out_path="ascii_logo.txt", color=False)`
Saves ASCII art to a file with optional coloring.

## Example Output

The script will:
1. Display a preview of the ASCII art (first 1500 characters)
2. Save the complete ASCII art to a text file
3. Show confirmation messages for successful operations

## Error Handling

- File not found detection
- General exception handling with descriptive error messages

## Character Mapping

The ASCII characters are mapped from dark to light:
`"@%#*+=-:. "`

Where:
- `@` represents the darkest pixels
- ` ` (space) represents the lightest pixels

## License

This project is open source and available under the [MIT License](LICENSE).
