from pathlib import Path
import zipfile, hashlib
base=Path("WoolixPack-Mobs.zip")
assert hashlib.sha1(base.read_bytes()).hexdigest()=="5a07984fd80ba1904cb77386752ec44fb40a3e25"
with zipfile.ZipFile(base) as source, zipfile.ZipFile("WoolixPack-Hotbar.zip", "w", zipfile.ZIP_DEFLATED) as out:
    for entry in source.infolist():
        patch=Path("hud-hotbar") / entry.filename
        out.writestr(entry, patch.read_bytes() if patch.is_file() else source.read(entry))
with zipfile.ZipFile("WoolixPack-Hotbar.zip") as out:
    assert out.testzip() is None
print(hashlib.sha1(Path("WoolixPack-Hotbar.zip").read_bytes()).hexdigest())
