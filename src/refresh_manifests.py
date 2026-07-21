from pathlib import Path
import urllib.request


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


# Iterate through every file under globeco/templates recursively and change every occurence of the literal "monitoring" to "globeco"
for file in templates_dir.rglob('*'):
    if file.is_file():
        print("Editing file: ", file)
        contents = file.read_text()
        contents = contents.replace('monitoring', 'globeco')
        file.write_text(contents)



# Special logic for the Prometheus valuse file

# prometheus_values_file = parent_dir / "globeco-observability" / "k8s_aws" / "values_prometheus.yaml"
# print("Prometheus values file: ", prometheus_values_file)
# if prometheus_values_file.exists():
#     # Edit the globeco/values.yaml file by deleting everything between 
#     # "# START PROMETHEUS VALUES" and "# END PROMETHEUS VALUES" and replacing it with the contents of the prometheus-values.yaml file
#     # The section starts with "prometheus:" and is followed by the content of the file.  
#     # Each line of the file must be indented two spaces.  
#     values_file = Path.cwd() / "globeco" / "values.yaml"
#     print("Values file: ", values_file)

#     if values_file.exists():
#         print("Editing values file...")
#         with open(values_file, 'r') as f:
#             lines = f.readlines()

#         with open(values_file, 'w') as f:
#             write = True
#             for line in lines:
#                 if line.strip() == "# START PROMETHEUS VALUES":
#                     write = False
#                     f.write(line)
#                     f.write("prometheus:\n")
#                     # read the prometheus-values.yaml file and write it to the values.yaml file with 2 space indentation
#                     with open(prometheus_values_file, 'r') as pf:
#                         pf_lines = pf.readlines()
#                         for pf_line in pf_lines:
#                             f.write("  " + pf_line)
#                 elif line.strip() == "# END PROMETHEUS VALUES":
#                     write = True
#                     f.write(line)
#                 elif write:
#                     f.write(line)

# Special logic for OpenTelemetry
# cert-manager and opentelemetry-operator are installed as prerequisites (not as Helm templates)
# because their CRDs must exist before the main chart can reference them.
# Install them separately before deploying this chart:
#   helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace --set installCRDs=true
#   helm install opentelemetry-operator open-telemetry/opentelemetry-operator --namespace opentelemetry-operator-system --create-namespace


    



