# Charge Back Shared Resources Log Analytics Recipe

* [Overview](#overview)
* [Schema](#schema)
* [Example Data](#example-data)
* [Source Data](#source-data)
* [Transformation](#transformation)

## Overview

Charge Back: As an organization, charge back the cost of shared Log Analtyics workspaces by subscription and `BillableDataBytes`.

### Sketch
![Overview Sketch](https://dummyimage.com/300x300/fff/aaa)

### PowerBI
![Overview PowerBi](https://dummyimage.com/300x300/fff/aaa)

## Schema

Parameters may include:

**Single Table**
| Field | Type | Notes |
|-------|------|-------|
| tbd |   | |


## Example Data
See full dataset [sample_data.csv](sample_data.csv)

## Source Data

API https://learn.microsoft.com/en-us/azure/azure-monitor/logs/api/overview


**Azure Graph API Query**
```kql
union withsource = t *
| where TimeGenerated between(datetime("2023-01-01 00:00:00") .. datetime("2023-01-01 23:59:59"))
| where _IsBillable == true
| parse _ResourceId with "/subscription/" suscriptionid "/"
| summarize BillableDataBytes = sum(_BilledSize) by subscriptionid
| sort by subscriptionid nulls last
``` 

## Transformation

Transform the source by mapping to new format, apply steps in notes and sort by displayName.

[JMESPath](https://jmespath.org/) notation used to map to fields.

| Field | Source | Notes |
|-------|------|-------|

