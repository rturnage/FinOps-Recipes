# Common Data Set

The purpose of the Common Data Set is to standardize on the various data sets used to create meaningful reports for Azure Cost Optimzation and to provide a sample database for local development.

|Table | Source | Fields | Sorted | Typed |
|------|--------|--------|-------|--------|
| [Regions](regions.md) | Blob - download/regions/azure regionsv2.json | Yes | Yes | No |
| [Advisor](advisor.md) | Blob - download/advisor/merged/advisor.json| Yes | Yes | No |
| [ISFData](isf_data.md) | Blob - download/isfratio/isfratio.csv | Yes | Yes | Yes |
| [Reservation Transactions](reservation_transactions.md) | Blob - download/restransactions/restransactions.json | Yes | Yes | No |
| [ActualCost](actual_cost.md) | DB | Yes | No (OK) | Yes |
| [ActualCostSummary](actual_cost_summary.md) | DB | Yes | No (OK) | Yes |
| [AmortizedCost](amortized_cost.md) | DB | Yes | No (OK) | Yes |
| [AmortizedCostSummary](amortized_cost_summary.md) | DB | Yes | No (OK) | Yes |
| Reservation Details | DB |Yes | Yes | Yes |
| Subscriptions | Billing data | NA | NA | NA |
| Reservation Recommendations | blob - download/resrecommendations/merged/reservation_merged.json| Yes | Yes | No |
| [Meters](meters.md) | Reservation Recommendations | NA | NA | NA |
| PriceList | Blob - download/pricesheet/pricesheet.json | Yes | Yes | No |
| Marketplace | Blob - download/marketplace/marketplace.json |  Yes | Yes | No |
| Date | Calculated | NA | NA | NA |

## Relationships

| Table Left | Table Right | Cardinality | Cross Filter |
| -----------|-------------|-------------|--------------|
| ActualCosts.Date | Date.DateAsTextAlt | Many to one | Both |
| ActualCost.MeterId | Meters.meterId | Many to one | Single |
| ActualCost.ResourceLocation | Regions.name | Many to one | Single |
| ActualCosts.SubscriptonId | Subscriptions.SubscriptionId | Many to one | Single |
| AmortizedCost.Date | Date.DateAsTextAlt | Many to one | Single |
| AmortizedCost.ResourceLocation | Regions.name | Many to one | Single |
| AmortizedCost.SubscriptionId | Subscriptions.SubscriptionId | Many to one | Single |
| Reservation Recomendatins.subscriptionId | Subscriptions.SubscriptionId | Many to one | Single |

## Reservation Recommendations Table

| Field | Type | Notes |
|-------|------|-------|
| AnnualSavings | Number | Calculated AnnualSavings = 'Reservation Recommendations'[netSavings]/SUBSTITUTE(SUBSTITUTE('Reservation Recommendations'[Look Back Period],"Last",""),"Days","")*365 |

    TBD 