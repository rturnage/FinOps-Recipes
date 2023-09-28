/*****************************************************************
Tagged Resources Compliance SQL Transformations

There are several different ways to calculate the transformation.
- Direct Query
	- Selected from Detail Table
	- or Selected from Summary Table
- View over Core Tables
	- Detailed Table
	- or Summary Table
- Dedicated Tagged Resources Table
	- Updated with stored procedure

*****************************************************************/

DECLARE /* Set Parameters */
	@last_week date
	, @target_tag [nvarchar](300)
SET @target_tag = '<example tag>'
SET @last_week = DATEADD(day, -7, convert(date, GETDATE()))

BEGIN /* Direct Query via Detail Table */
	select  [Date] as [date]
		,[CostCenter] as [cost_center]
		,[SubscriptionId] as [subscription_id]
		,[SubscriptionName] as [subscription_name]
		,[ResourceGroup] as [resource_group]
		,[ConsumedService] as [consumed_service]
		,[MeterCategory] as [meter_category]
		,[MeterSubCategory] as [meter_sub_category]
		,[MeterName] as [meter_name]
		,[ProductName] as [product_name]
		,[PartNumber] as [part_number]
		,Count(Distinct [ResourceId]) as resource_count
		,Sum(case when charindex(@target_tag, [Tags],0) > 0 then 1 else 0 end) as compliant_tag_resource_count
		,Sum([CostInBillingCurrency]) as cost
	FROM [costmanagement].[ActualCost]
	WHERE Date = @last_week
	Group By
		[Date]
		,[CostCenter]
		,[SubscriptionId]
		,[SubscriptionName]
		,[ResourceGroup]
		,[ConsumedService]
		,[MeterCategory]
		,[MeterSubCategory]
		,[MeterName]
		,[ProductName]
		,[PartNumber]
	Order by  [Date]
		,[CostCenter]
		,[SubscriptionId]
		,[SubscriptionName]
		,[ResourceGroup]
		,[ConsumedService]
		,[MeterCategory]
		,[MeterSubCategory]
		,[MeterName]
		,[ProductName]
		,[PartNumber]
END

BEGIN /* Get Tagged Resources from Summary Table */
	select  [Date] as [date]
		,[CostCenter] as [cost_center]
		,[SubscriptionId] as [subscription_id]
		,[SubscriptionName] as [subscription_name]
		,[ResourceGroup] as [resource_group]
		,[ConsumedService] as [consumed_service]
		,[MeterCategory] as [meter_category]
		,[MeterSubCategory] as [meter_sub_category]
		,[MeterName] as [meter_name]
		,[ProductName] as [product_name]
		,[PartNumber] as [part_number]
		,Sum([ResourceIdCount]) as [resource_id_count]
		,Sum(case when charindex(@target_tag, [Tags],0) > 0 then 1 else 0 end) as compliant_tag_resource_count
		,Sum([CostInBillingCurrency]) as cost
	FROM [costmanagement].[ActualCostSummary]
	WHERE Date = @last_week
	Group By
		[Date]
		,[CostCenter]
		,[SubscriptionId]
		,[SubscriptionName]
		,[ResourceGroup]
		,[ConsumedService]
		,[MeterCategory]
		,[MeterSubCategory]
		,[MeterName]
		,[ProductName]
		,[PartNumber]
	Order by  [Date]
		,[CostCenter]
		,[SubscriptionId]
		,[SubscriptionName]
		,[ResourceGroup]
		,[ConsumedService]
		,[MeterCategory]
		,[MeterSubCategory]
		,[MeterName]
		,[ProductName]
		,[PartNumber]
END

BEGIN /* Create View of Tagged Resources from summary table */
	Create View [costmanagement].[TaggedResources] as

		select  [Date] as [date]
			,[CostCenter] as [cost_center]
			,[SubscriptionId] as [subscription_id]
			,[SubscriptionName] as [subscription_name]
			,[ResourceGroup] as [resource_group]
			,[ConsumedService] as [consumed_service]
			,[MeterCategory] as [meter_category]
			,[MeterSubCategory] as [meter_sub_category]
			,[MeterName] as [meter_name]
			,[ProductName] as [product_name]
			,[PartNumber] as [part_number]
			,Sum([ResourceIdCount]) as [resource_id_count]
			,Sum(case when charindex(@target_tag, [Tags],0) > 0 then 1 else 0 end) as compliant_tag_resource_count
			,Sum([CostInBillingCurrency]) as cost
		FROM [costmanagement].[ActualCostSummary]
		Group By
			[Date]
			,[CostCenter]
			,[SubscriptionId]
			,[SubscriptionName]
			,[ResourceGroup]
			,[ConsumedService]
			,[MeterCategory]
			,[MeterSubCategory]
			,[MeterName]
			,[ProductName]
			,[PartNumber]
END

BEGIN /* Update Tagged Resource Table via stored procedure */
	execute costmanagement.UpdateTaggedResources @last_week, GETDATE(), @target_tag
END
