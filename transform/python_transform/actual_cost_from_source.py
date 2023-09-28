#!/usr/bin/python
"""Script to transform Actual Costs from source."""
import argparse
import csv
import os
import random
import re

from globals import (
    DUMMY_ACCOUNT_NAME_MAP,
    DUMMY_RESOURCE_MAP,
    DUMMY_RG_MAP,
    DUMMY_EMAIL_MAP,
    SAMPLE_DATA_PATH,
    NOUN_WORDS,
    generate_resource_name,
    generate_rg_name,
    replace_row_by_pattern,
    replace_row_subscription,
    save_dummy_map_data,
    convert_iso_date,
)

DEFAULT_SRC_FILENAME = "ActualCost_Exported.csv"
DEFAULT_DEST_FILENAME = "ActualCosts.csv"


def transform_data(src_filename):
    """Transform source dataset to new dataset."""
    rows = []

    COL_InvoiceSectionName = 0
    COL_AccountName = 1
    COL_AccountOwnerId = 2
    COL_SubscriptionId = 3
    COL_SubscriptionName = 4
    COL_ResourceGroup = 5
    COL_ResourceLocation = 6
    COL_Date = 7
    COL_ProductName = 8
    COL_MeterCategory = 9
    COL_MeterSubCategory = 10
    COL_MeterId = 11
    COL_MeterName = 12
    COL_MeterRegion = 13
    COL_UnitOfMeasure = 14
    COL_Quantity = 15
    COL_EffectivePrice = 16
    COL_CostInBillingCurrency = 17
    COL_CostCenter = 18
    COL_ConsumedService = 19
    COL_ResourceId = 20
    COL_Tags = 21
    COL_OfferId = 22
    COL_AdditionalInfo = 23
    COL_ServiceInfo1 = 24
    COL_ServiceInfo2 = 25
    COL_ResourceName = 26
    COL_ReservationId = 27
    COL_ReservationName = 28
    COL_UnitPrice = 29
    COL_ProductOrderId = 30
    COL_ProductOrderName = 31
    COL_Term = 31
    COL_PublisherType = 33
    COL_PublisherName = 34
    COL_ChargeType = 35
    COL_Frequency = 36
    COL_PricingModel = 37
    COL_AvailabilityZone = 38
    COL_BillingAccountId = 39
    COL_BillingAccountName = 40
    COL_BillingCurrencyCode = 41
    COL_BillingPeriodStartDate = 42
    COL_BillingPeriodEndDate = 43
    COL_BillingProfileId = 44
    COL_BillingProfileName = 45
    COL_InvoiceSectionId = 46
    COL_IsAzureCreditEligible = 47
    COL_PartNumber = 48
    COL_PayGPrice = 49
    COL_PlanName = 50
    COL_ServiceFamily = 51
    COL_CostAllocationRuleName = 52

    with open(src_filename, encoding="utf-8") as file:
        source_data = csv.reader(file)
        # Skip header row
        next(source_data)
        for i in source_data:
            row = (
                i[COL_InvoiceSectionName],
                i[COL_AccountName],
                i[COL_AccountOwnerId],
                i[COL_SubscriptionId],
                i[COL_SubscriptionName],
                i[COL_ResourceGroup],
                i[COL_ResourceLocation],
                i[COL_Date],
                i[COL_ProductName],
                i[COL_MeterCategory],
                i[COL_MeterSubCategory],
                i[COL_MeterId],
                i[COL_MeterName],
                i[COL_MeterRegion],
                i[COL_UnitOfMeasure],
                i[COL_Quantity],
                i[COL_EffectivePrice],
                i[COL_CostInBillingCurrency],
                i[COL_CostCenter],
                i[COL_ConsumedService],
                i[COL_ResourceId],
                i[COL_Tags],
                i[COL_OfferId],
                i[COL_AdditionalInfo],
                i[COL_ServiceInfo1],
                i[COL_ServiceInfo2],
                i[COL_ResourceName],
                i[COL_ReservationId],
                i[COL_ReservationName],
                i[COL_UnitPrice],
                i[COL_ProductOrderId],
                i[COL_ProductOrderName],
                i[COL_Term],
                i[COL_PublisherType],
                i[COL_PublisherName],
                i[COL_ChargeType],
                i[COL_Frequency],
                i[COL_PricingModel],
                i[COL_AvailabilityZone],
                i[COL_BillingAccountId],
                i[COL_BillingAccountName],
                i[COL_BillingCurrencyCode],
                i[COL_BillingPeriodStartDate],
                i[COL_BillingPeriodEndDate],
                i[COL_BillingProfileId],
                i[COL_BillingProfileName],
                i[COL_InvoiceSectionId],
                i[COL_IsAzureCreditEligible],
                i[COL_PartNumber],
                i[COL_PayGPrice],
                i[COL_PlanName],
                i[COL_ServiceFamily],
                i[COL_CostAllocationRuleName]
            )
            rows.append(list(row))
    return rows

