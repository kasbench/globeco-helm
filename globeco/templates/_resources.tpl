{{/*
Resource allocation for globeco-allocation-service
*/}}
{{- define "globeco.globecoAllocationServiceResources" -}}
resources:
  requests:
    {{- if eq .Values.autoscaler "vertical-2" }}
    cpu: "75m"
    memory: "150Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "100m"
    memory: "200Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "125m"
    memory: "250Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "150m"
    memory: "300Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "175m"
    memory: "350Mi"
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
    cpu: "75m"
    memory: "150Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "100m"
    memory: "200Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "125m"
    memory: "250Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "150m"
    memory: "300Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "175m"
    memory: "350Mi"
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
    cpu: "738m"
    memory: "750Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "984m"
    memory: "1000Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "1230m"
    memory: "1250Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "1476m"
    memory: "1500Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "1722m"
    memory: "1750Mi"
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
    cpu: "165m"
    memory: "150Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "220m"
    memory: "200Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "275m"
    memory: "250Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "330m"
    memory: "300Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "385m"
    memory: "350Mi"
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
    cpu: "351m"
    memory: "600Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "468m"
    memory: "800Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "585m"
    memory: "1000Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "702m"
    memory: "1200Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "819m"
    memory: "1400Mi"
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
    cpu: "433m"
    memory: "1500Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "578m"
    memory: "2000Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "722m"
    memory: "2500Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "867m"
    memory: "3000Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "1011m"
    memory: "3500Mi"
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
    cpu: "85m"
    memory: "150Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "114m"
    memory: "200Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "142m"
    memory: "250Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "171m"
    memory: "300Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "199m"
    memory: "350Mi"
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
    cpu: "886m"
    memory: "900Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "1182m"
    memory: "1200Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "1477m"
    memory: "1500Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "1773m"
    memory: "1800Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "2068m"
    memory: "2100Mi"
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
    cpu: "1569m"
    memory: "900Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "2092m"
    memory: "1200Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "2615m"
    memory: "1500Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "3138m"
    memory: "1800Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "3661m"
    memory: "2100Mi"
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
    cpu: "256m"
    memory: "1350Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "342m"
    memory: "1800Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "427m"
    memory: "2250Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "513m"
    memory: "2700Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "598m"
    memory: "3150Mi"
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
    cpu: "343m"
    memory: "300Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "458m"
    memory: "400Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "572m"
    memory: "500Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "687m"
    memory: "600Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "801m"
    memory: "700Mi"
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
    cpu: "807m"
    memory: "1650Mi"
    {{- else if eq .Values.autoscaler "vertical-3" }}
    cpu: "1076m"
    memory: "2200Mi"
    {{- else if eq .Values.autoscaler "vertical-4" }}
    cpu: "1345m"
    memory: "2750Mi"
    {{- else if eq .Values.autoscaler "vertical-5" }}
    cpu: "1614m"
    memory: "3300Mi"
    {{- else if eq .Values.autoscaler "vertical-6" }}
    cpu: "1883m"
    memory: "3850Mi"
    {{- else }}
    cpu: "538m"
    memory: "1100Mi"
    {{- end }}
  limits:
    memory: "6000Mi"
{{- end }}

