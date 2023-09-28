# Actual Cost Table

* [Overview](#overview)
* [Schema](#schema)
* [Example Data](#example-data)
* [Source Data](#source-data)
* [Transformation](#transformation)

## Overview
![Actual Cost](https://dummyimage.com/300x300/fff/aaa)

The Actual Cost table provides detailed data for Actual Costs.

## Schema
| Field | Type | Notes |
|-------|------|-------|
| InvoiceSectionName | nvarchar(300) NULL | |
| AccountName | nvarchar(300) NULL | |
| AccountOwnerId | nvarchar(300) NULL | |
| SubscriptionId | nvarchar(300) NULL | |
| SubscriptionName | nvarchar(300) NULL | |
| ResourceGroup | nvarchar(300) NULL | |
| ResourceLocation | nvarchar(300) NULL | |
| Date | date NULL | |
| ProductName | nvarchar(300) NULL | |
| MeterCategory | nvarchar(300) NULL | |
| MeterSubCategory | nvarchar(300) NULL | |
| MeterId | nvarchar(300) NULL | |
| MeterName | nvarchar(300) NULL | |
| MeterRegion | nvarchar(300) NULL | |
| UnitOfMeasure | nvarchar(300) NULL | |
| Quantity | decimal (28,20) NULL | |
| EffectivePrice | decimal (28,20) NULL | |
| CostInBillingCurrency | decimal (28,20) NULL | |
| CostCenter | nvarchar(300) NULL | |
| ConsumedService | nvarchar(300) NULL | |
| ResourceId | nvarchar(2000) NULL | |
| Tags | nvarchar(4000) NULL | |
| OfferId | nvarchar(300) NULL | |
| AdditionalInfo | nvarchar(4000) NULL | |
| ServiceInfo1 | nvarchar(300) NULL | |
| ServiceInfo2 | nvarchar(300) NULL | |
| ResourceName | nvarchar(300) NULL | |
| ReservationId | nvarchar(300) NULL | |
| ReservationName | nvarchar(300) NULL | |
| UnitPrice | decimal (28,20) NULL | |
| ProductOrderId | nvarchar(300) NULL | |
| ProductOrderName | nvarchar(300) NULL | |
| Term | nvarchar(300) NULL | |
| PublisherType | nvarchar(300) NULL | |
| PublisherName | nvarchar(300) NULL | |
| ChargeType | nvarchar(300) NULL | |
| Frequency | nvarchar(300) NULL | |
| PricingModel | nvarchar(300) NULL | |
| AvailabilityZone | nvarchar(300) NULL | |
| BillingAccountId | nvarchar(300) NULL | |
| BillingAccountName | nvarchar(300) NULL | |
| BillingCurrencyCode | nvarchar(20) NULL | |
| BillingPeriodStartDate | date NULL | |
| BillingPeriodEndDate | date NULL | |
| BillingProfileId | nvarchar(100) NULL | |
| BillingProfileName | nvarchar(300) NULL | |
| InvoiceSectionId | nvarchar(300) NULL | |
| IsAzureCreditEligible | nvarchar(10) NULL | |
| PartNumber | nvarchar(50) NULL | |
| PayGPrice | nvarchar(100) NULL | |
| PlanName | nvarchar(300) NULL | |
| ServiceFamily | nvarchar(300) NULL | |
| CostAllocationRuleName | nvarchar(300) NULL

## Example Data
See full dataset [/sample_data/ActualCostsSummary.csv](../sample_data/ActualCosts.csv)

| AccountName | AccountOwnerId | AdditionalInfo | AvailabilityZone | BillingAccountId | BillingAccountName | BillingCurrencyCode | BillingPeriodEndDate | BillingPeriodStartDate | BillingProfileId | BillingProfileName | ChargeType | ConsumedService | CostAllocationRuleName | CostCenter | CostInBillingCurrency | Date | EffectivePrice | Frequency | InvoiceSectionId | InvoiceSectionName | IsAzureCreditEligible | MeterCategory | MeterId | MeterName | MeterRegion | MeterSubCategory | OfferId | PartNumber | PayGPrice | PlanName | PricingModel | ProductName | ProductOrderId | ProductOrderName | PublisherName | PublisherType | Quantity | ReservationId | ReservationName | ResourceGroup | ResourceId | ResourceLocation | ResourceName | ServiceFamily | ServiceInfo1 | ServiceInfo2 | SubscriptionId | SubscriptionName | Tags | Term | UnitOfMeasure | UnitPrice |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|68b524ab-0f59-43d2-b8a4-6da7575ada4e|
|e77b15a3-c4cf-4235-ae68-ff98795705ca|
|13bb8ce7-f82e-4463-84f9-ab3ae7e3cdb2|
|286bf7e1-9b61-4739-9f6b-4583e64da0e9|
|ec8c7b49-9790-4261-b46f-293dabb53fd9|

## Source Data

| Source |  Version | Detail | 
|--------|----------|--------|
| Azure Export | 2022-10-01 | [Exports - Create Or Update](https://learn.microsoft.com/en-us/rest/api/cost-management/exports/create-or-update?tabs=HTTP)
| Azure API | 2022-10-01 | [Generate Cost Detail Report - Create Operation](https://learn.microsoft.com/en-us/rest/api/cost-management/generate-cost-details-report/create-operation?tabs=HTTP) |
| Azure API | 2022-10-01 | [Generate Cost Detail Report - Get Operation Results](https://learn.microsoft.com/en-us/rest/api/cost-management/generate-cost-details-report/get-operation-results?tabs=HTTP) |

Fetch the data by either:
* Exporting the Data (Recommended)
    * Create a scheduled export [Exports - Create Or Update](https://learn.microsoft.com/en-us/rest/api/cost-management/exports/create-or-update?tabs=HTTP)
* Generateing Cost Detail Report
    * Initiate the Cost Detail Report by calling [Create Operation Results](https://learn.microsoft.com/en-us/rest/api/cost-management/generate-cost-details-report/create-operation?tabs=HTTP)
    * Download the data using the [Get Operation Results](https://learn.microsoft.com/en-us/rest/api/cost-management/generate-cost-details-report/get-operation-results?tabs=HTTP)

## Transformation

Transform the source by applying steps in notes.

> No transformation. This is a 1:1 mapping between the source and destination.

