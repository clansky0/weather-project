Create Combined CSV File
================

``` r
library(tidyverse)
```

``` r
StormEvents_1950 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1950_c20250520.csv")
```

    ## Rows: 223 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1950 <- StormEvents_1950|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1951 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1951_c20250520.csv")
```

    ## Rows: 269 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1951 <- StormEvents_1951|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1952 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1952_c20250520.csv")
```

    ## Rows: 272 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1952 <- StormEvents_1952|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1953 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1953_c20250520.csv")
```

    ## Rows: 492 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1953 <- StormEvents_1953|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1954 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1954_c20250520.csv")
```

    ## Rows: 609 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1954 <- StormEvents_1954|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1955 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1955_c20250520.csv")
```

    ## Rows: 1413 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1955 <- StormEvents_1955|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1956 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1956_c20250520.csv")
```

    ## Rows: 1703 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1956 <- StormEvents_1956|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1957 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1957_c20250520.csv")
```

    ## Rows: 2184 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1957 <- StormEvents_1957|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1958 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1958_c20250520.csv")
```

    ## Rows: 2213 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1958 <- StormEvents_1958|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1959 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1959_c20250520.csv")
```

    ## Rows: 1813 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1959 <- StormEvents_1959|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1960 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1960_c20250520.csv")
```

    ## Rows: 1945 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1960 <- StormEvents_1960|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1961 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1961_c20250520.csv")
```

    ## Rows: 2246 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1961 <- StormEvents_1961|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1962 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1962_c20250520.csv")
```

    ## Rows: 2389 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1962 <- StormEvents_1962|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1963 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1963_c20250520.csv")
```

    ## Rows: 1968 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1963 <- StormEvents_1963|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1964 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1964_c20250520.csv")
```

    ## Rows: 2348 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1964 <- StormEvents_1964|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1965 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1965_c20250520.csv")
```

    ## Rows: 2835 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1965 <- StormEvents_1965|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1966 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1966_c20250520.csv")
```

    ## Rows: 2388 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1966 <- StormEvents_1966|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1967 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1967_c20250520.csv")
```

    ## Rows: 2688 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1967 <- StormEvents_1967|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1968 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1968_c20250520.csv")
```

    ## Rows: 3312 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1968 <- StormEvents_1968|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1969 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1969_c20250520.csv")
```

    ## Rows: 2926 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1969 <- StormEvents_1969|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1970 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1970_c20250520.csv")
```

    ## Rows: 3215 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1970 <- StormEvents_1970|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1971 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1971_c20250520.csv")
```

    ## Rows: 3471 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1971 <- StormEvents_1971|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1972 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1972_c20250520.csv")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

    ## Rows: 2171 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (16): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (25): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (10): WFO, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTHER_WFO, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1972 <- StormEvents_1972|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1973 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1973_c20250520.csv")
```

    ## Rows: 4453 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1973 <- StormEvents_1973|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1974 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1974_c20250520.csv")
```

    ## Rows: 5375 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (17): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (10): EPISODE_ID, WFO, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTHER_...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1974 <- StormEvents_1974|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1975 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1975_c20250520.csv")
```

    ## Rows: 4975 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1975 <- StormEvents_1975|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1976 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1976_c20250520.csv")
```

    ## Rows: 3768 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (11): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (16): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1976 <- StormEvents_1976|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1977 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1977_c20250520.csv")
```

    ## Rows: 3728 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (12): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (15): EPISODE_ID, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1977 <- StormEvents_1977|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1978 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1978_c20250520.csv")
```

    ## Rows: 3657 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (12): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (15): EPISODE_ID, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1978 <- StormEvents_1978|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1979 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1979_c20250520.csv")
```

    ## Rows: 4279 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (12): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (15): EPISODE_ID, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1979 <- StormEvents_1979|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1980 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1980_c20250520.csv")
```

    ## Rows: 6136 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (12): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (15): EPISODE_ID, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1980 <- StormEvents_1980|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1981 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1981_c20250520.csv")
```

    ## Rows: 4517 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (12): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (15): EPISODE_ID, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1981 <- StormEvents_1981|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1982 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1982_c20250520.csv")
```

    ## Rows: 7126 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (12): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (15): EPISODE_ID, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1982 <- StormEvents_1982|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1983 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1983_c20250520.csv")
```

    ## Rows: 8322 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (12): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (15): EPISODE_ID, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1983 <- StormEvents_1983|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1984 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1984_c20250520.csv")
