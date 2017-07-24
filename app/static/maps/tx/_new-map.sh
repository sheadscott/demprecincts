#!/bin/bash
COUNTY=$1

# Copy the geojson map file to the app directory
if [ -e "/Users/Shea/Sites/vogb/GIS/county-voting-precincts/tx/${COUNTY}.geojson" ]
then
  cp /Users/Shea/Sites/vogb/GIS/county-voting-precincts/tx/${COUNTY}.geojson ./${COUNTY}.geojson
else
  echo "Files not found or an argument wasn't given."
  exit 1
fi

# Convert geojson to topojson
geo2topo county=${COUNTY}.geojson > ${COUNTY}.json

# Delete geojson file
rm ${COUNTY}.geojson

# Load variables from text file
source ./_add-county.txt 

# Add variables to database
sqlite3 /Users/Shea/Sites/demprecincts/app.db "INSERT INTO county (name, state, sheet_url, latitude, longitude) VALUES ('${NAME}',${STATE},'${SHEET_URL}',${LAT},${LONG})"
