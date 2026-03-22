#!/usr/bin/env bash
#
# Patch LM Studio to support SmolVLM/SmolVLM2 models.
#
# LM Studio's bundled MLX runtime is missing the `num2words` package
# that SmolVLM's processor requires. This script copies the package
# from the system Python into LM Studio's site-packages.
#
# Without this patch, loading any SmolVLM model fails with:
#   ImportError: Package `num2words` is required to run SmolVLM processor.
#
# Usage:
#   ./scripts/patch-lmstudio-smolvlm.sh
#
# Prerequisites:
#   pip3 install num2words
#
# Note: This patch may need to be re-applied after LM Studio updates,
# as updates can replace the bundled Python environment.

set -euo pipefail

# LM Studio's bundled MLX Python site-packages
LMSTUDIO_SITE="$HOME/.lmstudio/extensions/backends/vendor/_amphibian/app-mlx-generate-mac14-arm64@19/lib/python3.11/site-packages"

if [[ ! -d "$LMSTUDIO_SITE" ]]; then
    echo "Error: LM Studio MLX runtime not found at:"
    echo "  $LMSTUDIO_SITE"
    echo ""
    echo "Make sure LM Studio is installed and has loaded an MLX model at least once."
    exit 1
fi

# Check if already patched
if [[ -d "$LMSTUDIO_SITE/num2words" ]]; then
    echo "Already patched: num2words is present in LM Studio's site-packages."
    exit 0
fi

# Ensure num2words is installed in system Python
if ! python3 -c "import num2words" 2>/dev/null; then
    echo "Installing num2words in system Python..."
    pip3 install --break-system-packages num2words 2>/dev/null \
        || pip3 install num2words
fi

# Copy num2words and its dependency (docopt) into LM Studio
NUM2WORDS_PATH=$(python3 -c "import num2words; print(num2words.__path__[0])")
DOCOPT_PATH=$(python3 -c "import docopt; print(docopt.__file__)")

echo "Copying num2words from: $NUM2WORDS_PATH"
echo "Copying docopt from:    $DOCOPT_PATH"
echo "Target:                 $LMSTUDIO_SITE"

cp -r "$NUM2WORDS_PATH" "$LMSTUDIO_SITE/"
cp "$DOCOPT_PATH" "$LMSTUDIO_SITE/"

echo ""
echo "Done. SmolVLM models should now load in LM Studio."
echo "If LM Studio is running, restart it for the change to take effect."