```

    ## Rows: 7335 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (12): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (15): EPISODE_ID, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1984 <- StormEvents_1984|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1985 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1985_c20250520.csv")
```

    ## Rows: 7979 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (12): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (15): EPISODE_ID, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1985 <- StormEvents_1985|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1986 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1986_c20250520.csv")
```

    ## Rows: 8725 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (12): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (15): EPISODE_ID, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1986 <- StormEvents_1986|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1987 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1987_c20250520.csv")
```

    ## Rows: 7363 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (12): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (15): EPISODE_ID, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1987 <- StormEvents_1987|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1988 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1988_c20250520.csv")
```

    ## Rows: 7257 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (12): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (15): EPISODE_ID, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1988 <- StormEvents_1988|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1989 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1989_c20250520.csv")
```

    ## Rows: 10407 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (12): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (15): EPISODE_ID, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1989 <- StormEvents_1989|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1990 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1990_c20250520.csv")
```

    ## Rows: 10945 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (12): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (15): EPISODE_ID, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1990 <- StormEvents_1990|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1991 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1991_c20250520.csv")
```

    ## Rows: 12516 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (12): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (15): EPISODE_ID, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1991 <- StormEvents_1991|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1992 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1992_c20250520.csv")
```

    ## Rows: 13534 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (12): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (15): EPISODE_ID, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTH...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1992 <- StormEvents_1992|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1993 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1993_c20250520.csv")
```

    ## Rows: 8664 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (17): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (23): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (11): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1993 <- StormEvents_1993|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1994 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1994_c20250520.csv")
```

    ## Rows: 15627 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (17): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (23): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl (11): EPISODE_ID, WFO, SOURCE, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1994 <- StormEvents_1994|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1995 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1995_c20250520.csv")
```

    ## Rows: 20464 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (19): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, BEGIN_DATE_TIME, ...
    ## dbl (23): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (9): EPISODE_ID, WFO, MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTHER_...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1995 <- StormEvents_1995|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1996 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1996_c20250520.csv")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

    ## Rows: 48534 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (20): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (7): MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTHER_WFO, TOR_OTHER_CZ...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1996 <- StormEvents_1996|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1997 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1997_c20250520.csv")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

    ## Rows: 41991 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (20): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (7): MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTHER_WFO, TOR_OTHER_CZ...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1997 <- StormEvents_1997|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1998 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1998_c20250520.csv")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

    ## Rows: 50973 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (20): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (7): MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTHER_WFO, TOR_OTHER_CZ...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1998 <- StormEvents_1998|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_1999 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d1999_c20250520.csv")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

    ## Rows: 46383 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (20): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (7): MAGNITUDE_TYPE, FLOOD_CAUSE, CATEGORY, TOR_OTHER_WFO, TOR_OTHER_CZ...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_1999 <- StormEvents_1999|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2000 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2000_c20250520.csv")
```

    ## Rows: 52007 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (21): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (6): FLOOD_CAUSE, CATEGORY, TOR_OTHER_WFO, TOR_OTHER_CZ_STATE, TOR_OTHE...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2000 <- StormEvents_2000|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2001 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2001_c20250520.csv")
```

    ## Rows: 48875 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (21): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (6): FLOOD_CAUSE, CATEGORY, TOR_OTHER_WFO, TOR_OTHER_CZ_STATE, TOR_OTHE...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2001 <- StormEvents_2001|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2002 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2002_c20250520.csv")
```

    ## Rows: 50936 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (21): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (6): FLOOD_CAUSE, CATEGORY, TOR_OTHER_WFO, TOR_OTHER_CZ_STATE, TOR_OTHE...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2002 <- StormEvents_2002|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2003 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2003_c20250520.csv")
```

    ## Rows: 52956 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (21): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (6): FLOOD_CAUSE, CATEGORY, TOR_OTHER_WFO, TOR_OTHER_CZ_STATE, TOR_OTHE...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2003 <- StormEvents_2003|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2004 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2004_c20250520.csv")
```

    ## Rows: 52409 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (21): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (6): FLOOD_CAUSE, CATEGORY, TOR_OTHER_WFO, TOR_OTHER_CZ_STATE, TOR_OTHE...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2004 <- StormEvents_2004|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2005 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2005_c20250520.csv")
```

    ## Rows: 53976 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (21): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (6): FLOOD_CAUSE, CATEGORY, TOR_OTHER_WFO, TOR_OTHER_CZ_STATE, TOR_OTHE...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2005 <- StormEvents_2005|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2006 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2006_c20250520.csv")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

    ## Rows: 56400 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (22): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (5): CATEGORY, TOR_OTHER_WFO, TOR_OTHER_CZ_STATE, TOR_OTHER_CZ_FIPS, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2006 <- StormEvents_2006|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2007 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2007_c20250520.csv")
