echo "Downloading 911 response data"
curl -# "https://data.seattle.gov/api/views/3k2p-39jp/rows.csv?accessType=DOWNLOAD" >> 911-response.csv
echo "Downloading police reports"
curl -# "https://data.seattle.gov/api/views/7ais-f98f/rows.csv?accessType=DOWNLOAD" >> police-report.csv
#echo "Downloading crime map"
#curl -# "https://data.seattle.gov/api/views/x3ji-ckps/rows.csv?accessType=DOWNLOAD" >> crime-map.csv