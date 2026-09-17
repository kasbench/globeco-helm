{{/*
Replicas by autoscaler
*/}}
{{- define "globeco.replicas" -}}
{{- if eq .Values.autoscaler "vpa" }}
replicas: 2
{{- else if eq .Values.autoscaler "horizontal-2" }}
replicas: 2
{{- else if eq .Values.autoscaler "horizontal-3" }}
replicas: 3
{{- else if eq .Values.autoscaler "horizontal-4" }}
replicas: 4
{{- else if eq .Values.autoscaler "horizontal-5" }}
replicas: 5
{{- else if eq .Values.autoscaler "horizontal-6" }}
replicas: 6
{{- else if contains "vertical" .Values.autoscaler }}
replicas: 2
{{- else }}
replicas: 1
{{- end }}
{{- end }}