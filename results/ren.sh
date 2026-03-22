#!/usr/bin/env bash
# rename_omlx_to_vmlx.sh
# Renames all files containing 'omlx' in their name to 'vmlx'
# within the jangq-ai-qwen directory (dry-run by default)

set -euo pipefail

TARGET_DIR="${1:-./jangq-ai-qwen}"
DRY_RUN="${2:-true}"

if [[ ! -d "$TARGET_DIR" ]]; then
  echo "ERROR: Directory '$TARGET_DIR' not found." >&2
  exit 1
fi

echo "Scanning: $TARGET_DIR"
echo "Dry run:  $DRY_RUN"
echo "---"

RENAMED=0
SKIPPED=0

while IFS= read -r -d '' file; do
  dir=$(dirname "$file")
  base=$(basename "$file")

  new_base="${base//omlx/vmlx}"
  new_file="$dir/$new_base"

  if [[ -e "$new_file" ]]; then
    echo "SKIP (target exists): $file -> $new_file"
    ((SKIPPED++)) || true
    continue
  fi

  if [[ "$DRY_RUN" == "true" ]]; then
    echo "DRY RUN: mv '$file' -> '$new_file'"
  else
    mv "$file" "$new_file"
    echo "RENAMED: '$file' -> '$new_file'"
  fi
  ((RENAMED++)) || true

done < <(find "$TARGET_DIR" -type f -name "*omlx*" -print0)

echo "---"
echo "Files renamed (or would rename): $RENAMED"
echo "Files skipped (target exists):   $SKIPPED"

if [[ "$DRY_RUN" == "true" ]]; then
  echo ""
  echo "Run with DRY_RUN=false to apply changes:"
  echo "  $0 \"$TARGET_DIR\" false"
fi
