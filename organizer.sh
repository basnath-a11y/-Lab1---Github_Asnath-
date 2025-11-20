#!/bin/bash

# 1. Create archive folder if not exists
if [ ! -d "archive" ]; then
    mkdir archive
fi

# 2. Find CSV files
csv_files=$(ls *.csv 2> /dev/null)

if [ -z "$csv_files" ]; then
    echo "No CSV files found."
    exit 0
fi

# 3. Loop through CSV files
for file in $csv_files; do
    timestamp=$(date +"%Y%m%d-%H%M%S")
    new_name="${file%.csv}-$timestamp.csv"

    echo "Archiving $file → archive/$new_name"

    # Log details and file content
    echo "----- ARCHIVE LOG -----" >> organizer.log
    echo "Original File: $file" >> organizer.log
    echo "New File: $new_name" >> organizer.log
    echo "Timestamp: $timestamp" >> organizer.log
    echo "Content:" >> organizer.log
    cat "$file" >> organizer.log
    echo "------------------------" >> organizer.log
    echo "" >> organizer.log

    # Move + rename
    mv "$file" "archive/$new_name"
done

echo "Archiving complete!"
