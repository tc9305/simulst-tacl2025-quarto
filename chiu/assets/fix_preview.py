"""Apply the shared SimulST fix to this deck's embedded speaker HTML."""

from pathlib import Path
import sys

folder = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(folder.parent / "scripts"))
from fix_slide_preview import fix_html

slide = folder / "seamless_streaming_progress.html"
original = slide.read_bytes().decode("utf-8")
fixed = fix_html(original)
if fixed != original:
    slide.write_bytes(fixed.encode("utf-8"))
print("Streaming_chu: embedded speaker HTML is safe for Live Server preview.")
