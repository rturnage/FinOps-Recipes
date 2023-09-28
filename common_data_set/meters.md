# Meters Table

* [Overview](#overview)
* [Schema](#schema)
* [Example Data](#example-data)
* [Source Data](#source-data)
* [Transformation](#transformation)

## Overview
![Meters](https://dummyimage.com/300x300/fff/aaa)

The meters table provides information about the Azure meters.

## Schema
| Field | Type | Notes |
|-------|------|-------|
| meterId | nvarchar(36) | |

## Example Data
See full dataset [/sample_data/Meters.csv](../sample_data/Meters.csv)

|displayName |
|-----|
|68b524ab-0f59-43d2-b8a4-6da7575ada4e|
|e77b15a3-c4cf-4235-ae68-ff98795705ca|
|13bb8ce7-f82e-4463-84f9-ab3ae7e3cdb2|
|286bf7e1-9b61-4739-9f6b-4583e64da0e9|
|ec8c7b49-9790-4261-b46f-293dabb53fd9|
## Source Data

| Source |  Detail | 
|-----|------|
| Reservation Recommendations Common Dataset Table| [Reservation Recommendations](reservations_recommendations.md) 

## Transformation

Transform the source by applying steps in notes.

1) Remove all columns, except for meterId
2) Remove duplicates

