#!/bin/bash

REQUIRED_PAGEFIND_VERSION="1.5.2"
PAGEFIND_VERSION=$(python3 -m pagefind --version 2>/dev/null | awk '{print $2}')

# Check if the Pagefind CLI can generate the component assets used by nav search.
if [ "$PAGEFIND_VERSION" != "$REQUIRED_PAGEFIND_VERSION" ]; then
    echo "Pagefind $REQUIRED_PAGEFIND_VERSION is required. Please install it first:"
    echo "pip3 install \"pagefind[extended]==$REQUIRED_PAGEFIND_VERSION\""
    exit 1
fi

echo "Cleaning old Pagefind index..."
rm -rf _site/_pagefind

echo "Building Jekyll site and indexing with Pagefind..."
bundle exec jekyll build --drafts --future --incremental && python3 -m pagefind

echo "Starting Jekyll server..."
bundle exec jekyll serve --drafts --incremental --verbose --profile --future --skip-initial-build
