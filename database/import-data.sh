#!/usr/bin/env bash

#run the setup script to create the DB and the schema in the DB
#do this in a loop because the timing for when the SQL instance is ready is indeterminate
DATA_IMPORTED_FILE=/usr/src/app/imported

for i in {1..50};
do
    /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -d master -v PBI_USER_PASSWORD="$PBI_USER_PASSWORD" -i setup.sql
    if [ $? -eq 0 ]
    then
        echo "setup.sql completed"
        break
    else
        echo "not ready yet..."
        sleep 1
    fi
done

#import the data from the csv file
/opt/mssql-tools/bin/bcp CfmRecipes.cfm.Regions in "/usr/src/app/Regions.csv" -e /usr/src/app/bcp_err.log -c -t',' -S localhost -U sa -P $SA_PASSWORD
/opt/mssql-tools/bin/bcp CfmRecipes.cfm.Advisor in "/usr/src/app/Advisor.csv" -e /usr/src/app/bcp_err.log -c -t',' -S localhost -U sa -P $SA_PASSWORD
/opt/mssql-tools/bin/bcp CfmRecipes.cfm.ISFData in "/usr/src/app/ISFRatio.csv" -f /usr/src/app/ISFRatio.fmt -e /usr/src/app/bcp_err.log -S localhost -U sa -P $SA_PASSWORD
/opt/mssql-tools/bin/bcp "CfmRecipes.cfm.[Reservation Transactions]" in "/usr/src/app/ReservationTransactions.csv" -e /usr/src/app/bcp_err.log -c -t',' -S localhost -U sa -P $SA_PASSWORD
/opt/mssql-tools/bin/bcp CfmRecipes.cfm.ActualCost in "/usr/src/app/ActualCost.csv" -e /usr/src/app/bcp_err.log -S localhost -U sa -P $SA_PASSWORD
/opt/mssql-tools/bin/bcp CfmRecipes.cfm.ActualCostSummary in "/usr/src/app/ActualCostSummary.csv" -e /usr/src/app/bcp_err.log -S localhost -U sa -P $SA_PASSWORD
/opt/mssql-tools/bin/bcp CfmRecipes.cfm.AmortizedCost in "/usr/src/app/AmortizedCost.csv" -e /usr/src/app/bcp_err.log -S localhost -U sa -P $SA_PASSWORD
/opt/mssql-tools/bin/bcp CfmRecipes.cfm.AmortizedCostSummary in "/usr/src/app/AmortizedCostSummary.csv" -e /usr/src/app/bcp_err.log -S localhost -U sa -P $SA_PASSWORD
