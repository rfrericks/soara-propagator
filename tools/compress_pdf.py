#!/usr/bin/env python3
"""Shrink a rendered Propagator PDF by recompressing its embedded photos.

WeasyPrint embeds photos at their full source resolution/quality, which is
usually far more than a 7in-wide printed column needs and can push a
photo-heavy issue's PDF to 2MB+ -- more than some sites/inboxes are happy
with. This only touches large embedded JPEGs: it downsamples them to a
print-appropriate size and re-encodes at a slightly lower JPEG quality.
Vector text, tables, and small/already-efficient images (icons, the
masthead logo) are left alone.

Usage:
    python tools/compress_pdf.py issues/2026-09/Propagator-2026-09.pdf
    python tools/compress_pdf.py issues/2026-09/Propagator-2026-09.pdf -o out.pdf
    python tools/compress_pdf.py issues/2026-09/Propagator-2026-09.pdf --dry-run

Default behavior overwrites the input file in place (matching the published
filename convention in docs/generation-guide.md -- run this right after
build_pdf.py); use -o to write elsewhere, or --dry-run to preview the size
reduction without writing anything.

Dependencies: pikepdf, Pillow
    pip install pikepdf Pillow --break-system-packages
"""
import argparse
import io
import shutil
import sys
import tempfile
from pathlib import Path

try:
    import pikepdf
    from PIL import Image
except ImportError as e:  # pragma: no cover
    sys.exit(f"Missing dependency: {e}. Run: pip install pikepdf Pillow")

# A photo wider/taller than this (px) gets downsampled -- plenty for a
# 7in-wide printed column at a couple hundred DPI.
MAX_DIM_LARGE = 1200
QUALITY_LARGE = 65
# Smaller photos (already close to their display size) just get re-encoded
# at a gentler quality, without resizing.
MAX_DIM_SMALL = 900
QUALITY_SMALL = 75


def compress(src: Path, dst: Path, dry_run=False):
    pdf = pikepdf.open(src)
    n = 0
    saved = 0

    for obj in pdf.objects:
        try:
            if obj.get("/Subtype") != pikepdf.Name("/Image"):
                continue
        except Exception:
            continue
        if obj.get("/Filter") != pikepdf.Name("/DCTDecode"):
            continue  # not a JPEG (e.g. the masthead logo) -- leave it alone

        w = int(obj.get("/Width", 0))
        h = int(obj.get("/Height", 0))
        before = len(obj.read_raw_bytes())

        large = max(w, h) > MAX_DIM_SMALL
        max_dim = MAX_DIM_LARGE if large else MAX_DIM_SMALL
        quality = QUALITY_LARGE if large else QUALITY_SMALL

        pil = pikepdf.PdfImage(obj).as_pil_image().convert("RGB")
        scale = min(1.0, max_dim / max(pil.width, pil.height))
        new_size = (max(1, round(pil.width * scale)), max(1, round(pil.height * scale)))
        if scale < 1.0:
            pil = pil.resize(new_size, Image.LANCZOS)

        buf = io.BytesIO()
        pil.save(buf, format="JPEG", quality=quality, optimize=True)
        jpeg_bytes = buf.getvalue()

        if len(jpeg_bytes) >= before:
            continue  # re-encoding didn't actually help -- leave the original

        if not dry_run:
            obj.write(jpeg_bytes, filter=pikepdf.Name("/DCTDecode"))
            obj["/Width"] = new_size[0]
            obj["/Height"] = new_size[1]
            obj["/ColorSpace"] = pikepdf.Name("/DeviceRGB")
            obj["/BitsPerComponent"] = 8

        saved += before - len(jpeg_bytes)
        n += 1
        print(f"  {w}x{h} ({before / 1024:.0f}KB) -> {new_size[0]}x{new_size[1]} "
              f"q{quality} ({len(jpeg_bytes) / 1024:.0f}KB)")

    before_total = Path(src).stat().st_size
    if dry_run:
        print(f"[dry run] {n} image(s) would shrink by ~{saved / 1024:.0f}KB "
              f"({before_total / 1024:.0f}KB -> ~{(before_total - saved) / 1024:.0f}KB)")
        return

    # Save to a temp file first so a failure never leaves a half-written PDF.
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    pdf.save(tmp_path, compress_streams=True,
              object_stream_mode=pikepdf.ObjectStreamMode.generate, linearize=False)
    shutil.move(str(tmp_path), str(dst))

    after_total = dst.stat().st_size
    print(f"Recompressed {n} image(s). {before_total / 1024:.0f}KB -> {after_total / 1024:.0f}KB "
          f"({(1 - after_total / before_total) * 100:.0f}% smaller)")


def main():
    ap = argparse.ArgumentParser(description="Shrink a Propagator PDF's embedded photos.")
    ap.add_argument("source", help="path to the rendered PDF")
    ap.add_argument("-o", "--output", help="output path (default: overwrite source)")
    ap.add_argument("--dry-run", action="store_true", help="report savings without writing")
    args = ap.parse_args()

    src = Path(args.source).resolve()
    if not src.exists():
        sys.exit(f"Not found: {src}")
    dst = Path(args.output).resolve() if args.output else src

    compress(src, dst, dry_run=args.dry_run)


if __name__ == "__main__":
    main()

# end of compress_pdf.py
