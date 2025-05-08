<template>
  <header>
    <h1>Genesis Music Learning App</h1>
    <h2>Generate custom songs to make learning fun and memorable</h2>
    <div class="api-status">
      <span>API Status: </span>
      <span v-if="apiStatus === null">Checking...</span>
      <span v-else-if="apiStatus === 'ok'" class="status-ok">Connected</span>
      <span v-else class="status-error">Disconnected</span>
    </div>
  </header>
  
  <main>
    <div class="input-section">
      <h3>Create a Learning Song</h3>
      <div class="form-group">
        <label for="topic-input">What are you learning about?</label>
        <input id="topic-input" v-model="learningTopic" placeholder="Enter topic (e.g., Photosynthesis, World War II, Calculus...)" />
      </div>
      
      <div class="form-group">
        <label for="song-prompt">What should the song explain or teach?</label>
        <textarea id="song-prompt" v-model="userInput" placeholder="Describe what you want to learn through music... For example: 'Create a song explaining how photosynthesis works in plants'"></textarea>
      </div>
      
      <div class="form-options">
        <div class="form-group">
          <label for="model-select">Generation Method</label>
          <select id="model-select" v-model="selectedModel">
            <option value="auto">Auto (MCP)</option>
            <option value="beatoven">Music Only</option>
            <option value="o4-mini">Lyrics Only</option>
            <option value="gpt-image-1">Image</option>
            <option value="veo2">Video</option>
          </select>
        </div>
        
        <div class="form-group" v-if="selectedModel === 'auto' || selectedModel === 'beatoven'">
          <label for="genre-select">Music Genre</label>
          <select id="genre-select" v-model="selectedGenre">
            <option value="pop">Pop</option>
            <option value="rock">Rock</option>
            <option value="jazz">Jazz</option>
            <option value="classical">Classical</option>
            <option value="electronic">Electronic</option>
            <option value="hip_hop">Hip Hop</option>
            <option value="country">Country</option>
            <option value="folk">Folk</option>
          </select>
        </div>
        
        <div class="form-group" v-if="selectedModel === 'auto' || selectedModel === 'beatoven'">
          <label for="duration-select">Song Duration</label>
          <select id="duration-select" v-model="selectedDuration">
            <option :value="30">30 seconds</option>
            <option :value="60">1 minute</option>
            <option :value="120">2 minutes</option>
            <option :value="180">3 minutes</option>
          </select>
        </div>
      </div>
      
      <button class="generate-button" @click="processInput">Generate Learning Content</button>
    </div>
    
    <div class="output-section">
      <h3>Your Learning Content</h3>
      <div class="output-display">
        <p v-if="isLoading">Creating your personalized learning content...</p>
        <div v-else-if="output" class="result">
          <div v-if="outputType === 'text'" class="text-output">{{ output }}</div>
          <img v-else-if="outputType === 'image'" :src="output" alt="Generated image" />
          <video v-else-if="outputType === 'video'" controls>
            <source :src="output" type="video/mp4">
            Your browser does not support the video tag.
          </video>
          <div v-else-if="outputType === 'music'" class="music-output">
            <h4>Your Learning Song</h4>
            <audio controls>
              <source :src="output" type="audio/mpeg">
              Your browser does not support the audio tag.
            </audio>
          </div>
        </div>
        <p v-else class="placeholder">Your personalized learning content will appear here</p>
      </div>
    </div>
  </main>
  
  <footer>
    <p>Genesis Music Learning App - Making education fun and memorable</p>
  </footer>
</template>

<script>
import config from './config'

