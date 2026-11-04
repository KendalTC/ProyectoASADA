# Abre el .docx en LibreOffice, actualiza la tabla de contenido y exporta a PDF.
import sys, time, subprocess, tempfile, os, uno
from pathlib import Path
sys.path.insert(0, "/root/.claude/skills/synced/cef05cd7-efa1-4b80-b7ff-8d25e994b5d7_cf44cd37-e605-4bf8-9d01-1bea42a660c9/docx/scripts")
from office.soffice import get_soffice_env
from com.sun.star.beans import PropertyValue
src, pdf = map(os.path.abspath, sys.argv[1:3])
prof = tempfile.mkdtemp(prefix="lo_prof_")
proc = subprocess.Popen(["soffice", f"-env:UserInstallation={Path(prof).as_uri()}", "--headless", "--invisible", "--norestore",
                         "--accept=socket,host=127.0.0.1,port=2083;urp;"], env=get_soffice_env())
ctx = None
local = uno.getComponentContext()
resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
for _ in range(60):
    try:
        ctx = resolver.resolve("uno:socket,host=127.0.0.1,port=2083;urp;StarOffice.ComponentContext"); break
    except Exception: time.sleep(1)
smgr = ctx.ServiceManager
desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
def pv(n, v):
    p = PropertyValue(); p.Name = n; p.Value = v; return p
doc = desktop.loadComponentFromURL(Path(src).as_uri(), "_blank", 0, (pv("Hidden", True),))
idx = doc.getDocumentIndexes()
for i in range(idx.getCount()):
    idx.getByIndex(i).update()
doc.refresh()
doc.storeToURL(Path(pdf).as_uri(), (pv("FilterName", "writer_pdf_Export"),))
doc.close(True)
try: desktop.terminate()
except Exception: pass
proc.wait(timeout=30)
print("ok", idx.getCount() if False else "")
