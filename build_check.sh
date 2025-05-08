#!/bin/bash
# Build verification script for Render

echo "=== ENVIRONMENT INFO ==="
pwd
echo "Current directory: $(pwd)"
ls -la

echo "=== FRONTEND DIRECTORY STRUCTURE ==="
cd frontend || { echo "Frontend directory not found!"; exit 1; }
ls -la

echo "=== RUNNING BUILD ==="
npm ci
npm run build

echo "=== CHECKING BUILD RESULT ==="
ls -la
if [ -d "dist" ]; then
  echo "dist directory exists"
  ls -la dist
  echo "BUILD SUCCESSFUL"
else
  echo "dist directory does not exist! Build failed."
  exit 1
fi