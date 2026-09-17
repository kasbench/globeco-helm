from pathlib import Path
import urllib.request
import json
import yaml
import re
    

microservices = ["globeco-allocation-service",
    "globeco-confirmation-service",
    "globeco-execution-service",
    "globeco-fix-engine",
    "globeco-order-generation-service",
    "globeco-order-service",
    "globeco-portfolio-accounting-service",
    "globeco-portfolio-management-portal",
    "globeco-portfolio-service",
    "globeco-pricing-service",
    "globeco-security-service",
    "globeco-trade-service",
    ]

def to_camel_case(text: str) -> str:
    # Replace hyphens and underscores with spaces, then split into words
    words = re.sub(r'[-_]+', ' ', text).split()
    
    if not words:
        return ""
    
    # Lowercase the first word, capitalize the rest, and join them
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])




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
memory_usage = json.load(open('./data/memory_usage.json'))



# Adjust all VPA policies to match actual CPU usage for each deployment

for file in templates_dir.rglob('vpa.yaml'):
    # print("Editing file: ", file)

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



with open("./globeco/templates/_resources.tpl", "w", encoding="utf-8") as tpl:
    for microservice in microservices:
        # convert microservice name to camel case
        microservice_cc = to_camel_case(microservice)
        
        # generate the template comment for the microservice
        tpl.write("{{/*\n")
        tpl.write(f"Resource allocation for {microservice}\n")
        tpl.write("*/}}\n")
        
        # generate the define statment for the microservice resource
        tpl.write("{{- ") 
        tpl.write(f'define "globeco.{microservice_cc}Resources"')
        tpl.write(" -}}\n")
        
        # calculate the cpu allocation request
        max_cpu = cpu_usage[microservice]["max"]
        max_cpu_millicores = max(round(max_cpu * 1000/0.70), 50)
        
        # calculate the memory allocatin request
        max_mem_mi = memory_usage[microservice]["max"]/0.70
        # round up to the nearest 100
        max_mem_mi = int(max_mem_mi) + (100 - int(max_mem_mi) % 100)
        # print(f"{microservice}: {max_cpu_millicores}m")
        # print()
        tabs = " " * 10
        tabs = ""
        tpl.write(tabs + "resources:\n")
        tpl.write(tabs + "  requests:\n")
        for i in range(2,7):
            cpu_request = max_cpu_millicores * ((i+1) * 0.5)
            mem_request = max_mem_mi * ((i+1) * 0.5)
            if i == 2:
                tpl.write(tabs + "    {{- if eq .Values.autoscaler \"vertical-" + str(i) + "\" }}\n")    
            else:
                tpl.write(tabs + "    {{- else if eq .Values.autoscaler \"vertical-" + str(i) + "\" }}\n")    
            tpl.write(tabs + f"    cpu: \"{int(cpu_request)}m\"\n")
            tpl.write(tabs + f"    memory: \"{int(mem_request)}Mi\"\n")
        
        tpl.write(tabs + "    {{- else }}\n")
        tpl.write(tabs + f"    cpu: \"{int(max_cpu_millicores)}m\"\n")
        tpl.write(tabs + f"    memory: \"{int(max_mem_mi)}Mi\"\n")
        tpl.write(tabs + "    {{- end }}\n")
        tpl.write(tabs + "  limits:\n")
        # print(tabs + f"    memory: \"{mem_request}Mi\"")
        tpl.write(tabs + f"    memory: \"6000Mi\"\n")
        tpl.write("{{- end }}\n\n") 
        
    





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


    



