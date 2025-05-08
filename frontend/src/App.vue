<template>
  <div class="app-container">
    <div v-if="isLoading" class="loading-overlay">
      <div class="loading-spinner"></div>
      <p>Generating your educational music...</p>
    </div>
    
    <div class="app-content">
      <div class="left-panel">
        <div class="form-section">
          <h2>What do you want to learn?</h2>
          <div class="input-container">
            <input 
              v-model="learningTopic" 
              placeholder="I'm trying to understand this chart in Economics" 
              class="topic-input"
            />
          </div>
          
          <div class="upload-section">
            <p class="upload-label">upload for additional context (PDF, etc)</p>
            <FileUpload @file-selected="handleFileUpload">upload</FileUpload>
          </div>
          
          <div class="genre-section">
            <h3>Genre</h3>
            <div class="genre-buttons">
              <button 
                class="genre-button" 
                :class="{ 'active': selectedGenre === 'country' }"
                @click="selectGenre('country')"
              >
                Country
              </button>
              <button 
                class="genre-button" 
                :class="{ 'active': selectedGenre === 'hip_hop' }"
                @click="selectGenre('hip_hop')"
              >
                Hip hop
              </button>
              <button 
                class="genre-button" 
                :class="{ 'active': selectedGenre === 'pop' }"
                @click="selectGenre('pop')"
              >
                Pop
              </button>
              <button 
                class="genre-button"
                @click="showMoreGenres"
              >
                More
              </button>
            </div>
          </div>
          
          <button class="compose-button" @click="processInput">Compose</button>
        </div>
      </div>
      
      <div class="right-panel">
        <div class="output-section">
          <div class="output-header">
            <div class="thumbnail">
              <div class="placeholder-thumbnail">
                image for thumbnail of video
              </div>
            </div>
            
            <div class="song-info">
              <h3 class="song-info-title">the why</h3>
              <p>Summary of results</p>
            </div>
          </div>
          
          <h3 class="song-title">{{ songTitle || 'Song title' }}</h3>
          
          <div class="video-player">
            <template v-if="videoUrl">
              <video controls>
                <source :src="videoUrl" type="video/mp4">
                Your browser does not support the video tag.
              </video>
            </template>
            <template v-else-if="audioUrl">
              <div class="audio-container">
                <div class="play-button-overlay" @click="toggleAudio">
                  <span class="play-icon">{{ isAudioPlaying ? '❚❚' : '▶' }}</span>
                  <span class="play-text">{{ isAudioPlaying ? 'Pause' : 'Play' }}</span>
                </div>
                <audio ref="audioPlayer" :src="audioUrl" @ended="audioEnded" class="hidden-audio"></audio>
                <div class="audio-placeholder">
                  {{ isAudioPlaying ? 'Now playing...' : 'Music track available' }}
                </div>
              </div>
            </template>
            <template v-else>
              <div class="play-button-overlay">
                <span class="play-icon">▶</span>
                <span class="play-text">play button</span>
              </div>
              <div class="video-placeholder">
                music video
              </div>
            </template>
          </div>
          
          <div class="lyrics-section">
            <h3>Lyrics</h3>
            <p v-if="lyricsText" class="lyrics-content">{{ lyricsText }}</p>
            <p v-else-if="output && outputType === 'text'" class="lyrics-content">{{ output }}</p>
            <p v-else class="lyrics-content placeholder-text">Your lyrics will appear here</p>
          </div>
          
          <div class="action-buttons">
            <button class="action-button" @click="downloadContent" :disabled="!audioUrl && !videoUrl">Download</button>
            <button class="action-button" @click="shareContent" :disabled="!audioUrl && !videoUrl">Share</button>
            <button class="action-button action-button-wide" @click="generateVideo" :disabled="!audioUrl || videoUrl">Turn into music video</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- API Status indicator (keep this for development) -->
  <div class="api-status-indicator">
    <span>API Status: </span>
    <span v-if="apiStatus === null">Checking...</span>
    <span v-else-if="apiStatus === 'ok'" class="status-ok">Connected</span>
    <span v-else class="status-error">Disconnected</span>
  </div>
</template>

<script>
import config from './config'
import FileUpload from './components/FileUpload.vue'

