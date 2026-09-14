from pathlib import Path
import urllib.request
import json
import math
import yaml

    


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
        # print("Editing file: ", file)
        contents = file.read_text()
        contents = contents.replace('monitoring', 'globeco')
        file.write_text(contents)

# Iterate through every file under globeco/templates recursively and change every occurence of the literal 
# "(slice "hpa" "keda")" to "(list "hpa" "keda")"
for file in templates_dir.rglob('*'):
    if file.is_file():
        # print("Editing file: ", file)
        contents = file.read_text()
        contents = contents.replace('(slice "hpa" "keda")', '(list "hpa" "keda")')
        file.write_text(contents)

# Store the contents of json file ../data/cpu_usage.json as a dictionary
cpu_usage = json.load(open('./data/cpu_usage.json'))   

# Update the resource requests and limits in all Deployment manifests

for file in templates_dir.rglob("*"):
    if not file.is_file():
        continue

    try:
        data = yaml.safe_load(file.read_text())
    except yaml.YAMLError:
        continue

    if not isinstance(data, dict):
        continue

    # Filter for globeco Deployment manifests
    if data.get("kind") != "Deployment":
        continue

    name = data.get("metadata", {}).get("name", "")
    if not name.startswith("globeco") or name not in cpu_usage.keys():
        print(f"Skipping {name}")
        continue

    max_cpu = cpu_usage[name]["max"]
    req_m = max(math.ceil(max_cpu * 1000 / 0.70), 50)
    print(f"Name={name}, req_m={req_m}, max_cpu={max_cpu}")

    # Update containers under spec.template.spec.containers
    containers = data.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [])
    for container in containers:
        resources = container.setdefault("resources", {})
        requests = resources.setdefault("requests", {})
        limits = resources.setdefault("limits", {})

        requests["cpu"] = f"{req_m}m"

        # Parse existing CPU limit (millicores or core count)
        raw_limit = str(limits.get("cpu", "")).strip().strip('"')
        if raw_limit:
            if raw_limit.endswith("m"):
                current_limit_m = int(raw_limit[:-1])
            else:
                current_limit_m = int(float(raw_limit) * 1000)

            if current_limit_m <= req_m:
                limits["cpu"] = f"{req_m * 2}m"

    with file.open("w") as f:
        yaml.safe_dump(data, f, sort_keys=False)


# # Iterate through every file under globeco/templates, skip if not a file.  If the file is a deployment manifest,
# # change the resource request to the "max" value in cpu_usage for that deployment's name, converting the value from 
# # cores to millicores by multiplying by 1000 and rounding up. Note that deployment won't always be in the file name. 
# # Look inside the file to see if it is a deployment by looking for `kind: Deployment`.  Ignore deployments that don't
# # start with `globeco` in their name.abs
# for file in templates_dir.rglob('*'):
#     if file.is_file():
#         print("Editing file: ", file)
#         contents = file.read_text()
#         if 'kind: Deployment' in contents and 'globeco' in contents:
#             # Get the deployment name from the metadata.name field
#             lines = contents.split('\n')
#             deployment_name = ""
#             for line in lines:
#                 if 'metadata:' in line:
#                     # Find the next line that starts with "  name:"
#                     for next_line in lines[lines.index(line):]:
#                         if next_line.strip().startswith("name:"):
#                             deployment_name = next_line.strip().split(":")[1].strip()
#                             break
#                     break

#             print("Deployment name: ", deployment_name)
#             if deployment_name in cpu_usage and deployment_name.startswith("globeco"):
#                 # Get the max CPU usage for this deployment
#                 max_cpu = cpu_usage[deployment_name]["max"]
#                 # Convert to millicores
#                 max_cpu_millicores = max(round(max_cpu * 1000/0.70), 50)
#                 print("Max CPU: ", max_cpu, "Millicores: ", max_cpu_millicores)
#                 # Replace the resource request with the new value
#                 # Find the line that contains "requests:" and the next line that contains "cpu:"
#                 # Replace the value after "cpu:" with the new value
#                 lines = contents.split('\n')
#                 for i, line in enumerate(lines):
#                     if 'requests:' in line:
#                         # Find the next line that contains "cpu:"
#                         for j in range(i+1, len(lines)):
#                             if 'cpu:' in lines[j]:
#                                 # Replace the value after "cpu:" with the new value, in double quotes
#                                 lines[j] = lines[j].split(':')[0] + ': ' + '"' + str(max_cpu_millicores) + 'm' + '"'
#                                 break
#                         break
            
