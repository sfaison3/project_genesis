#!/bin/bash
# Custom build script for Render deployment

set -e  # Exit on any error

echo "=== ENVIRONMENT INFO ==="
echo "Current directory: $(pwd)"
ls -la

echo "=== CREATING DIST DIRECTORIES ==="
mkdir -p dist
mkdir -p ./dist
mkdir -p ../dist
mkdir -p /opt/render/project/src/dist

echo "=== BUILDING FRONTEND ==="
cd frontend
npm ci
npm run build
echo "Frontend build output:"
ls -la dist/

echo "=== COPYING BUILD FILES TO MULTIPLE POSSIBLE LOCATIONS ==="
# Copy to root dist
cp -r dist/* ../dist/
# Copy to current directory dist
cp -r dist/* ../dist/
# Copy to Render's typical location
cp -r dist/* /opt/render/project/src/dist/ || echo "Couldn't copy to Render path - this is normal locally"

echo "=== VERIFYING ROOT DIST DIRECTORY ==="
cd ..
ls -la dist/

echo "=== ADDITIONAL FALLBACK - SYMLINK FRONTEND DIST ==="
ln -sf frontend/dist dist_link || echo "Symlink creation failed - this is optional"

echo "Build completed successfully!"