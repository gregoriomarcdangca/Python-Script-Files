import re
from pathlib import Path
#foldervariable
folder = "C:\\Users\\marcg\\Desktop\\CLEANER"
folder_path = Path(folder)
#filelist
folder_1 = [p for p in folder_path.iterdir() if p.is_file()]
#read content
for file_path in folder_1:
    content = file_path.read_text(encoding="utf-8")
    cleaned = re.sub(r"#", " ", content)
    file_path.write_text(cleaned, encoding="utf-8")

