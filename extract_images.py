import fitz  # PyMuPDF
import sys
from pathlib import Path

def extract_images_from_pdf(pdf_path: Path, output_base_dir: Path):
    base_name = pdf_path.stem.replace(" ", "_")
    output_dir = output_base_dir / base_name
    doc = fitz.open(pdf_path)
    image_count = 0

    for page_number, page in enumerate(doc, start=1):
        for img_index, img in enumerate(page.get_images(full=True), start=1):
            if image_count == 0:
                output_dir.mkdir(parents=True, exist_ok=True)
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            filename = f"{base_name}_p{page_number}_img{img_index}.{image_ext}"
            output_path = output_dir / filename
            with open(output_path, "wb") as f:
                f.write(image_bytes)
            print(f"[+] {filename}")
            image_count += 1

    return image_count

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_images.py <pdf_folder> <output_folder>")
        sys.exit(1)

    pdf_folder = Path(sys.argv[1])
    output_base_dir = Path(sys.argv[2])
    output_base_dir.mkdir(parents=True, exist_ok=True)

    if not pdf_folder.exists() or not pdf_folder.is_dir():
        print(f"[!] Folder does not exist: {pdf_folder}")
        sys.exit(1)

    pdf_files = list(pdf_folder.glob("*.pdf"))
    if not pdf_files:
        print("⚠️  No PDF files found in the folder.")
        sys.exit(0)

    for pdf_file in pdf_files:
        print(f"\n📄 Extracting from: {pdf_file.name}")
        try:
            count = extract_images_from_pdf(pdf_file, output_base_dir)
            if count == 0:
                print("⚠️  No images found. No folder created.")
            else:
                print(f"✅ Done. {count} image(s) extracted.")
        except Exception as e:
            print(f"[!] Error processing {pdf_file.name}: {e}")

