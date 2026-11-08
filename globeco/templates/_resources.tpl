{{/*
Resource allocation for globeco-allocation-service
*/}}
{{- define "globeco.globecoAllocationServiceResources" -}}
resources:
  requests:
    {{- if eq .Values.autoscaler "vertical-2" }}
    cpu: "100m"
    memory: "200Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "150m"
    memory: "300Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "200m"
    memory: "400Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "250m"
    memory: "500Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "300m"
    memory: "600Mi"
    {{- else }}
    cpu: "50m"
    memory: "100Mi"
    {{- end }}
  limits:
    memory: "6000Mi"
{{- end }}

{{/*
Resource allocation for globeco-confirmation-service
*/}}
{{- define "globeco.globecoConfirmationServiceResources" -}}
resources:
  requests:
    {{- if eq .Values.autoscaler "vertical-2" }}
    cpu: "100m"
    memory: "200Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "150m"
    memory: "300Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "200m"
    memory: "400Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "250m"
    memory: "500Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "300m"
    memory: "600Mi"
    {{- else }}
    cpu: "50m"
    memory: "100Mi"
    {{- end }}
  limits:
    memory: "6000Mi"
{{- end }}

{{/*
Resource allocation for globeco-execution-service
*/}}
{{- define "globeco.globecoExecutionServiceResources" -}}
resources:
  requests:
    {{- if eq .Values.autoscaler "vertical-2" }}
    cpu: "984m"
    memory: "1000Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "1476m"
    memory: "1500Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "1968m"
    memory: "2000Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "2460m"
    memory: "2500Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "2952m"
    memory: "3000Mi"
    {{- else }}
    cpu: "492m"
    memory: "500Mi"
    {{- end }}
  limits:
    memory: "6000Mi"
{{- end }}

{{/*
Resource allocation for globeco-fix-engine
*/}}
{{- define "globeco.globecoFixEngineResources" -}}
resources:
  requests:
    {{- if eq .Values.autoscaler "vertical-2" }}
    cpu: "220m"
    memory: "200Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "330m"
    memory: "300Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "440m"
    memory: "400Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "550m"
    memory: "500Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "660m"
    memory: "600Mi"
    {{- else }}
    cpu: "110m"
    memory: "100Mi"
    {{- end }}
  limits:
    memory: "6000Mi"
{{- end }}

{{/*
Resource allocation for globeco-order-generation-service
*/}}
{{- define "globeco.globecoOrderGenerationServiceResources" -}}
resources:
  requests:
    {{- if eq .Values.autoscaler "vertical-2" }}
    cpu: "468m"
    memory: "800Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "702m"
    memory: "1200Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "936m"
    memory: "1600Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "1170m"
    memory: "2000Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "1404m"
    memory: "2400Mi"
    {{- else }}
    cpu: "234m"
    memory: "400Mi"
    {{- end }}
  limits:
    memory: "6000Mi"
{{- end }}

{{/*
Resource allocation for globeco-order-service
*/}}
{{- define "globeco.globecoOrderServiceResources" -}}
resources:
  requests:
    {{- if eq .Values.autoscaler "vertical-2" }}
    cpu: "578m"
    memory: "2000Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "867m"
    memory: "3000Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "1156m"
    memory: "4000Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "1445m"
    memory: "5000Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "1734m"
    memory: "6000Mi"
    {{- else }}
    cpu: "289m"
    memory: "1000Mi"
    {{- end }}
  limits:
    memory: "6000Mi"
{{- end }}

{{/*
Resource allocation for globeco-portfolio-accounting-service
*/}}
{{- define "globeco.globecoPortfolioAccountingServiceResources" -}}
resources:
  requests:
    {{- if eq .Values.autoscaler "vertical-2" }}
    cpu: "114m"
    memory: "200Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "171m"
    memory: "300Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "228m"
    memory: "400Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "285m"
    memory: "500Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "342m"
    memory: "600Mi"
    {{- else }}
    cpu: "57m"
    memory: "100Mi"
    {{- end }}
  limits:
    memory: "6000Mi"
{{- end }}

{{/*
Resource allocation for globeco-portfolio-management-portal
*/}}
{{- define "globeco.globecoPortfolioManagementPortalResources" -}}
resources:
  requests:
    {{- if eq .Values.autoscaler "vertical-2" }}
    cpu: "1182m"
    memory: "1200Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "1773m"
    memory: "1800Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "2364m"
    memory: "2400Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "2955m"
    memory: "3000Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "3546m"
    memory: "3600Mi"
    {{- else }}
    cpu: "591m"
    memory: "600Mi"
    {{- end }}
  limits:
    memory: "6000Mi"
{{- end }}

{{/*
Resource allocation for globeco-portfolio-service
*/}}
{{- define "globeco.globecoPortfolioServiceResources" -}}
resources:
  requests:
    {{- if eq .Values.autoscaler "vertical-2" }}
    cpu: "2092m"
    memory: "1200Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "3138m"
    memory: "1800Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "4184m"
    memory: "2400Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "5230m"
    memory: "3000Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "6276m"
    memory: "3600Mi"
    {{- else }}
    cpu: "1046m"
    memory: "600Mi"
    {{- end }}
  limits:
    memory: "6000Mi"
{{- end }}

{{/*
Resource allocation for globeco-pricing-service
*/}}
{{- define "globeco.globecoPricingServiceResources" -}}
resources:
  requests:
    {{- if eq .Values.autoscaler "vertical-2" }}
    cpu: "342m"
    memory: "1800Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "513m"
    memory: "2700Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "684m"
    memory: "3600Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "855m"
    memory: "4500Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "1026m"
    memory: "5400Mi"
    {{- else }}
    cpu: "171m"
    memory: "900Mi"
    {{- end }}
  limits:
    memory: "6000Mi"
{{- end }}

{{/*
Resource allocation for globeco-security-service
*/}}
{{- define "globeco.globecoSecurityServiceResources" -}}
resources:
  requests:
    {{- if eq .Values.autoscaler "vertical-2" }}
    cpu: "458m"
    memory: "400Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "687m"
    memory: "600Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "916m"
    memory: "800Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "1145m"
    memory: "1000Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "1374m"
    memory: "1200Mi"
    {{- else }}
    cpu: "229m"
    memory: "200Mi"
    {{- end }}
  limits:
    memory: "6000Mi"
{{- end }}

{{/*
Resource allocation for globeco-trade-service
*/}}
{{- define "globeco.globecoTradeServiceResources" -}}
resources:
  requests:
    {{- if eq .Values.autoscaler "vertical-2" }}
    cpu: "1076m"
    memory: "2200Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "1614m"
    memory: "3300Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "2152m"
    memory: "4400Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "2690m"
    memory: "5500Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "3228m"
    memory: "6600Mi"
    {{- else }}
    cpu: "538m"
    memory: "1100Mi"
    {{- end }}
  limits:
    memory: "6000Mi"
{{- end }}

