# PDF Image Extractor (Simple Image Export from PDFs)

This tool extracts images from PDF files — useful for saving uploaded photos from Jotform forms or other scanned documents. No need to open PDFs manually.

---

## 🧰 What You Need

Before you can use this, you'll need:

1. **Python 3.8 or newer**  
   - You can download it here: https://www.python.org/downloads/
   - Make sure to check the box **“Add Python to PATH”** during installation.

2. **This tool** (a small script)  
   You can download it directly or clone it if you're using Git.

---

## 📦 Setup Instructions

### Option A: Download directly (simple)

1. Click the green “Code” button on this page and select **Download ZIP**  
2. Unzip it to a folder (e.g. `C:\PDFImageExtractor`)

### Option B: Clone with Git (for developers)

```bash
git clone https://github.com/yourusername/pdf-image-extractor.git
cd pdf-image-extractor
```

---

## 🔧 Install Required Package

Open **Command Prompt** (Windows) or **Terminal** (Mac/Linux), then run:

```bash
pip install pymupdf
```

This installs the required image extraction tool.

---

## 🚀 How to Use It

1. Put all your PDF files into a folder (e.g. `C:\PDFs\`)
2. Open Command Prompt (or Terminal)
3. Navigate to where you downloaded the script

```bash
cd C:\PDFImageExtractor
```

4. Run the script like this:

```bash
python extract_images.py C:\PDFs C:\ExtractedImages
```

- Replace `C:\PDFs` with the folder that contains your PDF files.
- Replace `C:\ExtractedImages` with the folder where you want the images to go.

---

## 📁 What You’ll Get

- Each PDF will get its own folder inside your output folder.
- Only PDFs that contain images will be processed.
- Image files will be saved as `.jpg`, `.png`, or whatever format they were embedded as.

---

## ❓ Troubleshooting

- **“pip not recognized”** — Python might not be installed correctly. Try reinstalling and ensure "Add to PATH" is checked.
- **No images extracted** — Some PDFs are scanned images (not embedded images), and won’t work with this tool.
- **Permission denied** — Try running the command prompt as Administrator.

---

## ✅ Example

You have 5 PDFs in `Downloads\Applications\`. You want the images to appear in `Documents\PhotosFromPDFs`.

```bash
python extract_images.py "C:\Users\YourName\Downloads\Applications" "C:\Users\YourName\Documents\PhotosFromPDFs"
```

---

## 📝 License

This tool is free to use and modify (MIT License).
