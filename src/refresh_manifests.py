from pathlib import Path

# Get the current working directory and go up one level to the parent directory
parent_dir = Path.cwd().parent
print("Parent directory: ", parent_dir)

# Get the templates directory in this project (globeco/templates)   
templates_dir = Path.cwd() / "globeco" / "templates"
print("Template directory: ", templates_dir)

# Get all the subdirectories under the parent directory and iterate
for subdir in parent_dir.iterdir():
    if subdir.is_dir():
        # skip if subdirectory name doesn't start with "globeco"
        if not subdir.name.startswith("globeco"):
            continue

        # Look inside the subdirectory to see if there is a subdirectory "k8s_aws", if not continue
        if not (subdir / "k8s_aws").is_dir():
            continue

        # If there is a k8s_aws directory, open a file in it called "k8s.lst"
        manifest_file = subdir / "k8s_aws" / "k8s.lst"
        if manifest_file.exists():
            # Create a directory templates_dir / subdir_name 
            subdir_templates_dir = templates_dir / subdir.name
            subdir_templates_dir.mkdir(exist_ok=True)
            

            # Read the contents of the file line by line
            with open(manifest_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    filename = line.strip()
                    if filename.startswith("#") or filename.startswith("+") or filename.startswith(">") or filename == "":
                        continue

                    # copy the filename to subdir_templates_dir
                    (subdir_templates_dir / filename).write_text((subdir / "k8s_aws" / filename).read_text())




