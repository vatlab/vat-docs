#!/bin/sh

MYWEB="vatlab.github.io/vat-docs/"
HERE=$(pwd)

# Download all the website
wget -k -r "https://${MYWEB}" # -k converts links

# Remove index.html from converted links
for f in ${MYWEB}/index.html ${MYWEB}/*/index.html; do
  sed -i -e "s/index.html//g" $f
  rm -f $f-e
done

# Here is my repository
REPDIR=${1-${HOME}/reps/myweb}

echo $REPDIR

cd $REPDIR
