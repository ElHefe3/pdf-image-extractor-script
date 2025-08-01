# PDF Image Extractor

A command-line tool for extracting embedded images from all PDF files in a given folder.

## Features

- Processes all `.pdf` files in a specified input folder
- Creates a separate subfolder for each PDF (named after the file)
- Extracts and saves all images found in each PDF using [PyMuPDF](https://pymupdf.readthedocs.io/)
- Skips PDFs that contain no images (no output folder created)

## Requirements

- Python 3.8+
- [`PyMuPDF`](https://pypi.org/project/PyMuPDF/)

Install via pip:

```bash
pip install pymupdf
```

## Usage

```bash
python extract_images.py <pdf_folder> <output_folder>
```

- `<pdf_folder>`: Path to the folder containing `.pdf` files
- `<output_folder>`: Destination folder where images will be saved

### Example

```bash
python extract_images.py ./inbox ./extracted
```

- All PDFs in `./inbox` will be processed
- Extracted images will be saved to `./extracted/<PDF_NAME>/`

Each image file will be named like:

```
PDFNAME_p1_img1.jpg
PDFNAME_p2_img2.png
```

## Output Behavior

- If a PDF has no extractable images, it will be skipped
- For PDFs with images:
  - A subfolder will be created inside `<output_folder>`
  - Images are saved in their original format (`jpg`, `png`, etc.)

## Notes

- The script only looks at the first-level `.pdf` files in the input directory (no recursion)
- Works best with PDFs that contain embedded images (not scanned or rasterized PDFs)

## License

MIT — free to use, modify, and distribute.
```