export default {
  components: {
    FileUpload
  },
  data() {
    return {
      userInput: '',
      learningTopic: '',
      selectedModel: 'beatoven', // Default to music generation
      selectedGenre: 'hip_hop',  // Default to hip hop
      selectedDuration: 60,
      output: null,
      outputType: 'text',
      isLoading: false,
      apiUrl: config.apiUrl,
      apiStatus: null,
      genres: [],
      songTitle: '',
      videoUrl: '',
      audioUrl: '',
      lyricsText: '',
      uploadedFile: null,
      uploadedFileName: '',
      isAudioPlaying: false
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
    selectGenre(genre) {
      this.selectedGenre = genre
    },
    
    showMoreGenres() {
      // This would show a modal or expanded list of genres
      alert('Additional genres coming soon!')
    },
    
    handleFileUpload(file) {
      this.uploadedFile = file
      this.uploadedFileName = file.name
      console.log('File uploaded:', file.name)
      
      // In a real implementation, we might want to:
      // 1. Show a preview of the file
      // 2. Read text files to extract context
      // 3. Send the file to the backend for processing
      
      // For simplicity, we'll just store the file and alert the user
      alert(`File "${file.name}" selected for additional context`)
    },
    
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
          { id: 'classical', name: 'Classical' },
          { id: 'hip_hop', name: 'Hip Hop' },
          { id: 'country', name: 'Country' }
        ]
      }
    },
    
    async processInput() {
      if (!this.learningTopic.trim()) {
        alert('Please enter what you want to learn about!')
        return
      }
      
      this.isLoading = true
      try {
        // Automatically use learning topic as input if no specific user input
        if (!this.userInput.trim()) {
          this.userInput = `Create a song about ${this.learningTopic}`
        }
        
        // Use the API URL from environment variables
        const endpoint = `${this.apiUrl}/generate`.replace('//', '/')
        console.log('Making request to:', endpoint)
        
        // For file uploads, we need to use FormData instead of plain JSON
        if (this.uploadedFile) {
          const formData = new FormData()
          formData.append('file', this.uploadedFile)
          formData.append('input', this.userInput)
          formData.append('model', 'beatoven') 
          formData.append('learning_topic', this.learningTopic)
          formData.append('genre', this.selectedGenre)
          formData.append('duration', this.selectedDuration)
          
          console.log('Sending FormData with file:', this.uploadedFileName)
          
          const response = await fetch(endpoint, {
            method: 'POST',
            body: formData
          })
          
          if (!response.ok) {
            const errorData = await response.json()
            throw new Error(errorData.detail || 'API request failed')
          }
          
          const data = await response.json()
          this.handleApiResponse(data)
          return
        }
        
        // Standard JSON request (no file upload)
        const requestBody = {
          input: this.userInput,
          model: 'beatoven', // Always use beatoven for music
          learning_topic: this.learningTopic,
          genre: this.selectedGenre,
          duration: this.selectedDuration
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
        this.handleApiResponse(data)
      } catch (error) {
        console.error('Error:', error)
        this.output = `Error processing request: ${error.message}`
        this.outputType = 'text'
      } finally {
        this.isLoading = false
      }
    },
    
    handleApiResponse(data) {
      // Handle different types of responses
      this.output = data.output
      this.outputType = data.type
      
      // If we get a music response, we would also have lyrics and a title
      if (data.type === 'music') {
        this.audioUrl = data.output
        this.songTitle = data.title || `Song about ${this.learningTopic}`
        this.lyricsText = data.lyrics || 'Lyrics not available for this song.'
        
        // In a real app, we'd also handle video URL if available
        this.videoUrl = data.video_url || ''
      }
    },
    
    toggleAudio() {
      if (!this.$refs.audioPlayer) return
      
      if (this.isAudioPlaying) {
        this.$refs.audioPlayer.pause()
      } else {
        this.$refs.audioPlayer.play()
      }
      
      this.isAudioPlaying = !this.isAudioPlaying
    },
    
    audioEnded() {
      this.isAudioPlaying = false
    },
    
    downloadContent() {
      if (this.audioUrl) {
        // Create an anchor element and trigger download
        const a = document.createElement('a')
        a.href = this.audioUrl
        a.download = `${this.songTitle || 'learning_song'}.mp3`
        document.body.appendChild(a)
        a.click()
        document.body.removeChild(a)
      } else if (this.videoUrl) {
        // Similar process for video
        const a = document.createElement('a')
        a.href = this.videoUrl
        a.download = `${this.songTitle || 'learning_video'}.mp4`
        document.body.appendChild(a)
        a.click()
        document.body.removeChild(a)
      }
    },
    
    shareContent() {
      // Use Web Share API if available
      if (navigator.share) {
        navigator.share({
          title: this.songTitle || 'Learning Song',
          text: 'Check out this educational song I created!',
          url: this.audioUrl || this.videoUrl
        })
        .catch(err => {
          console.error('Error sharing:', err)
          this.fallbackShare()
        })
      } else {
        this.fallbackShare()
      }
    },
    
    fallbackShare() {
      // Fallback for browsers without Web Share API
      const shareText = `${this.songTitle || 'Learning Song'}: ${this.audioUrl || this.videoUrl}`
      
      // Copy to clipboard
      navigator.clipboard.writeText(shareText)
        .then(() => alert('Link copied to clipboard!'))
        .catch(() => alert('Unable to copy to clipboard. The URL is: ' + (this.audioUrl || this.videoUrl)))
    },
    
    generateVideo() {
      if (!this.audioUrl) return
      
      this.isLoading = true
      
      // In a real implementation, we'd make an API call to generate a video
      // For this prototype, we'll simulate it with a timeout
      setTimeout(() => {
        alert('Video generation is not implemented in this prototype. In a production version, this would send the audio to a video generation service.')
        this.isLoading = false
      }, 1500)
    }
  }
}
</script>

