# Developer Docs

Follow the [Quick Start](../README.md#quick-start) to get the starting development environment.

* [Manage Docker Database](#docker-database)
* [Create Sample Data](#sample-data)

## Docker Database
Docker commands to manage the database image. 

```bash
# Build the image
docker build --pull --rm -f "database/Dockerfile.dev" -t cfm_recipes:latest "."

# Run a new recipes container. This loads default data.
docker run --env-file .env -p 1433:1433 --hostname cfm_recipes --name cfm_recipes --detach cfm_recipes:latest

# Get a shell to the container
docker container exec -it cfm_recipes /bin/bash

# Stop the container to keep the current state.
docker container stop cfm_recipes

# Start the stopped container. Does not reload data. 
docker container start cfm_recipes

# Remove a container
docker container rm cfm_recipes

# Quick Build. Kills the image after run
docker run --rm -it --env-file .env -p 1433:1433 --hostname cfm_recipes --name cfm_recipes cfm-recipes:latest

# Create Database DACPACK
docker container exec -it cfm_recipes /usr/src/app/create_db_package.sh dacpac

# Create Database BACPACK
docker container exec -it cfm_recipes /usr/src/app/create_db_package.sh bacpac

# Copy dacpac or bacpac from docker image to local
docker container cp cfm_recipes:/usr/src/app/CfmRecipes.dacpac ./database/CfmRecipes.dacpac  
docker container cp cfm_recipes:/usr/src/app/CfmRecipes.bacpac ./database/CfmRecipes.bacpac 
```
## SQL 

Helpful sql queries
```sql

-- Show table details
exec sp_help '[cfm].[AmortizedCostSummary]'

-- Execute a stored procedure
DECLARE @DateRangeStart date
DECLARE @DateRangeEnd date
SET @DateRangeStart = '2022-01-01'
SET @DateRangeEnd = '2022-10-31'

exec [cfm].[UpdateAmortizedSummaryTable] @DateRangeStart,  @DateRangeEnd

-- Aggregate String values in group by
,STRING_AGG(CONVERT(NVARCHAR(max), [Tags]), ',') [TagsList]

```
## Linting

Before checking in project, run the following:

```bash
codespell --skip="*.pbit,*.pbix,**/.venv"

# in python project
cd ./transform/python_transform
isort regions_from_azure_list_locations.py
black regions_from_azure_list_locations.py
flake8 regions_from_azure_list_locations.py
pylint regions_from_azure_list_locations.py
pydocstyle regions_from_azure_list_locations.py

```

## Sample Data

The sample data:

- provides enough data to demo a recipe report.
- aligns to the common data schema

Sample data can be created several ways:

- Generate via procedure
- Modifying real data

### Regions - Sample Data

Download the data using the [list-locations](https://docs.microsoft.com/en-us/rest/api/resources/subscriptions/list-locations#code-try-0) api with either the `az cli` or `wget`.

```bash
# Replace with your subscription-id and bearer token
subscription_id=<subscription-id>
bearer_token=<bearer token>
regions_filename="./sample_data/Regions.json"

# az cli example
az account list-locations > $regions_filename

# wget example
header='--header=Authorization: Bearer $bearer_token'
wget "$header" https://management.azure.com/subscriptions/$subscription_id/locations?api-version=2020-01-01 -O $regions_filename
```

Transform the data using one of the methods:

* PowerBi Template
* python script

**PowerBI**

- Open the `./sample_data/RegionsFromAzureAccountListLocations.pbit` and select the path to the downloaded `./sample_data/Regions.json` file.
- On the `Raw Data` tab, select the dataset click `Export Data` from the ellipse.
- Save the file as `./sample_data/Regions.csv`

Remove bad records by:

- Remove the header row
- Replacing `subscripionid` with `dummy_subscription_id`
- Remove the `,` (comma) and `"` (quote)s from `"Tokyo, Saitama"` to `Tokyo Saitama`

**Python**

Run the python script to transform the downloaded `./sample_data/Regions.json` file.

```bash
dest_filename="./sample_data/Wowza.csv"
python ./transform/python_transform/regions_from_azure_list_locations.py --src_filename $regions_filename --dest_filename
```

### Advisor - Sample Data

- Initiate the Recommendation Generation process
- Download from Azure
- Transform the data
- Remove Bad Records

Initiate the Recommendation py calling [generate-recommendations](https://docs.microsoft.com/en-us/rest/api/advisor/recommendations/generate)
Download the data using the [list-recommendations](https://docs.microsoft.com/en-us/rest/api/advisor/recommendations/list) api with either the `az cli` or `wget`.

```bash
# Replace with your subscription-id and bearer token
subscription_id=<subscription-id>
bearer_token=<bearer token>
recommendation_filename=Advisor.json

# az cli example
az advisor recommendation list > $recommendation_filename

# wget example
header='--header=Authorization: Bearer $bearer_token'

wpost "$header" POST https://management.azure.com/subscriptions/$subscription_id/providers/Microsoft.Advisor/generateRecommendations?api-version=2017-04-19

wget "$header" https://management.azure.com/subscriptions/$subscription_id/providers/Microsoft.Advisor/recommendations?api-version=2020-01-01 -O $recommendation_filename
```

Transform the data using the PowerBi Template.

- Open the `sampledata/AdvisorFromAzureAdvisorRecommendationList.pbit` and enter the path to the downloaded `sampledata/Advisor.json` file for the `json_data_file_name` parameter.
- On the `Raw Data` tab, select the dataset click `Export Data` from the ellipse.
- Save the file as `sampledata/Advisor.csv`

Remove bad records by:

- Remove the header row
- Replacing `subscripionid` with dummy_subscription_id
- Replacing `resource Group Name` with dummy resource group name
- Replacing `vm name` with dummy vm name
- Remove the `,` (comma) and `"` (quote)s from `"Virtual machines should encrypt temp disks, caches, and data flows between Compute and Storage resources"` to `Virtual machines should encrypt temp disks caches and data flows between Compute and Storage resources`

### ISF Data - Sample Data

- Download from Azure
- Remove Bad Records

Download the [ISFRatio file](https://isfratio.blob.core.windows.net/isfratio/ISFRatio.csv) with  `wget`.

```bash
wget https://isfratio.blob.core.windows.net/isfratio/ISFRatio.csv 
```

Remove bad records by:

- Remove the header row
- Replacing `subscripionid` with dummy_subscription_id
- Replacing `resource Group Name` with dummy resource group name
- Replacing `vm name` with dummy vm name
- Remove the `,` (comma) and `"` (quote)s from `"Virtual machines should encrypt temp disks, caches, and data flows between Compute and Storage resources"` to `Virtual machines should encrypt temp disks caches and data flows between Compute and Storage resources`

### Reservation Transaction - Sample Data

- Download from Azure
- Transform the data
- Remove Bad Records

Download the data using the [/api/consumption/reservation-transactions/list](https://docs.microsoft.com/en-us/rest/api/consumption/reservation-transactions/list) api with either the `az cli` or `wget`.

```bash
# Replace with your subscription-id and bearer token
billing_account_id=<billingAccountId>
subscription_id=<subscription-id>
period_start_date=<Filter start date 2021-06-01>
period_end_date=<Filter end date 2021-11-30>
bearer_token=<bearer token>
data_file=ReservationTransactions.json
consumption_api_version=2021-10-01

# az cli example

az consumption reservation detail list --end-date --reservation-order-id --start-date > $data_file
# OR

billing_account_id=$(az billing account list --query "[].name" -o tsv)
invoice_name=$(az billing invoice list --account-name $billing_account_id --period-end-date $period_end_date --period-start-date $period_end_date)
az billing transaction list --account-name $billing_account_id --invoice-name

# wget example
header='--header=Authorization: Bearer $bearer_token'

# Get Billing Account Id
header='--header=Authorization: Bearer $bearer_token'
wget "$header" https://management.azure.com/providers/Microsoft.Billing/billingAccounts?api-version=$consumption_api_version -O billing_accounts.json

# Get Reservation transactions
wget "$header" https://management.azure.com/providers/Microsoft.Billing/billingAccounts/$billingAccountId/providers/Microsoft.Consumption/reservationTransactions?$filter=properties/EventDate+ge$event_start_date+AND+properties/EventDate+le+$event_end_dateapi-version=$consumption_api_version -O $data_file
```

Transform the data using the PowerBi Template.

- Open the `sampledata/ReservationTransactionsFromAzureApiJson.pbit` and enter the path to the downloaded `sampledata/ReservationTransactions.json` file for the `json_data_file_name` parameter.
- On the `Raw Data` tab, select the dataset click `Export Data` from the ellipse.
- Save the file as `sampledata/ReservationTransactions.csv`

Remove bad records by:

- Remove the header row
- Replacing `subscripionid` with dummy_subscription_id

### Actual Cost - Sample Data

- Download Data
    - Option 1 (Query Usage data)
    - Option 2 (Create & Invoke Export Job)
- Transform the data
- Remove Bad Records

**Download Option 1 - Query Usage Data**

Download the data using the [/api/cost-management/query/usage](https://docs.microsoft.com/en-us/rest/api/cost-management/query/usage) api with either the `az cli` or `wget`.
And the cli [usage](https://docs.microsoft.com/en-us/cli/azure/costmanagement?view=azure-cli-latest#az_costmanagement_query)

**Download Option 2 - Export Job**

Create and invoke an export using the `az cli` [export](https://docs.microsoft.com/en-us/cli/azure/costmanagement/export?view=azure-cli-latest) command or call the [/api/cost-management/exports/create-or-update](https://docs.microsoft.com/en-us/rest/api/cost-management/exports/create-or-update) api with `wget`.

Set scope to 
- `/providers/Microsoft.Billing/billingAccounts/{billingAccountId}`
- `/subscriptions/{subscriptionId}/`


```bash
# Replace with your subscription-id and bearer token


# billing_account_id=$(az billing account list --query "[].name" -o tsv)
# invoice_name=$(az billing invoice list --account-name $billing_account_id --period-end-date $period_end_date --period-start-date $period_end_date)
# az billing transaction list --account-name $billing_account_id --invoice-name

billing_number=<Billing Number AKA Enrollment Number>
subscription_id=<subscription-id>
bearer_token=<bearer token>

scope="providers/Microsoft.Billing/billingAccounts/$billing_number"

# azcli
cost_type="ActualCosts"
cost_filename="ActualCostBilling.json"
az costmanagement query --type $cost_type --timeframe "MonthToDate" --scope $scope > $cost_filename

cost_type="AmortizedCosts"
cost_filename="AmortizedCostBilling.json"
az costmanagement query --type $cost_type --timeframe "MonthToDate" --scope $scope > $cost_filename

# Query usage
POST https://management.azure.com/$scope/providers/Microsoft.CostManagement/query?api-version=2021-10-01
{
	type: "ActualCosts",
    timeframe: "MonthToDate",
	dataset: {
            "granularity": "Daily"
        }
	
}

POST https://management.azure.com/$scope/providers/Microsoft.CostManagement/query?api-version=2021-10-01
{
	type: "AmortizedCosts",
    timeframe: "MonthToDate",
	dataset: {
            "granularity": "Daily"
        }
	
}

```

Powershell example to create and invoke an export for both Actual and Amortized costs.
```powershell
$StorageAccountSubscriptionId=<Destination Subscription ID>
$ResourceGroup=<Billing Storage Resource Group>
$StorageAccountName=<Billing Costs Storage Account>

$DatasetGranularity="Daily"
$DefinitionTimeframe="MonthToDate" 
$DestinationResourceId="/subscriptions/$StorageAccountSubscriptionId/resourceGroups/$ResourceGroup/providers/Microsoft.Storage/storageAccounts/$StorageAccountName"
$DestinationContainer="Costs"
$ScheduleStatus="Inactive" 
$Format="Csv" 

billing_account_id=$(az billing account list --query "[].name" -o tsv)
$Scope=providers/Microsoft.Billing/billingAccounts/$billing_account_id

$ExportName="OneTime-Actual-CostManagement-Export" 
$DefinitionType="ActualCost"
$DestinationRootFolderPath="/actual_costs/scheduled_exports"
New-AzCostManagementExport 
    -Name $ExportName -Scope $Scope -DatasetGranularity $DatasetGranularity -DefinitionTimeframe $DefinitionTimeframe -DefinitionType $DefinitionType -ScheduleStatus $ScheduleStatus -Format $Format -DestinationResourceId $DestinationResourceId -DestinationContainer $DestinationContainer -DestinationRootFolderPath $DestinationRootFolderPath
Invoke-AzCostManagementExecuteExport -ExportName $ActualCostExportName -Scope $Scope

$ExportName="OneTime-Amortized-CostManagement-Export" 
$DefinitionType="AmortizedCost"
$DestinationRootFolderPathAmortized="/amortized_costs/scheduled_exports"
New-AzCostManagementExport
    -Name AmortizedCostExportName -Scope $Scope -DatasetGranularity $DatasetGranularity -DefinitionTimeframe $DefinitionTimeframe -DefinitionType $DefinitionType -ScheduleStatus $ScheduleStatus -Format $Format -DestinationResourceId $DestinationResourceId -DestinationContainer $DestinationContainer -DestinationRootFolderPath $DestinationRootFolderPath
Invoke-AzCostManagementExecuteExport -ExportName $ExportName -Scope $Scope

```

### Creating a Data Transform PBI template
Template Overview: Report used to transform raw data into csv file.

| Parameter Name | Description |
|----------------|-------------|
| json_data_file_name | filename of the downloaded json data from the api |


### Creating the Sample PBI template

Template Overview: Sample Azure cost optimization reports built on top of a common dataset.

| Parameter Name | Description | Default |
|----------------|-------------|---------|
| server         | server name (Host or ip. The port may be optionally specified with the server, separated by a colon or a comma.) | localhost |
| database       | SQL Server database on server <server> | CfmRecipes |


## Design Notes

### Dummy Data

| Field | Value |
|-------|-------|
|subscriptionId | 00000000-0000-2222-0000-000000000000 |
|subscriptionName | Infrastructure Subscription |
|billingaccount | 123456 |

### Sql DB

Default Sql Collation `SQL_Latin1_General_CP1_CI_AS`
```sql
SELECT SERVERPROPERTY('Collation')
SELECT DATABASEPROPERTYEX('CfmRecipies', 'Collation')
```

Create Sql bcp format file
```bash
/opt/mssql-tools/bin/bcp CfmRecipes.cfm.ISFData format nul -c -f ISFRatio.fmt -t, -S localhost -U sa -P $SA_PASSWORD
```