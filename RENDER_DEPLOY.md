# Render Deployment Instructions

If you're experiencing issues with the render.yaml configuration, here are direct instructions for deploying via the Render Dashboard:

## Deploy as a Static Site

1. Log in to your Render Dashboard
2. Click "New" > "Static Site"
3. Connect your repository (GitHub/GitLab)
4. Configure with these settings:

   - **Name**: genesis (or your preferred name)
   - **Build Command**: 
   ```
   cd frontend && npm ci && npm run build
   ```
   - **Publish Directory**: 
   ```
   frontend/dist
   ```
   - **Branch**: main (or your default branch)
   - **Environment Variables**: Add if needed (like `VITE_API_URL`)

5. Create a file called `frontend/_redirects` with the content:
   ```
   /* /index.html 200
   ```
   
   This handles client-side routing in a single-page application.

## Troubleshooting Common Issues

1. **Publish directory not found**:
   - Ensure your build process is correctly generating the `dist` folder in the specified path
   - Check build logs for errors
   - Verify package.json has the correct build script

2. **Build errors**:
   - Look for dependency issues in the build logs
   - Check for Node.js version requirements
   - Consider adding a `.node-version` file to specify the Node version

3. **Routing issues**:
   - Add the _redirects file as described above
   - Configure route rewrites in the Render dashboard
   
4. **Alternative Direct Build Command**:
   If you continue to have issues, try this comprehensive build command:
   ```
   cd frontend && 
   npm ci && 
   npm run build && 
   cd .. && 
   mkdir -p dist && 
   cp -r frontend/dist/* dist/
   ```
   
   Then use `dist` as the publish directory.