#!/usr/bin/python
"""Script to transform Regions from Azure List Locations output."""
import argparse
import csv
import json
import os

from globals import DUMMY_SUBSCRIPTION_ID, ORI_SUBSCRIPTION_ID

DEFAULT_SRC_FILENAME = "Regions.json"
DEFAULT_DEST_FILENAME = "Regions.csv"


def transform_data(src_filename):
    """Transform source dataset to new dataset."""
    empty_paired_region = [{"name": ""}]

    rows = []

    with open(src_filename, encoding="utf-8") as file:
        source_data = json.load(file)
        for i in source_data["value"]:

            row = (
                i["displayName"],
                i["metadata"].get("geographyGroup", None),
                i["id"],
                str(i["metadata"].get("latitude", "")),
                str(i["metadata"].get("longitude", "")),
                i["name"],
                i["metadata"].get("pairedRegion", empty_paired_region)[0]["name"],
                i["metadata"].get("physicalLocation", None),
                i["metadata"].get("regionCategory", None),
                i["regionalDisplayName"],
                i["metadata"].get("regionType", None),
                i["id"].split("/")[2],
            )
            rows.append(list(row))

    rows.sort(key=lambda el: el[0])
    return rows


def remove_bad_records(rows):
    """Remove bad records."""
    col_id = 2
    col_physical_location = 7
    col_subscription_id = -1

    for row in rows:

        # Replacing subscripionid with dummy_subscription_id
        row[col_id] = row[col_id].replace(ORI_SUBSCRIPTION_ID, DUMMY_SUBSCRIPTION_ID)
        row[col_subscription_id] = row[col_subscription_id].replace(
            ORI_SUBSCRIPTION_ID, DUMMY_SUBSCRIPTION_ID
        )

        # Remove the , (comma) and " (quote)s from "Tokyo, Saitama" to Tokyo Saitama
        if row[col_physical_location]:
            row[col_physical_location] = row[col_physical_location].replace(",", "")

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
    rows = remove_bad_records(rows)
    save_file(rows, dest_filename)


if __name__ == "__main__":

    script_dir = os.path.dirname(__file__)
    sample_data_dir = os.path.join(script_dir, "../../sample_data/")
    sample_data_dir = os.path.normpath(sample_data_dir)

    parser = argparse.ArgumentParser(
        description="Transform Regions.",
        add_help=True,
    )
    parser.add_argument("--src_filename", "-s", help="Source filename.")
    parser.add_argument("--dest_filename", "-d", help="Destination filename")
    args = parser.parse_args()

    # Use environment variables if arguments are not passed
    arg_src_filename = args.src_filename or os.path.join(
        sample_data_dir, DEFAULT_SRC_FILENAME
    )
    arg_dest_filename = args.dest_filename or os.path.join(
        sample_data_dir, DEFAULT_DEST_FILENAME
    )

    main(arg_src_filename, arg_dest_filename)
