# Reservation Transactions Table

* [Overview](#overview)
* [Schema](#schema)
* [Example Data](#example-data)
* [Source Data](#source-data)
* [Transformation](#transformation)

## Overview
![Reservation Transactions](https://dummyimage.com/300x300/fff/aaa)

The Reservation Transactions table provides detailed data for Reservation transactions.

## Schema
| Field | Type | Notes |
|-------|------|-------|
| accountName | nvarchar(100) | |
| accountOwnerEmail | nvarchar(100) | |
| amount | Decimal(12,3) | |
| armSkuName | nvarchar(50) | |
| billingFrequency | nvarchar(50) | |
| costCenter | nvarchar(100) | |
| currency | nvarchar(20) | |
| currentEnrollment | nvarchar(50) | |
| departmentName | nvarchar(50) | |
| description | nvarchar(50) | |
| eventDate | Date | |
| eventType | nvarchar(10) | |
| id | nvarchar(200) | |
| name | nvarchar(50) | |
| purchasingEnrollment | nvarchar(50) | |
| purchasingSubscriptionGuid | nvarchar(50) | |
| purchasingSubscriptionName | nvarchar(50) | |
| quantity | int | |
| region | nvarchar(25) | |
| reservationOrderId | nvarchar(50) | |
| reservationOrderName | nvarchar(50) | |
| tags | nvarchar(200) | |
| term | nvarchar(5) | |
| type | nvarchar(50) | |

## Example Data
See full dataset [/sample_data/ReservationTransactions.csv](../sample_data/ReservationTransactions.csv)

| accountName | accountOwnerEmail | amount | armSkuName | billingFrequency | costCenter | currency | currentEnrollment | departmentName | description | eventDate | eventType | id | name | purchasingEnrollment | purchasingSubscriptionGuid | purchasingSubscriptionName | quantity | region | reservationOrderId | reservationOrderName | tags | term | type |
|-------------|-------------------|--------|------------|------------------|------------|----------|-------------------|----------------|-------------|-----------|-----------|----|------|----------------------|----------------------------|----------------------------|----------|--------|--------------------|----------------------|------|------|------|
| Aco Infrastructure | admin@example.com | 21 | Standard_DS1_v2 | recurring | "" | USD | 123456 | Unassigned | Standard_DS1_v2 westus 1 Year | 2019-09-09 12:19:04 | Purchase | /billingAccounts/123456/providers/Microsoft.Consumption/reservationtransactions/201909091919 | 201909091919 | 123456 | 00000000-0000-2222-0000-000000000000 | Infrastructure Subscription | 1 | westus | 00000000-0000-0000-0000-000000000000 | 2019-Q3-Purchase | devmaster | P1Y | Microsoft.Consumption/reservationTransactions |
| Aco Infrastructure | admin@example.com | -21 | Standard_DS1_v2 | recurring | "" | USD | 123456 | Unassigned | Standard_DS1_v2 westus 1 Year | 2019-09-09 12:19:04 | Refund | /billingAccounts/123456/providers/Microsoft.Consumption/reservationtransactions/201909091919 | 201909091919 | 123456 | 00000000-0000-2222-0000-000000000000 | Infrastructure Subscription | 1 | westus | 00000000-0000-0000-0000-000000000000 | 2019-Q3-Purchase | devmaster | P1Y | Microsoft.Consumption/reservationTransactions |
| Aco Infrastructure | admin@example.com | 500 | Standard_D1 | recurring | "" | USD | 123456 | Unassigned | Standard_D1 westus 1 Year | 2021-12-17 12:19:04 | Purchase | /billingAccounts/123456/providers/Microsoft.Consumption/reservationtransactions/202112171919 | 202112171919 | 123456 | 00000000-0000-2222-0000-000000000000 | Infrastructure Subscription | 5 | westus | 00000000-0000-0000-0000-000000000001 | 2021-Q4-Purchase | "" | P1Y | Microsoft.Consumption/reservationTransactions |
| Aco Infrastructure | admin@example.com | 600 | Standard_B1s | recurring | "" | USD | 123456 | Unassigned | Standard_B1s westus 1 Year | 2021-12-17 12:19:04 | Purchase | /billingAccounts/123456/providers/Microsoft.Consumption/reservationtransactions/202112171919 | 202112171919 | 123456 | 00000000-0000-2222-0000-000000000000 | Infrastructure Subscription | 15 | westus | 00000000-0000-0000-0000-000000000001 | 2021-Q4-Purchase | "" | P1Y | Microsoft.Consumption/reservationTransactions |

## Source Data

| Source |  Version | Detail | 
|--------|----------|--------|
| Azure API | 2021-10-01| [Reservation Transactions - List](https://learn.microsoft.com/en-us/rest/api/consumption/reservation-transactions/list?tabs=HTTP) |
|           |           |  `filter=properties/EventDate+ge+{start_date}+AND+properties/EventDate+le+{end_date}` |

## Transformation

Transform the source by applying steps in notes.

[JMESPath](https://jmespath.org/) notation used to map to fields.

| Field | Source | Notes |
|-------|------|-------|
| accountName | value[*].properties.accountName |
| accountOwnerEmail | value[*].properties.accountOwnerEmail |
| amount | value[*].properties.amount |
| armSkuName | value[*].properties.armSkuName |
| billingFrequency | value[*].properties.billingFrequency |
| costCenter | value[*].properties.costCenter |
| currency | value[*].properties.currency |
| currentEnrollment | value[*].properties.currentEnrollment |
| departmentName | value[*].properties.departmentName |
| description | value[*].properties.description |
| eventDate | value[*].properties.eventDate |
| eventType | value[*].properties.eventType |
| id | value[*].id |
| name | value[*].name |
| purchasingEnrollment | value[*].properties.purchasingEnrollment |
| purchasingSubscriptionGuid | value[*].properties.purchasingSubscriptionGuid |
| purchasingSubscriptionName | value[*].properties.purchasingSubscriptionName |
| quantity | value[*].properties.quantity |
| region | value[*].properties.region |
| reservationOrderId | value[*].properties.reservationOrderId |
| reservationOrderName | value[*].properties.reservationOrderName |
| tags | value[*].tags |
| term | value[*].properties.billingFrequency |
| type | value[*].type |