```

    ## Rows: 59011 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (26): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (25): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2007 <- StormEvents_2007|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2008 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2008_c20250520.csv")
```

    ## Rows: 71190 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (26): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (25): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2008 <- StormEvents_2008|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2009 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2009_c20250520.csv")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

    ## Rows: 57398 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (26): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (1): CATEGORY
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2009 <- StormEvents_2009|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2010 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2010_c20250520.csv")
```

    ## Rows: 62807 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (26): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (1): CATEGORY
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2010 <- StormEvents_2010|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2011 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2011_c20250520.csv")
```

    ## Rows: 79091 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (26): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (1): CATEGORY
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2011 <- StormEvents_2011|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2012 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2012_c20250520.csv")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

    ## Rows: 64503 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (26): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (1): CATEGORY
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2012 <- StormEvents_2012|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2013 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2013_c20250520.csv")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

    ## Rows: 59986 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (26): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (1): CATEGORY
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2013 <- StormEvents_2013|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2014 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2014_c20250520.csv")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

    ## Rows: 59475 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (22): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (5): CATEGORY, TOR_OTHER_WFO, TOR_OTHER_CZ_STATE, TOR_OTHER_CZ_FIPS, TO...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2014 <- StormEvents_2014|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2015 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2015_c20250818.csv")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

    ## Rows: 57907 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (26): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (1): CATEGORY
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2015 <- StormEvents_2015|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2016 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2016_c20250818.csv")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

    ## Rows: 56005 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (25): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (25): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (1): CATEGORY
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2016 <- StormEvents_2016|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2017 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2017_c20250520.csv")
```

    ## Rows: 57029 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (26): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (25): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2017 <- StormEvents_2017|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2018 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2018_c20250520.csv")
```

    ## Rows: 62697 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (25): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (26): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2018 <- StormEvents_2018|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2019 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2019_c20250520.csv")
```

    ## Rows: 67861 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (26): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (25): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2019 <- StormEvents_2019|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2020 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2020_c20250702.csv")
```

    ## Rows: 61278 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (26): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (25): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2020 <- StormEvents_2020|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2021 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2021_c20250520.csv")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

    ## Rows: 61389 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (26): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (1): CATEGORY
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2021 <- StormEvents_2021|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2022 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2022_c20250721.csv")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

    ## Rows: 69887 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (26): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (1): CATEGORY
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2022 <- StormEvents_2022|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2023 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2023_c20250731.csv")
```

    ## Warning: One or more parsing issues, call `problems()` on your data frame for details,
    ## e.g.:
    ##   dat <- vroom(...)
    ##   problems(dat)

    ## Rows: 75593 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (26): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (24): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## lgl  (1): CATEGORY
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2023 <- StormEvents_2023|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
StormEvents_2024 <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d2024_c20250818.csv")
```

    ## Rows: 69493 Columns: 51
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: ","
    ## chr (26): STATE, MONTH_NAME, EVENT_TYPE, CZ_TYPE, CZ_NAME, WFO, BEGIN_DATE_T...
    ## dbl (25): BEGIN_YEARMONTH, BEGIN_DAY, BEGIN_TIME, END_YEARMONTH, END_DAY, EN...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

``` r
StormEvents_2024 <- StormEvents_2024|>
select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,
-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,
-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,  -END_AZIMUTH,
-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)
```

