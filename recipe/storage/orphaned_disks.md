# Orphaned Disks Recipe

* [Overview](#overview)
* [Schema](#schema)
* [Example Data](#example-data)
* [Source Data](#source-data)
* [Transformation](#transformation)

## Overview

Best Practice: As an organization, have 90% attached disk (<10% orphaned)

### Sketch
![Overview](overview.jpg)

### PowerBI
![Overview](overview_pbi.jpg)

## Schema

Parameters may include:
* `optimal_percentage` As the target to compare cost

**Single Table**
| Field | Type | Notes |
|-------|------|-------|
| date |   | |
| subscription_name |  | Filter  |
| subscription_id | nvarchar(100) | Filter |
| resource_group | nvarchar(100) | Filter |
| orphaned_disk_count | |
| attached_disk_count | |
| total_disk_count | | Calcuated orphaned + attached 
| attached_disk_percent | | Calculated attached / total | 
| cost | | |
| is_forecast | | Forcasted data |
| is_latest | | Indicates the most recent data |
| is_optimal_forcast | | Indicates optimal forecast |
| forecast_cost | | Calculated cost if record is_forecast=True and is_optimal_forecast=False |
| optimal_cost | | Calculated cost if record is_forecast=True and is_optimal_forecast=True |

**Multi Table**
Latest
| Field | Type | Notes |
|-------|------|-------|
| date |   | |
| subscription_name |  | Filter  |
| subscription_id | nvarchar(100) | Filter |
| resource_group | nvarchar(100) | Filter |
| orphaned_disk_count | |
| attached_disk_count | |
| total_disk_count | | Calcuated orphaned + attached 
| attached_disk_percent | | Calculated attached / total | 
| cost | | |


## Example Data
See full dataset [sample_data.csv](sample_data.csv)

## Source Data

* Azure Graph API Query 
* Detail
    ```
    Resources
    | where type has "microsoft.compute/disks"
    | extend diskState = tostring(properties.diskState)
    | where  diskState == 'Unattached' or managedBy == ""
    | project name, diskState, managedBy, subscriptionId, resourceGroup, location
    ``` 

## Transformation

Transform the source by mapping to new format, apply steps in notes and sort by displayName.

[JMESPath](https://jmespath.org/) notation used to map to fields.

| Field | Source | Notes |
|-------|------|-------|
