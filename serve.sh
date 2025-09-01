#!/bin/bash

# Check if Pagefind is installed
if ! python3 -c "import pagefind" 2>/dev/null; then
    echo "Pagefind is not installed. Please install it first:"
    echo "pip3 install \"pagefind[extended]\""
    exit 1
fi

echo "Cleaning old Pagefind index..."
rm -rf _site/_pagefind

echo "Building Jekyll site and indexing with Pagefind..."
bundle exec jekyll build --drafts --future --incremental && python3 -m pagefind

echo "Starting Jekyll server..."
bundle exec jekyll serve --drafts --incremental --verbose --profile --future --skip-initial-build