export default {
  data() {
    return {
      userInput: '',
      learningTopic: '',
      selectedModel: 'auto',
      selectedGenre: 'pop',
      selectedDuration: 60,
      output: null,
      outputType: 'text',
      isLoading: false,
      apiUrl: config.apiUrl,
      apiStatus: null,
      genres: []
    }
  },
  mounted() {
    console.log('API URL:', this.apiUrl)
    this.checkApiHealth()
    // Check API health every 30 seconds
    setInterval(this.checkApiHealth, 30000)
    
    // Load available music genres
    this.loadMusicGenres()
  },
  methods: {
    async checkApiHealth() {
      try {
        const endpoint = `${this.apiUrl}/health`.replace('//', '/')
        console.log('Checking API health at:', endpoint)
        
        const response = await fetch(endpoint)
        if (!response.ok) {
          throw new Error('API health check failed')
        }
        
        const data = await response.json()
        this.apiStatus = data.status
        console.log('API Status:', this.apiStatus)
      } catch (error) {
        console.error('Health check error:', error)
        this.apiStatus = 'error'
      }
    },
    
    async loadMusicGenres() {
      try {
        const endpoint = `${this.apiUrl}/music/genres`.replace('//', '/')
        console.log('Loading music genres from:', endpoint)
        
        const response = await fetch(endpoint)
        if (!response.ok) {
          throw new Error('Failed to load music genres')
        }
        
        this.genres = await response.json()
        console.log('Available genres:', this.genres)
      } catch (error) {
        console.error('Error loading genres:', error)
        // Use default genres if API call fails
        this.genres = [
          { id: 'pop', name: 'Pop' },
          { id: 'rock', name: 'Rock' },
          { id: 'jazz', name: 'Jazz' },
          { id: 'classical', name: 'Classical' }
        ]
      }
    },
    
    async processInput() {
      if (!this.userInput.trim()) {
        alert('Please enter what you want to learn about!')
        return
      }
      
      this.isLoading = true
      try {
        // Use the API URL from environment variables
        const endpoint = `${this.apiUrl}/generate`.replace('//', '/')
        console.log('Making request to:', endpoint)
        
        const requestBody = {
          input: this.userInput,
          model: this.selectedModel,
          learning_topic: this.learningTopic
        }
        
        // Add music-specific parameters if needed
        if (this.selectedModel === 'beatoven' || this.selectedModel === 'auto') {
          requestBody.genre = this.selectedGenre
          requestBody.duration = this.selectedDuration
        }
        
        console.log('Request payload:', requestBody)
        
        const response = await fetch(endpoint, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(requestBody)
        })
        
        if (!response.ok) {
          const errorData = await response.json()
          throw new Error(errorData.detail || 'API request failed')
        }
        
        const data = await response.json()
        this.output = data.output
        this.outputType = data.type // 'text', 'image', 'video', or 'music'
      } catch (error) {
        console.error('Error:', error)
        this.output = `Error processing request: ${error.message}`
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
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 0;
  padding: 0;
  color: #333;
  background-color: #f9f9f9;
}

header, footer {
  background-color: #5d4194;
  color: white;
  text-align: center;
  padding: 1.5rem;
}

header h1 {
  margin: 0;
  font-size: 2.2rem;
}

header h2 {
  font-weight: 400;
  margin: 0.5rem 0 0;
  font-size: 1.3rem;
  opacity: 0.9;
}

main {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
}

.input-section, .output-section {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  padding: 2rem;
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
  color: #444;
}

input[type="text"], 
input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  box-sizing: border-box;
}

textarea {
  width: 100%;
  height: 120px;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  box-sizing: border-box;
  resize: vertical;
}

.form-options {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.generate-button {
  display: block;
  width: 100%;
  padding: 1rem;
  background-color: #5d4194;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1.1rem;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.2s;
}

.generate-button:hover {
  background-color: #4c3575;
}

select {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
  background-color: white;
  cursor: pointer;
}

.output-display {
  min-height: 200px;
  border: 1px solid #ddd;
  background-color: white;
  border-radius: 4px;
  padding: 1.5rem;
}

.placeholder {
  color: #999;
  text-align: center;
  font-style: italic;
}

img, video {
  max-width: 100%;
  border-radius: 4px;
  display: block;
  margin: 0 auto;
}

audio {
  width: 100%;
  margin-top: 1rem;
}

.api-status {
  margin-top: 1rem;
  font-size: 0.9rem;
}

.status-ok {
  color: #3adb76;
  font-weight: bold;
}

.status-error {
  color: #ec5840;
  font-weight: bold;
}

.text-output {
  white-space: pre-wrap;
  line-height: 1.6;
}

.music-output {
  padding: 1.5rem;
  background-color: #f5f0ff;
  border-radius: 4px;
  text-align: center;
}

.music-output h4 {
  margin-top: 0;
  color: #5d4194;
  font-size: 1.2rem;
}

@media (max-width: 768px) {
  .form-options {
    grid-template-columns: 1fr;
  }
  
  main {
    padding: 1rem;
  }
  
  .input-section, .output-section {
    padding: 1.5rem;
  }
}
</style>