def generate_account_name():
    """Generate random account name."""
    rnd_word = random.choice(NOUN_WORDS)
    return f"{rnd_word[0].upper()}{rnd_word[1:]} Account"

def generate_email_address():
    """Generate random email."""
    rnd_word1 = random.choice(NOUN_WORDS)
    rnd_word2 = random.choice(NOUN_WORDS)
    rnd_number = random.randint(100,999)
    return f"{rnd_word1}_{rnd_word2}{rnd_number}@example.com"

# def replaced_account_name(matchobj):
#     """Replace account name."""
#     item = matchobj.group(1)
#     if item in DUMMY_ACCOUNT_NAME_MAP:
#         new_name = DUMMY_ACCOUNT_NAME_MAP[item]
#     else:
#         new_name = generate_account_name()
#         DUMMY_ACCOUNT_NAME_MAP[item] = new_name
#     new_name = f"/billingAccounts/{new_name}/"
#     return new_name

def replaced_account_name(item):
    """Replace account name."""
    if item in DUMMY_ACCOUNT_NAME_MAP:
        new_name = DUMMY_ACCOUNT_NAME_MAP[item]
    else:
        new_name = generate_account_name()
        DUMMY_ACCOUNT_NAME_MAP[item] = new_name
    return new_name

def replaced_email(item):
    """Replace email address."""
    if item in DUMMY_EMAIL_MAP:
        new_name = DUMMY_EMAIL_MAP[item]
    else:
        new_name = generate_email_address()
        DUMMY_EMAIL_MAP[item] = new_name
    return new_name

def replace_row_account_name(row, columns):
    """Replace row account name with dummy value."""
    pattern = re.compile(r"\/billingAccounts\/([\w\-]+)\/")
    return replace_row_by_pattern(row, columns, pattern, replaced_account_name)

def replaced_invoice_section_name(row, columns):
    """Replace row invoice section name with dummy value."""
    pattern = re.compile(r"\/billingAccounts\/([\w\-]+)\/")
    return replace_row_by_pattern(row, columns, pattern, replaced_account_name)

# def replace_row_email(row, columns):
#     """Replace row email with dummy value."""
#     pattern = re.compile(r"\([\w\-]+)")
#     return replace_row_by_pattern(row, columns, pattern, replaced_account_name)


def replace_with_dummy_data(rows):
    """Replace with dummy data."""
    col_invoice_section_name = 0
    col_account_name = 0
    col_email = 1
    col_cur_enrollment_id = 7
    col_id = 12
    col_pur_enrollment_id = 14
    col_sub_id = 15
    col_sub_name = 16
    
    for row in rows:
        # Replace Invoice Section Name with Dummy name
        row[col_account_name] = replaced_invoice_section_name(row[col_invoice_section_name]) 

        # Replace Account Name with Dummy name
        row[col_account_name] = replaced_account_name(row[col_account_name])      

        # Replace Owner Email with dummy email
        row[col_email] = replaced_email(row[col_email])
        # Replace Cur Enrollment

        # Replace Account ID in ID

        # Replace purchasingEnrollment
        # Replace purchasingSubscriptionGuid
        # Replace purchasingSubscriptionName

    return rows


def save_file(rows, dest_filename):
    """Save data to file."""
    with open(dest_filename, "w", newline="", encoding="utf-8") as dest_file:
        writer = csv.writer(dest_file)

        for row in rows:
            # print(row)
            writer.writerow(row)


def main(src_filename, dest_filename):
    """Transormation main logic."""
    rows = transform_data(src_filename)
    rows = replace_with_dummy_data(rows)
    save_file(rows, dest_filename)

    save_dummy_map_data()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Transform Reservation Transactions.",
        add_help=True,
    )
    parser.add_argument("--src_filename", "-s", help="Source filename.")
    parser.add_argument("--dest_filename", "-d", help="Destination filename")
    args = parser.parse_args()

    # Use environment variables if arguments are not passed
    arg_src_filename = args.src_filename or os.path.join(
        SAMPLE_DATA_PATH, DEFAULT_SRC_FILENAME
    )
    arg_dest_filename = args.dest_filename or os.path.join(
        SAMPLE_DATA_PATH, DEFAULT_DEST_FILENAME
    )

    main(arg_src_filename, arg_dest_filename)