<style>
/* Reset and base styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f0f0f0;
  color: #333;
}

.app-container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  background-color: #f0f0f0;
}

.app-content {
  display: flex;
  width: 100%;
  max-width: 1200px;
  min-height: 600px;
  background-color: #666;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

/* Left panel styles */
.left-panel {
  flex: 1;
  background-color: #666;
  color: white;
  padding: 30px;
}

.form-section {
  max-width: 500px;
  margin: 0 auto;
}

.form-section h2 {
  font-size: 24px;
  margin-bottom: 20px;
}

.input-container {
  margin-bottom: 20px;
}

.topic-input {
  width: 100%;
  padding: 12px 15px;
  font-size: 16px;
  border: none;
  border-radius: 10px;
  background-color: white;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.upload-section {
  margin: 30px 0;
  padding: 20px;
  border: 2px dashed white;
  border-radius: 15px;
  text-align: center;
}

.upload-label {
  margin-bottom: 15px;
}

.upload-button {
  background-color: #7c4dff;
  color: white;
  border: none;
  border-radius: 20px;
  padding: 8px 25px;
  font-size: 16px;
  cursor: pointer;
}

.genre-section {
  margin: 30px 0;
}

.genre-section h3 {
  margin-bottom: 15px;
  font-size: 20px;
}

.genre-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-bottom: 30px;
}

.genre-button {
  flex: 1 0 calc(33% - 15px);
  padding: 15px 10px;
  background-color: white;
  border: none;
  border-radius: 10px;
  font-size: 16px;
  cursor: pointer;
  min-width: 120px;
  color: #333;
}

.genre-button.active {
  background-color: #7c4dff;
  color: white;
}

.compose-button {
  width: 100%;
  padding: 15px;
  background-color: #7c4dff;
  color: white;
  border: none;
  border-radius: 10px;
  font-size: 18px;
  font-weight: bold;
  cursor: pointer;
  margin-top: 20px;
}

/* Right panel styles */
.right-panel {
  flex: 1;
  background-color: white;
  padding: 20px;
  overflow-y: auto;
}

.output-section {
  padding: 20px;
}

.output-header {
  display: flex;
  margin-bottom: 20px;
}

.thumbnail {
  width: 150px;
  height: 120px;
  margin-right: 15px;
}

.placeholder-thumbnail {
  width: 100%;
  height: 100%;
  background-color: #7c4dff;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 10px;
  border-radius: 10px;
}

.song-info {
  flex: 1;
  padding: 10px;
  border: 1px solid #eee;
  border-radius: 10px;
}

.song-info-title {
  margin-bottom: 10px;
}

.song-title {
  margin: 20px 0 15px 0;
}

.video-player {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
  background-color: #f4ecff;
  border-radius: 10px;
  margin-bottom: 20px;
  overflow: hidden;
}

.play-button-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  z-index: 2;
}

.play-icon {
  font-size: 48px;
  margin-bottom: 10px;
}

.video-placeholder, .audio-placeholder {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #666;
}

.audio-container {
  position: relative;
  width: 100%;
  height: 100%;
}

.hidden-audio {
  display: none;
}

.lyrics-section {
  border: 1px solid #eee;
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 20px;
  min-height: 150px;
}

.lyrics-content {
  margin-top: 10px;
  white-space: pre-line;
}

.placeholder-text {
  color: #999;
  font-style: italic;
}

.action-buttons {
  display: flex;
  justify-content: space-between;
  gap: 15px;
}

.action-button {
  flex: 1;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 10px;
  background-color: white;
  font-size: 16px;
  cursor: pointer;
}

.action-button-wide {
  flex: 2;
}

.action-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* API status indicator (hidden in production) */
.api-status-indicator {
  position: fixed;
  bottom: 10px;
  right: 10px;
  background-color: rgba(0, 0, 0, 0.7);
  color: white;
  padding: 5px 10px;
  border-radius: 5px;
  font-size: 12px;
  z-index: 1000;
}

.status-ok {
  color: #4caf50;
}

.status-error {
  color: #f44336;
}

/* Loading overlay */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  color: white;
}

.loading-spinner {
  width: 50px;
  height: 50px;
  border: 5px solid #f3f3f3;
  border-top: 5px solid #7c4dff;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Responsive adjustments */
@media (max-width: 900px) {
  .app-content {
    flex-direction: column;
  }
  
  .left-panel, .right-panel {
    width: 100%;
  }
  
  .genre-button {
    flex: 1 0 calc(50% - 10px);
  }
  
  .action-buttons {
    flex-wrap: wrap;
  }
  
  .action-button {
    flex: 1 0 calc(50% - 10px);
  }
  
  .action-button-wide {
    flex: 1 0 100%;
    order: -1;
    margin-bottom: 10px;
  }
}

@media (max-width: 600px) {
  .genre-button {
    flex: 1 0 100%;
  }
  
  .output-header {
    flex-direction: column;
  }
  
  .thumbnail {
    width: 100%;
    margin-right: 0;
    margin-bottom: 15px;
  }
}
</style>