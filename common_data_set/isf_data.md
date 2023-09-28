# ISF Data Table

* [Overview](#overview)
* [Schema](#schema)
* [Example Data](#example-data)
* [Source Data](#source-data)
* [Transformation](#transformation)

## Overview
![ISF Data](../docs/RecipesReportsISFData.jpg) 

The ISF Data table provides detailed data for Instance Size Flexibility Ratio.

## Schema
| Field | Type | Notes |
|-------|------|-------|
| ArmSkuName | nvarchar (50) NULL | |
| InstanceSizeFlexibilityGroup | nvarchar (200) NULL | |
| Ratio | Decimal(14,10) | |

## Example Data
See full dataset [/sampledata/ISFRatio.csv](../sampledata/ISFRatio.csv)

| InstanceSizeFlexibilityGroup | ArmSkuName | Ratio |
|------------|------------------------------|-------|
| BS Series High Memory | Standard_B20ms | 40 |
| D Series | Standard_D1 | 1 |
| D Series | Standard_D2 | 2 |
| D Series | Standard_D3 | 4 |
| D Series | Standard_D4 | 8 |
| DSv2 Series High Memory | Standard_DS13-2_v2 | 4 |
| Eav4 Series | Standard_E8a_v4 | 4 |

## Source Data

| Source |  Version | Detail | 
|--------|----------|--------|
| Blob Storage | latest | Download the [ISFRatio file](https://isfratio.blob.core.windows.net/isfratio/ISFRatio.csv).

## Transformation

> No transformation. This is a 1:1 mapping between the source and destination.
