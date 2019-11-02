New York State’s Shrinking Middle Class
================

## Introduction

This analysis is inspired by a recent [American Enterprise Institute
report](https://www.aei.org/carpe-diem/three-charts-based-on-todays-census-report-show-that-the-us-middle-class-is-shrinking-because-theyre-moving-up/).
It shows the U.S. middle class is shrinking because they are moving up.

![Households by Income Class Over Time](http://www.aei.org/wp-content/uploads/2019/09/censusnew1.png)

Is this same pattern observed in New York State?

## Data Sources

### Income & Median Household Income

The original study was based off of CPS data. This study will not use
the CPS because it is not designed to produce reliable statistics below
a state level. Instead we will be relying on the Decenial Census and
American Community Survey (ACS) data. They provide data on the number of
households by income class.

  - **1980** - 1980 U.S. Census, General Socail and Economic
    Characteristics, Table 180. Income Characteristics in 1979 for
    Counties: 1980

  - **1990** - 1990 U.S. Census, Social and Economic Characteristics,
    Table 148. Income in 1989 of Households, Families, and Persons: 1990

  - **2000** - 2000 U.S. Census, Table P052. Household Income in 1999

  - **2008-2012 & 2013-2017** - American Community Survey, 5 Year
    Estimates, Table B19001. Household Income in the Past 12 Months

## Inflation

The original study adjusted the income figures for inflation using the
[CPI-U-RS](https://www.bls.gov/cpi/research-series/home.htm) series. We
will be using the same series to adjust our income figures into 2018
dollars.

### Metropolitian definitions

We will be producing metroplitan level estimates. Metro definitions are
from the [U.S. Bueau of Economic
Analysis](https://apps.bea.gov/regional/docs/msalist.cfm).
