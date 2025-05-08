<template>
  <header>
    <h1>Genesis</h1>
    <h2>Multi-modal AI Orchestration Platform</h2>
  </header>
  
  <main>
    <div class="input-section">
      <h3>Input</h3>
      <textarea v-model="userInput" placeholder="Enter text, paste image URL, or describe video..."></textarea>
      <div class="button-row">
        <button @click="processInput">Generate</button>
        <select v-model="selectedModel">
          <option value="auto">Auto (MCP)</option>
          <option value="gpt-image-1">OpenAI gpt-image-1</option>
          <option value="veo2">Google veo2</option>
          <option value="gemini">Gemini</option>
          <option value="o4-mini">OpenAI o4-mini</option>
        </select>
      </div>
    </div>
    
    <div class="output-section">
      <h3>Output</h3>
      <div class="output-display">
        <p v-if="isLoading">Processing...</p>
        <div v-else-if="output" class="result">
          <div v-if="outputType === 'text'" class="text-output">{{ output }}</div>
          <img v-else-if="outputType === 'image'" :src="output" alt="Generated image" />
          <video v-else-if="outputType === 'video'" controls>
            <source :src="output" type="video/mp4">
            Your browser does not support the video tag.
          </video>
        </div>
        <p v-else class="placeholder">Results will appear here</p>
      </div>
    </div>
  </main>
  
  <footer>
    <p>Genesis - AI Orchestration Platform</p>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      userInput: '',
      selectedModel: 'auto',
      output: null,
      outputType: 'text',
      isLoading: false
    }
  },
  methods: {
    async processInput() {
      this.isLoading = true
      try {
        const response = await fetch('/api/generate', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            input: this.userInput,
            model: this.selectedModel
          })
        })
        
        const data = await response.json()
        this.output = data.output
        this.outputType = data.type // 'text', 'image', or 'video'
      } catch (error) {
        console.error('Error:', error)
        this.output = 'Error processing request'
        this.outputType = 'text'
      } finally {
        this.isLoading = false
      }
    }
  }
}
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  color: #333;
}

header, footer {
  background-color: #2c3e50;
  color: white;
  text-align: center;
  padding: 1rem;
}

main {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

.input-section, .output-section {
  margin-bottom: 2rem;
}

textarea {
  width: 100%;
  height: 100px;
  padding: 0.5rem;
  margin-bottom: 1rem;
}

.button-row {
  display: flex;
  gap: 1rem;
}

button {
  padding: 0.5rem 1rem;
  background-color: #3498db;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #2980b9;
}

select {
  padding: 0.5rem;
}

.output-display {
  min-height: 200px;
  border: 1px solid #ddd;
  padding: 1rem;
}

.placeholder {
  color: #999;
}

img, video {
  max-width: 100%;
}
</style>