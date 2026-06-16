import os
from pathlib import Path
from builder.core import show_pipeline, process, shared_config
from builder.loader import load
from builder import tools # needed to register all tools

prevwd = os.getcwd()
os.chdir(Path(__file__).parent)
#shared_config["retry_cache"] = True
list_paths = ["lists/biodata_group.txt", "lists/mever_group.txt"]
pipeline = [
    "builder.tools.github.get_stars", # COMMENT THIS LINE FOR TESTING BECAUSE IT DOES NOT CACHE
    "builder.tools.format.bootstrap.banner",
    "builder.tools.generic.sort",
    "builder.tools.github.add_readme",
    "builder.tools.github.add_license",
    "builder.tools.generic.cache",
    "builder.tools.generic.get_md",
    "builder.tools.generic.remove_section_images",
    "builder.tools.index.keywords",
    "builder.tools.format.bootstrap.create_previews",
    "builder.tools.index.keep_common_sections",
    #"builder.tools.format.bootstrap.keywords",
    "builder.tools.format.bootstrap.short_sections",
    "builder.tools.format.bootstrap.container",
]
show_pipeline(pipeline)
entries = list()
for list_path in list_paths:
    entries.extend(load(list_path))
text = process(entries, pipeline)
template = Path("template.html").read_text()
output_dir = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site"))
out_file = Path(output_dir/"docs/project/software.html")
catalogue = template.replace("{{CONTENTS}}", text)
html = out_file.read_text(encoding="utf-8")
html = html.replace("</body>", catalogue + "\n</body>", 1)
out_file.write_text(html, encoding="utf-8")