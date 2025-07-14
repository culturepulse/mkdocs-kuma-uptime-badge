# Advanced Examples

This page demonstrates more advanced usage of the MkDocs Uptime Badge Plugin.

## Different Badge Types

### Status Badge (Default)

{{uptime id=1}}

### Uptime Badge

{{uptime id=2 type=uptime hours=24}}

### Ping Badge

{{uptime id=3 type=ping hours=24}}

### Average Response Time Badge

{{uptime id=4 type=avg-response hours=24}}

### Certificate Expiry Badge

{{uptime id=5 type=cert-exp}}

### Response Badge

{{uptime id=6 type=response}}

## Custom Duration

### 24 Hours

{{uptime id=7 type=uptime hours=24}}

### 7 Days

{{uptime id=8 type=uptime hours=168}}

### 30 Days

{{uptime id=9 type=uptime hours=720 label="30" labelSuffix="d"}}

## Custom Styling

### Different Badge Styles

Default (flat):
{{uptime id=10}}

Flat Square:
{{uptime id=11 style=flat-square}}

Plastic:
{{uptime id=12 style=plastic}}

For The Badge:
{{uptime id=13 style=for-the-badge}}

Social:
{{uptime id=14 style=social}}

### Custom Labels and Colors

{{uptime id=15 labelPrefix="My" label="Service" labelSuffix="Status" color="blue" labelColor="gray"}}

## Special Characters

{{uptime id=16 upLabel="Service & API" downLabel="Down & Out"}}

## Multiple Badges on One Line

Status: {{uptime id=17}} | Uptime: {{uptime id=18 type=uptime hours=24}} | Ping: {{uptime id=19 type=ping hours=24}}