#                 # If the limit is less than or equal to the max_cpu_millicores, change the limit to 
#                 # twice the max_cpu_millicores 
#                 for i, line in enumerate(lines):
#                     if 'limits:' in line:
#                         # Find the next line that contains "cpu:"
#                         for j in range(i+1, len(lines)):
#                             if 'cpu:' in lines[j]:
#                                 # If the limit is less than or equal to the max_cpu_millicores, change the limit to
#                                 # twice the max_cpu_millicores
#                                 limit_line = lines[j]
#                                 limit_value = limit_line.split(':')[1].strip().replace('"', '').replace('m', '')
#                                 print("Limit value: ", limit_value)
#                                 if int(limit_value) <= max_cpu_millicores:
#                                     # Replace the value after "cpu:" with the new value, in double quotes
#                                     lines[j] = lines[j].split(':')[0] + ': ' + '"' + str(max_cpu_millicores * 2) + 'm' + '"'
#                                 break
#                         break

#                 contents = '\n'.join(lines)
#                 file.write_text(contents)

# Iterate through every file under globeco/templates, skip if not a file.  If the file is named "vpa.yaml",
# change minAllowed.cpu from 100m to 50m.  
# for file in templates_dir.rglob('vpa.yaml'):
#     print("Editing file: ", file)
#     contents = file.read_text()
#     # Replace "cpu: 100m" with "cpu: 50m"
#     lines = contents.split('\n')
#     for i, line in enumerate(lines):
#         if 'minAllowed:' in line:
#             # Find the next line that contains "cpu:"
#             for j in range(i+1, len(lines)):
#                 if 'cpu:' in lines[j]:
#                     # Replace the value after "cpu:" with "50m"
#                     lines[j] = lines[j].split(':')[0] + ': 50m'
#                     break
#             break

#     contents = '\n'.join(lines)
#     file.write_text(contents)

# spec:
#   targetRef:
#     apiVersion: apps/v1
#     kind: Deployment
#     name: globeco-portfolio-service
#   updatePolicy:
#     updateMode: "InPlaceOrRecreate"
#   resourcePolicy:
#     containerPolicies:
#       - containerName: globeco-portfolio-service
#         minAllowed:
#           cpu: 25m
#           memory: 200Mi
#         maxAllowed:
#           cpu: 2000m
#           memory: 2Gi
#         controlledResources: ["cpu", "memory"]
#         controlledValues: RequestsAndLimits

print()
print("Refreshing VPA")
print()

for file in templates_dir.rglob('vpa.yaml'):
    print("Editing file: ", file)

    # Read the file
    contents = file.read_text()

    # Strip out the lines beginning with "{{"
    contents = '\n'.join([line for line in contents.split('\n') if not line.strip().startswith('{{')])
    
    # load file as a yaml file using the pyaml library
    data = yaml.safe_load(contents)
    
    # Save spec.targetRef.name to a variable `deployment`
    deployment_name = data['spec']['targetRef']['name']
    
    # Get the max CPU usage for this deployment
    max_cpu = cpu_usage[deployment_name]["max"]
    
    # Convert to millicores
    max_cpu_millicores = max(round(max_cpu * 1000/0.70), 50)

    # Replace spec.resourcePolicy.container.policies.containerName.minAllowed.cpu with max_cpu_millicores for all values of containerName
    for container_policy in data['spec']['resourcePolicy']['containerPolicies']:
        container_policy['minAllowed']['cpu'] = str(max_cpu_millicores) + 'm'
        container_policy['maxAllowed']['cpu'] = "6000m"
        container_policy['maxAllowed']['memory'] = "6Gi"

    # Dump the yaml to a string
    data = yaml.dump(data, default_flow_style=False)

    # Prefix the data with the line `{{- if eq .Values.autoscaler "vpa" -}}`
    data = '{{- if eq .Values.autoscaler "vpa" -}}\n' + data

    # Add the line `{{- end -}}` at the end
    data = data + '{{- end -}}\n'

    # Write the file
    file.write_text(data)



    





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


    



