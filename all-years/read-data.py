
#create code chunks for each year to read csv
for i in range(60):
  year = i + 1950
  print('```{r ', year, '}', sep = '')
  print ('StormEvents_', year, ' <- read_csv("../data/ignore/StormEvents_details-ftp_v1.0_d',year,'_c20250520.csv")', sep = '')
  print('StormEvents_', year, ' <- StormEvents_', year, '|>', sep = '')
  print('select (-EPISODE_ID, -CZ_TYPE, -CZ_FIPS, -CZ_NAME, -WFO, -BEGIN_DATE_TIME, -CZ_TIMEZONE,')
  print('-END_DATE_TIME, -MAGNITUDE_TYPE, -TOR_LENGTH, -TOR_WIDTH, -TOR_OTHER_WFO, -TOR_OTHER_CZ_FIPS,')
  print('-TOR_OTHER_CZ_NAME, -BEGIN_RANGE, -BEGIN_AZIMUTH, -BEGIN_LOCATION, -END_RANGE,	-END_AZIMUTH,')
  print('-END_LOCATION, -EPISODE_NARRATIVE, -EVENT_NARRATIVE)')
  print('```\n')
  

  
#list of years for rbind
for i in range(60):
  year = i + 1950
  print('StormEvents_', year, ',',sep = '')
