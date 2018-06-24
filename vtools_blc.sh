#!/bin/sh
# Usage: bash vtools_blc.sh 

# Set a default if no comment is given
COMMENT="Automatic commit from vtools_blc.sh"

# variables
HERE=$(pwd)
MYWEB="vatlab.github.io/vat-docs/"
URL="urls.txt"
RESULT="blc_result.txt"

cd ~/vat-docs

# get all paths
wget --spider --force-html -r -l1 $MYWEB 2>&1 | grep 'Saving to:'
find $MYWEB > $URL

# delete DS_Store, add prefix, //to/
sed -i '' -e '/DS_Store/d' $URL 
sed -i '' -e "s/\/\//\//" $URL  
sed -i '' -e "s/^/http:\/\//" $URL  
sed -i '' -e "s/$/\//" $URL  
sed -i '' -e '1s/vat-docs\/\//vat-docs\//' $URL

# blc
k=1
while read line;do blc $line; ((k++)); done < $URL > $RESULT

git add $RESULT 
git commit -m "$COMMENT"
git push 

# Go back
cd $HERE

