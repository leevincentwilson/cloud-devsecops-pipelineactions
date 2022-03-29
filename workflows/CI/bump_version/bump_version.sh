#!/bin/bash

# Works with a file called VERSION in the current directory,
# the contents of which should be a semantic version number
# such as "1.2.3"

# this script will display the current version, automatically
# suggest a "minor" version update, and ask for input to use
# the suggestion, or use a newly entered value.

set -e

VERSION_FILE=$1

suggest_version() {
  local CURRENT_VERSION
  local CURRENT_MAJOR
  local CURRENT_MINOR
  local CURRENT_PATCH
  CURRENT_VERSION=`cat ${VERSION_FILE}`
  BASE_LIST=(`echo $CURRENT_VERSION | tr '.' ' '`)
  #CURRENT_MAJOR=$(echo "$CURRENT_VERSION" | cut -d. -f1)
  #CURRENT_MINOR=$(echo "$CURRENT_VERSION" | cut -d. -f2)
  #CURRENT_PATCH=$(echo "$CURRENT_VERSION" | cut -d. -f3)
  CURRENT_MAJOR=${BASE_LIST[0]}
  CURRENT_MINOR=${BASE_LIST[1]}
  CURRENT_PATCH=${BASE_LIST[2]}

  if [ "$CURRENT_PATCH" = "" ] || [ "$CURRENT_PATCH" = "0" ]; then
	  SUGGESTED_PATCH=0
          SUGGESTED_MINOR=$((CURRENT_MINOR + 1))
  else
	  SUGGESTED_PATCH=$((CURRENT_PATCH + 1))
          SUGGESTED_MINOR=$((CURRENT_MINOR + 0))
  fi	  

  echo "$CURRENT_MAJOR.$SUGGESTED_MINOR.$SUGGESTED_PATCH"
}

update_version() {
  NEW_VERSION=$1; shift
  
  echo "$NEW_VERSION" > $VERSION_FILE
  git add $VERSION_FILE
}

push_tags() {
  NEW_VERSION=$1; shift

  echo "Pushing new version to the origin"
  git commit -m "Bump version to ${NEW_VERSION}."
  #git tag -a -m "Tag version ${NEW_VERSION}." "v$NEW_VERSION"
  git push origin
  #git push origin --tags
}



if [ -f $VERSION_FILE ]; then
  SUGGESTED_VERSION=$(suggest_version)

  echo "Current version: $(cat ${VERSION_FILE})"
  echo "next version: $SUGGESTED_VERSION"
  NEW_VERSION=""

  if [ "$NEW_VERSION" = "" ]; then NEW_VERSION=$SUGGESTED_VERSION; fi
  echo "Will set new version to be $NEW_VERSION"
  update_version "$NEW_VERSION"
  push_tags "$NEW_VERSION"
else
  echo "Could not find a $VERSION_FILE file."
fi
