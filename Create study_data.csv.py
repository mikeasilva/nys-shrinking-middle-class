# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 05:22:23 2019

@author: Michael
"""
import numpy as np
import pandas as pd

parameters = {
    "1980": {
        "lower_bound_low_class": 10000,
        "upper_bound_low_class": 14999,
        "dollar_value_low_class": 10818,
        "lower_bound_middle_class": 25000,
        "upper_bound_middle_class": 34999,
        "dollar_value_middle_class": 30909,
        "below_low_class_columns": ["hh_lt_5K", "hh_5K_to_7499", "hh_7500_to_9999"],
        "above_low_class_columns": [
            "hh_lt_5K",
            "hh_5K_to_7499",
            "hh_7500_to_9999",
            "hh_10K_to_14999",
        ],
        "below_middle_class_columns": [
            "hh_lt_5K",
            "hh_5K_to_7499",
            "hh_7500_to_9999",
            "hh_10K_to_14999",
            "hh_15K_to_19999",
            "hh_20K_to_24999",
        ],
        "above_middle_class_columns": [
            "hh_lt_5K",
            "hh_5K_to_7499",
            "hh_7500_to_9999",
            "hh_10K_to_14999",
            "hh_15K_to_19999",
            "hh_20K_to_24999",
            "hh_25K_to_34999",
        ],
    },
    "1990": {
        "lower_bound_low_class": 15000,
        "upper_bound_low_class": 24999,
        "dollar_value_low_class": 17850,
        "lower_bound_middle_class": 50000,
        "upper_bound_middle_class": 74999,
        "dollar_value_middle_class": 51001,
        "below_low_class_columns": [
            "hh_lt_5K", 
            "hh_5K_to_9999", 
            "hh_10K_to_14999"
        ],
        "above_low_class_columns": [
            "hh_lt_5K",
            "hh_5K_to_9999",
            "hh_10K_to_14999",
            "hh_15K_to_24999",
        ],
        "below_middle_class_columns": [
            "hh_lt_5K",
            "hh_5K_to_9999",
            "hh_10K_to_14999",
            "hh_15K_to_24999",
            "hh_25K_to_34999",
            "hh_35K_to_49999",
        ],
        "above_middle_class_columns": [
            "hh_lt_5K",
            "hh_5K_to_9999",
            "hh_10K_to_14999",
            "hh_15K_to_24999",
            "hh_25K_to_34999",
            "hh_35K_to_49999",
            "hh_50K_to_74999",
        ],
    },
    "2000": {
        "lower_bound_low_class": 20000,
        "upper_bound_low_class": 24999,
        "dollar_value_low_class": 23150,
        "lower_bound_middle_class": 60000,
        "upper_bound_middle_class": 74999,
        "dollar_value_middle_class": 66144,
        "below_low_class_columns": [
            "hh_lt_10K",
            "hh_10K_to_14999",
            "hh_15K_to_19999"
        ],
        "above_low_class_columns": [
            "hh_lt_10K",
            "hh_10K_to_14999",
            "hh_15K_to_19999",
            "hh_20K_to_24999",
        ],
        "below_middle_class_columns": [
            "hh_lt_10K",
            "hh_10K_to_14999",
            "hh_15K_to_19999",
            "hh_20K_to_24999",
            "hh_25K_to_29999",
            "hh_30K_to_34999",
            "hh_35K_to_39999",
            "hh_40K_to_44999",
            "hh_45K_to_49999",
            "hh_50K_to_59999",
        ],
        "above_middle_class_columns": [
            "hh_lt_10K",
            "hh_10K_to_14999",
            "hh_15K_to_19999",
            "hh_20K_to_24999",
            "hh_25K_to_29999",
            "hh_30K_to_34999",
            "hh_35K_to_39999",
            "hh_40K_to_44999",
            "hh_45K_to_49999",
            "hh_50K_to_59999",
            "hh_60K_to_74999",
        ],
    },
    "2012": {
        "lower_bound_low_class": 30000,
        "upper_bound_low_class": 34999,
        "dollar_value_low_class": 31943,
        "lower_bound_middle_class": 75000,
        "upper_bound_middle_class": 99999,
        "dollar_value_middle_class": 91266,
        "below_low_class_columns": [
            "hh_lt_10K",
            "hh_10K_to_14999",
            "hh_15K_to_19999",
            "hh_20K_to_24999",
            "hh_25K_to_29999",
        ],
        "above_low_class_columns": [
            "hh_lt_10K",
            "hh_10K_to_14999",
            "hh_15K_to_19999",
            "hh_20K_to_24999",
            "hh_25K_to_29999",
            "hh_30K_to_34999",
        ],
        "below_middle_class_columns": [
            "hh_lt_10K",
            "hh_10K_to_14999",
            "hh_15K_to_19999",
            "hh_20K_to_24999",
            "hh_25K_to_29999",
            "hh_30K_to_34999",
            "hh_35K_to_39999",
            "hh_40K_to_44999",
            "hh_45K_to_49999",
            "hh_50K_to_59999",
            "hh_60K_to_74999",
        ],
        "above_middle_class_columns": [
            "hh_lt_10K",
            "hh_10K_to_14999",
            "hh_15K_to_19999",
            "hh_20K_to_24999",
            "hh_25K_to_29999",
            "hh_30K_to_34999",
            "hh_35K_to_39999",
            "hh_40K_to_44999",
            "hh_45K_to_49999",
            "hh_50K_to_59999",
            "hh_60K_to_74999",
            "hh_75K_to_99999",
        ],
    },
    "2017": {
        "lower_bound_low_class": 30000,
        "upper_bound_low_class": 34999,
        "dollar_value_low_class": 34167,
        "lower_bound_middle_class": 75000,
        "upper_bound_middle_class": 99999,
        "dollar_value_middle_class": 97620,
        "below_low_class_columns": [
            "hh_lt_10K",
            "hh_10K_to_14999",
            "hh_15K_to_19999",
            "hh_20K_to_24999",
            "hh_25K_to_29999",
        ],
        "above_low_class_columns": [
            "hh_lt_10K",
            "hh_10K_to_14999",
            "hh_15K_to_19999",
            "hh_20K_to_24999",
            "hh_25K_to_29999",
            "hh_30K_to_34999",
        ],
        "below_middle_class_columns": [
            "hh_lt_10K",
            "hh_10K_to_14999",
            "hh_15K_to_19999",
            "hh_20K_to_24999",
            "hh_25K_to_29999",
            "hh_30K_to_34999",
            "hh_35K_to_39999",
            "hh_40K_to_44999",
            "hh_45K_to_49999",
            "hh_50K_to_59999",
            "hh_60K_to_74999",
        ],
        "above_middle_class_columns": [
            "hh_lt_10K",
            "hh_10K_to_14999",
            "hh_15K_to_19999",
            "hh_20K_to_24999",
            "hh_25K_to_29999",
            "hh_30K_to_34999",
            "hh_35K_to_39999",
            "hh_40K_to_44999",
            "hh_45K_to_49999",
            "hh_50K_to_59999",
            "hh_60K_to_74999",
            "hh_75K_to_99999",
        ],
    },
}

files = {
    "1980": "data/1980_GSEC_TABLE_180.csv",
    "1990": "data/1990_SEC_TABLE_148.csv",
    "2000": "data/2000_SF3_P052.csv",
    "2012": "data/ACS_12_5YR_B19001.csv",
    "2017": "data/ACS_17_5YR_B19001.csv",
}


def find_proportion(below, above, total, lower_bound, upper_bound, dollar_value):
    Pa = below / total
    Pb = above / total
    theta = (np.log10(1 - Pa) - np.log10(1 - Pb)) / (
        np.log10(upper_bound) - np.log10(lower_bound)
    )
    k = ((Pb - Pa) / ((1 / (lower_bound ** theta)) - (1 / (upper_bound ** theta)))) ** (
        1 / theta
    )
    proportion = 0
    for p in np.arange(Pa, Pb, 0.0000001):
        estimate = k / ((1 - p) ** (1 / theta))
        # print(str(p) + " = $" + str(estimate))
        if estimate > dollar_value:
            break
        proportion = p
    return proportion


for year, file_name in files.items():
    print("Building " + year + " Study Data")

    df = pd.read_csv(file_name, dtype={"geoid": "object"})

    df["below_low_class"] = df[parameters[year]["below_low_class_columns"]].sum(axis=1)
    df["above_low_class"] = df[parameters[year]["above_low_class_columns"]].sum(axis=1)
    lower_bound_low_class = parameters[year]["lower_bound_low_class"]
    upper_bound_low_class = parameters[year]["upper_bound_low_class"]
    dollar_value_low_class = parameters[year]["dollar_value_low_class"]

    df["below_middle_class"] = df[parameters[year]["below_middle_class_columns"]].sum(
        axis=1
    )
    df["above_middle_class"] = df[parameters[year]["above_middle_class_columns"]].sum(
        axis=1
    )
    lower_bound_middle_class = parameters[year]["lower_bound_middle_class"]
    upper_bound_middle_class = parameters[year]["upper_bound_middle_class"]
    dollar_value_middle_class = parameters[year]["dollar_value_middle_class"]
    print(" Getting Low Class Proportions...")
    df["low_class"] = df.apply(
        lambda row: find_proportion(
            row["below_low_class"],
            row["above_low_class"],
            row["hh"],
            lower_bound_low_class,
            upper_bound_low_class,
            dollar_value_low_class,
        ),
        axis=1,
    )
    print(" Getting Middle Class Proportions...")
    df["middle_class"] = df.apply(
        lambda row: find_proportion(
            row["below_middle_class"],
            row["above_middle_class"],
            row["hh"],
            lower_bound_middle_class,
            upper_bound_middle_class,
            dollar_value_middle_class,
        ),
        axis=1,
    )
    df["middle_class"] = df["middle_class"] - df["low_class"]
    print(" Finalizing Data...")
    df["upper_class"] = 1 - df["low_class"] - df["middle_class"]
    df["year"] = int(year)
    df = df[["geoid", "hh", "low_class", "middle_class", "upper_class", "year"]]

    try:
        study_data = study_data.append(df)
    except NameError:
        study_data = df

study_data.to_csv("data/study_data.csv", index=False)