``` r
all_storms <- rbind(StormEvents_1950,
                    StormEvents_1951,
                    StormEvents_1952,
                    StormEvents_1953,
                    StormEvents_1954,
                    StormEvents_1955,
                    StormEvents_1956,
                    StormEvents_1957,
                    StormEvents_1958,
                    StormEvents_1959,
                    StormEvents_1960,
                    StormEvents_1961,
                    StormEvents_1962,
                    StormEvents_1963,
                    StormEvents_1964,
                    StormEvents_1965,
                    StormEvents_1966,
                    StormEvents_1967,
                    StormEvents_1968,
                    StormEvents_1969,
                    StormEvents_1970,
                    StormEvents_1971,
                    StormEvents_1972,
                    StormEvents_1973,
                    StormEvents_1974,
                    StormEvents_1975,
                    StormEvents_1976,
                    StormEvents_1977,
                    StormEvents_1978,
                    StormEvents_1979,
                    StormEvents_1980,
                    StormEvents_1981,
                    StormEvents_1982,
                    StormEvents_1983,
                    StormEvents_1984,
                    StormEvents_1985,
                    StormEvents_1986,
                    StormEvents_1987,
                    StormEvents_1988,
                    StormEvents_1989,
                    StormEvents_1990,
                    StormEvents_1991,
                    StormEvents_1992,
                    StormEvents_1993,
                    StormEvents_1994,
                    StormEvents_1995,
                    StormEvents_1996,
                    StormEvents_1997,
                    StormEvents_1998,
                    StormEvents_1999,
                    StormEvents_2000,
                    StormEvents_2001,
                    StormEvents_2002,
                    StormEvents_2003,
                    StormEvents_2004,
                    StormEvents_2005,
                    StormEvents_2006,
                    StormEvents_2007,
                    StormEvents_2008,
                    StormEvents_2009,
                    StormEvents_2010,
                    StormEvents_2011,
                    StormEvents_2012,
                    StormEvents_2013,
                    StormEvents_2014,
                    StormEvents_2015,
                    StormEvents_2016,
                    StormEvents_2017,
                    StormEvents_2018,
                    StormEvents_2019,
                    StormEvents_2020)
write_csv(all_storms, file="../data/ignore/all-storms.csv")
```

``` r
all_storms <- read.csv("../data/ignore/all-storms.csv")
```

``` r
least_common <- all_storms|>
  count(EVENT_TYPE)|>
  arrange(n)

#exclude  n < 1000
all_storms <- all_storms|>
  filter(!EVENT_TYPE %in% c("Volcanic Ashfall", "Tsunami", "Lakeshore Flood", "Dense Smoke",
                             "Northern Lights", "Seiche", "Volcanic Ash", "Dust Devil", 
                            "Astronomical Low Tide", "Freezing Fog", "Tropical Depression", 
                            "Avalanche", "Dust Storm", "Sleet", "Debris Flow", "Rip Current" ,
                            "Lake-Effect Snow", "Storm Surge/Tide", "Sneakerwave",""))

all_storms|>
  count(EVENT_TYPE)|>
  arrange(n)
```

    ##                    EVENT_TYPE      n
    ## 1            Marine Lightning      1
    ## 2            Marine Dense Fog     10
    ## 3  Marine Tropical Depression     15
    ## 4    Marine Hurricane/Typhoon     77
    ## 5          Marine Strong Wind    148
    ## 6       Marine Tropical Storm    323
    ## 7            Marine High Wind    579
    ## 8                 Marine Hail    727
    ## 9         Hurricane (Typhoon)   1995
    ## 10              Coastal Flood   3328
    ## 11                 Waterspout   5280
    ## 12             Tropical Storm   5860
    ## 13                   Wildfire   7570
    ## 14               Funnel Cloud   8874
    ## 15                  High Surf   9626
    ## 16             Excessive Heat   9770
    ## 17                  Ice Storm  11306
    ## 18    Extreme Cold/Wind Chill  12437
    ## 19               Frost/Freeze  12933
    ## 20                  Dense Fog  14325
    ## 21            Cold/Wind Chill  14363
    ## 22                   Blizzard  14537
    ## 23                  Lightning  16923
    ## 24                       Heat  22260
    ## 25                Strong Wind  22619
    ## 26                 Heavy Rain  26673
    ## 27   Marine Thunderstorm Wind  30796
    ## 28                    Drought  57856
    ## 29                      Flood  58470
    ## 30             Winter Weather  63702
    ## 31                 Heavy Snow  64078
    ## 32                    Tornado  72117
    ## 33                  High Wind  73927
    ## 34               Winter Storm  76123
    ## 35                Flash Flood  88692
    ## 36                       Hail 375625
    ## 37          Thunderstorm Wind 468069

``` r
earliest_storms <- all_storms|>
  select(YEAR, EVENT_TYPE)|>
  group_by(EVENT_TYPE)|>
  summarise(min_year = min(YEAR))|>
  arrange(min_year)
  


print(earliest_storms)
```

    ## # A tibble: 37 × 2
    ##    EVENT_TYPE        min_year
    ##    <chr>                <int>
    ##  1 Tornado               1950
    ##  2 Hail                  1955
    ##  3 Thunderstorm Wind     1955
    ##  4 Blizzard              1996
    ##  5 Coastal Flood         1996
    ##  6 Cold/Wind Chill       1996
    ##  7 Dense Fog             1996
    ##  8 Drought               1996
    ##  9 Flash Flood           1996
    ## 10 Flood                 1996
    ## # ℹ 27 more rows
