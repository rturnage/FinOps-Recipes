# Advisor Table

* [Overview](#overview)
* [Schema](#schema)
* [Example Data](#example-data)
* [Source Data](#source-data)
* [Transformation](#transformation)

## Overview
![Advisor View](../docs/RecipesReportsAdvisor.jpg)

The Advisor table provides detailed data for Azure Advisor recomendations.

## Schema
| Field | Type | Notes |
|-------|------|-------|
| assessmentKey | nvarchar(36) NULL | |
| Category | nvarchar(20) | |
| id | nvarchar(300) | |
| Impact | nvarchar(6) | |
| Impacted Resource Name | nvarchar(50) | |
| Impacted Resource Type | nvarchar(50) | |
| Last Updated | Date |
| name | nvarchar(50) | |
| recommendationTypeId | nvarchar(50) | |
| resourceId | nvarchar(2000) | |
| score | Decimal(3,2) NULL | |
| Short Description - Problem | nvarchar(200) | |
| Short Description - Solution | nvarchar(200) | |
| source | nvarchar(300) NULL | |
| subscriptionId | nvarchar(300) | |
| type | nvarchar(50) | |

## Example Data
See full dataset [/sample_data/Advisor.csv](../sample_data/Advisor.csv)

| assessmentKey | Category | id | Impact | Impacted Resource Name | Impacted Resource Type | Last Updated | name | recommendationTypeId | resourceId | score | Short Description - Problem | Short Description - Solution | source | subscriptionId | type |
|---------------|----------|----|--------|------------------------|------------------------|--------------|------|----------------------|------------|-------|-----------------------------|------------------------------|--------|----------------|------|
| 01195afff-c881-495e-9bc5-1486211ae03f | Security | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-dev/providers/microsoft.compute/virtualmachines/vm-app/providers/Microsoft.Advisor/recommendations/93f3162f-eddf-e642-cbab-949e06a95743 | Low | vm-app | Microsoft.Compute/virtualMachines | 2021-12-08 00:27:44 | 93f3162f-eddf-e642-cbab-949e06a95743 | 01195afff-c881-495e-9bc5-1486211ae03f | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-dev/providers/microsoft.compute/virtualmachines/vm-app | 0 | Machines should have vulnerability findings resolved | Machines should have vulnerability findings resolved | /subscriptions/00000000-0000-2222-0000-000000000000/resourceGroups/rg-dev/providers/Microsoft.Compute/virtualMachines/vm-app/providers/Microsoft.Security/assessments/01195afff-c881-495e-9bc5-1486211ae03f | 00000000-0000-2222-0000-000000000000 | Microsoft.Advisor/recommendations |
| 01195afff-c881-495e-9bc5-1486211ae03f | Security | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-production/providers/microsoft.compute/virtualmachines/vm-app/providers/Microsoft.Advisor/recommendations/3b17ca49-f2ba-c3be-f434-c0bf2e72dfcc | Low | rg-production | Microsoft.Compute/virtualMachines | 2021-12-08 00:27:44 | 3b17ca49-f2ba-c3be-f434-c0bf2e72dfcc | 01195afff-c881-495e-9bc5-1486211ae03f | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-production/providers/microsoft.compute/virtualmachines/rg-production | 0 | Machines should have vulnerability findings resolved | Machines should have vulnerability findings resolved | /subscriptions/00000000-0000-2222-0000-000000000000/resourceGroups/rg-production/providers/Microsoft.Compute/virtualMachines/rg-production/providers/Microsoft.Security/assessments/01195afff-c881-495e-9bc5-1486211ae03f | 00000000-0000-2222-0000-000000000000 | Microsoft.Advisor/recommendations |
| 13e7d036-6903-821c-6018-962938929bf0 | Security | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-test/providers/microsoft.containerregistry/registries/vm-app2/providers/Microsoft.Advisor/recommendations/5bf6839d-a139-bc3f-2e9e-7fecdb85b437 | Medium | vm-app2 | Microsoft.ContainerRegistry/registries | 2021-12-08 00:27:55 | 5bf6839d-a139-bc3f-2e9e-7fecdb85b437 | 13e7d036-6903-821c-6018-962938929bf0 | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-test/providers/microsoft.containerregistry/registries/vm-app2 | 0 | Container registries should use private link | Container registries should use private link | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-test/providers/microsoft.containerregistry/registries/vm-app2/providers/Microsoft.Security/assessments/13e7d036-6903-821c-6018-962938929bf0 | 00000000-0000-2222-0000-000000000000 | Microsoft.Advisor/recommendations |
| 13e7d036-6903-821c-6018-962938929bf0 | Security | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-app1/providers/microsoft.containerregistry/registries/reg-master/providers/Microsoft.Advisor/recommendations/0b7989f1-89a9-65eb-8546-5de841329b5f | Medium | reg-master | Microsoft.ContainerRegistry/registries | 2021-12-08 00:27:44 | 0b7989f1-89a9-65eb-8546-5de841329b5f | 13e7d036-6903-821c-6018-962938929bf0 | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-app1/providers/microsoft.containerregistry/registries/reg-master | 0 | Container registries should use private link | Container registries should use private link | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-app1/providers/microsoft.containerregistry/registries/reg-master/providers/Microsoft.Security/assessments/13e7d036-6903-821c-6018-962938929bf0 | 00000000-0000-2222-0000-000000000000 | Microsoft.Advisor/recommendations |
| 13e7d036-6903-821c-6018-962938929bf0 | Security | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-db/providers/microsoft.containerregistry/registries/reg-dev/providers/Microsoft.Advisor/recommendations/32883171-269c-a47f-58d9-da03df7d3fa6 | Medium | reg-dev | Microsoft.ContainerRegistry/registries | 2021-12-08 00:27:55 | 32883171-269c-a47f-58d9-da03df7d3fa6 | 13e7d036-6903-821c-6018-962938929bf0 | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-db/providers/microsoft.containerregistry/registries/reg-dev | 0 | Container registries should use private link | Container registries should use private link | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-db/providers/microsoft.containerregistry/registries/reg-dev/providers/Microsoft.Security/assessments/13e7d036-6903-821c-6018-962938929bf0 | 00000000-0000-2222-0000-000000000000 | Microsoft.Advisor/recommendations |
|                                      | HighAvailability | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-test/providers/microsoft.compute/virtualmachines/vm-app/providers/Microsoft.Advisor/recommendations/e76be915-eef6-9249-7cd5-2b02df9564a4 | Medium | rg-test-app | MICROSOFT.CLASSICCOMPUTE/VIRTUALMACHINES | e76be915-eef6-9249-7cd5-2b02df9564a4 | 651c7925-17a3-42e5-85cd-73bd095cf27f | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-test/providers/microsoft.compute/virtualmachines/rg-test-app |  | Enable Backups on your Virtual Machines | Enable Backups on your Virtual Machines |  | 00000000-0000-2222-0000-000000000000 | Microsoft.Advisor/recommendations |
|                                      | HighAvailability | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-dev/providers/microsoft.compute/virtualmachines/vm-db/providers/Microsoft.Advisor/recommendations/354a06ea-7a93-3079-5c4d-9871044915c1 | Medium | vm-db | MICROSOFT.CLASSICCOMPUTE/VIRTUALMACHINES | 354a06ea-7a93-3079-5c4d-9871044915c1 | 651c7925-17a3-42e5-85cd-73bd095cf27f | /subscriptions/00000000-0000-2222-0000-000000000000/resourcegroups/rg-dev/providers/microsoft.compute/virtualmachines/vm-db |  | Enable Backups on your Virtual Machines | Enable Backups on your Virtual Machines |  | 00000000-0000-2222-0000-000000000000 | Microsoft.Advisor/recommendations |

## Source Data

| Source |  Version | Detail | 
|--------|----------|--------|
| Azure API | 2017-04-19| Request [Recomendations - Generate](https://learn.microsoft.com/en-us/rest/api/advisor/recommendations/generate?tabs=HTTP) |
| Azure API | 2020-01-01| Retreive [Recomendations - List](https://learn.microsoft.com/en-us/rest/api/advisor/recommendations/list?tabs=HTTP)  |

## Transformation

Transform the source by applying steps in notes.

[JMESPath](https://jmespath.org/) notation used to map to fields.

| Field | Source | Notes |
|-------|------|-------|
| assessmentKey | value[*].extendedProperties.assessmentKey | |
| Category | value[*].properties.category | |
| id | value[*].id | |
| Impact | value[*].properties.impact | |
| Impacted Resource Name | value[*].properties.impactedValue | |
| Impacted Resource Type | value[*].properties.impactedField | |
| Last Updated | value[*].properties.lastUpdated | |
| name | value[*].name | |
| recommendationTypeId | value[*].properties.recommendationTypeId | |
| resourceId | value[*].resourceMetadata.resourceId | |
| score | value[*].extendedProperties.score | |
| Short Description - Problem | value[*].shortDescription.problem | |
| Short Description - Solution | value[*].shortDescription.solution | |
| source | value[*].resourceMetadata.source | |
| subscriptionId | value[*].id  | split by `/` take `3` index value |
| type | value[*].type | |
