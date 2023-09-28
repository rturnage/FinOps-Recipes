# Regions Table

* [Overview](#overview)
* [Schema](#schema)
* [Example Data](#example-data)
* [Source Data](#source-data)
* [Transformation](#transformation)

## Overview
![Regions](../docs/RecipesReportsRegions.jpg)

The regions table provides information about the Azure regions.

## Schema
| Field | Type | Notes |
|-------|------|-------|
| displayName | nvarchar(25) | |
| geographyGroup | nvarchar(20) NULL | |
| id | nvarchar(100) | |
| latitude | Decimal(8,6) NULL | |
| longitude | Decimal(9,6) NULL | |
| name | nvarchar(25) | |
| pairedRegion | nvarchar(25) NULL | |
| physicalLocation | nvarchar(35) NULL | |
| regionCategory | nvarchar(15) | | 
| regionalDisplayName | nvarchar(50) | |
| regionType | nvarchar(10) | |
| subscriptionId | nvarchar(50) | |

## Example Data
See full dataset [/sample_data/Regions.csv](../sample_data/Regions.csv)

|displayName | geographyGroup | id | latitude | longitude | name | pairedRegion | physicalLocation | regionCategory | regionalDisplayName | regionType | subscriptionId |
|------------|-----|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Asia |  | /subscriptions/00000000-0000-2222-0000-000000000000/locations/asia |  |  | asia |  |  | Other | Asia | Logical | 00000000-0000-2222-0000-000000000000 |
| Australia Central | Asia Pacific | /subscriptions/00000000-0000-2222-0000-000000000000/locations/australiacentral | -35.3075 | 149.1244 | australiacentral | australiacentral | Canberra | Other | (Asia Pacific) Australia Central | Physical | 00000000-0000-2222-0000-000000000000 |
| Brazil |  | /subscriptions/00000000-0000-2222-0000-000000000000/locations/brazil |  |  | brazil |  |  | Other | Brazil | Logical | 00000000-0000-2222-0000-000000000000 |
| Brazil Southeast | South America | /subscriptions/00000000-0000-2222-0000-000000000000/locations/brazilsoutheast | -22.90278 | -43.2075 | brazilsoutheast | brazilsouth | Rio | Other | (South America) Brazil Southeast | Physical | 00000000-0000-2222-0000-000000000000 |
| Central US | US | /subscriptions/00000000-0000-2222-0000-000000000000/locations/centralus | 41.5908 | -93.6208 | centralus | eastus2 | Iowa | Recommended | (US) Central US | Physical | 00000000-0000-2222-0000-000000000000 |
| Central US (Stage) | US | /subscriptions/00000000-0000-2222-0000-000000000000/locations/centralusstage |  |  | centralusstage |  |  | Other | (US) Central US (Stage) | Logical | 00000000-0000-2222-0000-000000000000 |
| Central US EUAP | US | /subscriptions/00000000-0000-2222-0000-000000000000/locations/centraluseuap | 41.5908 | -93.6208 | centraluseuap | eastus2euap |  | Other | (US) Central US EUAP | Physical | 00000000-0000-2222-0000-000000000000 |

## Source Data

| Source |  Detail | 
|-----|------|
| Azure Api | [Subscriptions List Locations](https://learn.microsoft.com/en-us/rest/api/resources/subscriptions/list-locations?tabs=HTTP) |
| Azure API Endpoint | GET https://management.azure.com/subscriptions/{subscriptionId}/locations?api-version=2020-01-01 | 
| Azure Api Version | 2020-01-01 |

## Transformation

Transform the source by mapping to new format, apply steps in notes and sort by displayName.

[JMESPath](https://jmespath.org/) notation used to map to fields.

| Field | Source | Notes |
|-------|------|-------|
| displayName | value[*].displayName | |
| geographyGroup | value[*].metadata.geographyGroup | |
| id | value[*].id | replace with dummy subscription id|
| latitude | value[*].metadata.latitude | |
| longitude | value[*].metadata.longitude | |
| name | value[*].name | |
| pairedRegion | value[*].metadata.pairedRegion[0].id | |
| physicalLocation | value[*].metadata.physicalLocation | |
| regionCategory | value[*].metadata.regionCategory | | 
| regionalDisplayName | value[*].regionalDisplayName | |
| regionType | value[*].regionType | |
| subscriptionId | value[*].id | <ul><li>split on `,` take `2` index value</li><li>replace with dummy subscription id</li></ul> |


