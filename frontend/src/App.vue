<template>
  <div>
    <header class="header">
      <div class="logo-container">
        <img src="./assets/asu-logo.svg" alt="ASU Logo" class="asu-logo" />
        <h1 class="site-title">Study Music</h1>
      </div>
      <button class="login-button">Login / Sign up</button>
    </header>

    <main class="main-content">
      <div class="hero-section">
        <h1 class="hero-title">Study Music</h1>
        <p class="hero-tagline">Tagline</p>
      </div>

      <div class="how-it-works">
        <h2 class="section-title">How it works</h2>
        <div class="steps-container">
          <div class="step">
            <h3>Compose</h3>
            <p>Boom! Your custom song is in the works. Want to tweak the lyrics or add a fun fact? Remix it 'til it's just right.</p>
          </div>
          <div class="step">
            <h3>Prelude</h3>
            <p>What are you learning? Drop your topic, pick a vibe (aka genre), and give us the scoop—we'll turn it into a jam.</p>
          </div>
          <div class="step">
            <h3>Listen</h3>
            <p>Hit play and vibe out to your learning anthem. Download it, share it, or turn it into a music video masterpiece!</p>
          </div>
        </div>
      </div>

      <div class="create-section">
        <div class="input-section">
          <div class="learning-input">
            <label>What are you learning about?</label>
            <input 
              type="text" 
              placeholder='"What is string theory?" or "Who was Gandhi?"' 
              v-model="learningTopic"
            />
          </div>

          <div class="file-upload-section">
            <p>Or drag and drop a file (PDF, JPEG, etc)</p>
            <FileUpload 
              @file-selected="handleFileUpload" 
              ref="fileUpload"
            >Browse files</FileUpload>
            <p v-if="uploadedFile" class="file-feedback">
              <span class="file-success">✓</span> File ready for processing
            </p>
          </div>

          <div class="genre-section">
            <label>Genre</label>
            <div class="genre-search">
              <input type="text" placeholder='"I like Taylor Swift" or "Kendrick Lamar"' v-model="genreInput" />
            </div>
            <div class="genre-buttons">
              <button 
                v-for="genre in displayedGenres.slice(0, 12)" 
                :key="genre.id" 
                :class="['genre-btn', {'active': selectedGenre === genre.id}]" 
                @click="selectGenre(genre.id)"
              >
                {{ genre.name }}
              </button>
              <button 
                v-if="displayedGenres.length > 12"
                class="genre-btn more-btn"
                @click="showMoreGenres = !showMoreGenres"
              >
                {{ showMoreGenres ? 'Less' : 'More' }}
              </button>
            </div>
            
            <div v-if="showMoreGenres" class="genre-buttons additional-genres">
              <button 
                v-for="genre in displayedGenres.slice(12)" 
                :key="genre.id" 
                :class="['genre-btn', {'active': selectedGenre === genre.id}]" 
                @click="selectGenre(genre.id)"
              >
                {{ genre.name }}
              </button>
            </div>
          </div>

          <button class="compose-btn" @click="generateMusic">Compose</button>
        </div>

        <div class="output-section">
          <div class="song-recommendation">
            <div class="song-controls">
              <button class="control-btn"><i class="icon-shuffle"></i></button>
              <button 
                class="control-btn play-btn"
                @click="togglePlayback"
              >
                <i :class="isPlaying ? 'icon-pause' : 'icon-play'"></i>
              </button>
            </div>
            <div class="song-info">
              <div class="song-title-section">
                <h4>{{ songTitle || 'Song Title' }}</h4>
                <span class="duration">{{ formattedDuration }}</span>
              </div>
              <p class="song-description">{{ songDescription }}</p>
            </div>
            <div class="album-art">
              <img :src="albumArt" alt="Album art" class="album-image" />
            </div>
          </div>

          <div class="lyrics-section">
            <div class="lyrics-header">
              <h3>Lyrics</h3>
              <button 
                class="expand-btn"
                @click="lyricsExpanded = !lyricsExpanded"
              >
                <i :class="lyricsExpanded ? 'icon-collapse' : 'icon-expand'"></i>
              </button>
            </div>
            <div 
              class="lyrics-content"
              :class="{ 'lyrics-expanded': lyricsExpanded }"
            >
              <p v-if="lyrics">{{ lyrics }}</p>
              <p v-else class="placeholder-text">Lyrics will appear here after generating music</p>
            </div>
          </div>
          
          <audio 
            ref="audioPlayer" 
            :src="audioUrl" 
            @timeupdate="updateProgress" 
            @loadedmetadata="onAudioLoaded"
            @ended="onAudioEnded"
            @error="onAudioError"
            style="display: none;"
          ></audio>
          
          <div class="player-controls">
            <div class="control-buttons">
              <button class="control-btn" aria-label="Shuffle"><i class="icon-shuffle"></i></button>
              <button class="control-btn" @click="skipBackward" aria-label="Previous"><i class="icon-prev"></i></button>
              <button 
                class="control-btn play-btn"
                @click="togglePlayback"
                aria-label="Play or Pause"
              >
                <i :class="isPlaying ? 'icon-pause' : 'icon-play'"></i>
              </button>
              <button class="control-btn" @click="skipForward" aria-label="Next"><i class="icon-next"></i></button>
              <button 
                class="control-btn"
                :class="{ 'active': isLooping }"
                @click="toggleLoop"
                aria-label="Repeat"
              >
                <i class="icon-repeat"></i>
              </button>
            </div>
            <div class="progress-bar">
              <span class="current-time">{{ formattedCurrentTime }}</span>
              <div 
                class="progress-track"
                @click="seekAudio"
                ref="progressTrack"
              >
                <div 
                  class="progress-filled"
                  :style="{ width: `${progressPercentage}%` }"
                ></div>
              </div>
              <span class="total-time">{{ formattedDuration }}</span>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import FileUpload from './components/FileUpload.vue'
import config from './config'
import albumArtImage from './assets/album-art.svg'

export default {
  components: {
    FileUpload
  },
  data() {
    return {
      learningTopic: '',
      genreInput: '',
      selectedGenre: 'hip-hop',
      uploadedFile: null,
      apiUrl: config.apiUrl,
      apiStatus: null,
      isLoading: false,
      showMoreGenres: false,
      lyricsExpanded: false,
      // Song/music data
      songTitle: 'Song Title',
      songDescription: 'The why, and how this will benefit you',
      audioUrl: '',
      lyrics: 'Psst, I see dead people\n(Mustard on the beat, ho)\nAyy, Mustard on the beat, ho',
      isPlaying: false,
      audioDuration: 63, // in seconds
      currentAudioTime: 0, // in seconds
      isLooping: false,
      albumArt: albumArtImage,
      // Available genres
      genres: [
        { id: 'country', name: 'Country' },
        { id: 'pop', name: 'Pop' },
        { id: 'hip-hop', name: 'Hip-hop' },
        { id: 'rap', name: 'Rap' },
        { id: 'heavy-metal', name: 'Heavy metal' },
        { id: 'jazz', name: 'Jazz' },
        { id: 'folk', name: 'Folk' },
        { id: 'eletronic', name: 'Eletronic' },
        { id: 'blues', name: 'Blues' },
        { id: 'punk', name: 'Punk' },
        { id: 'disco', name: 'Disco' },
        { id: 'soul', name: 'Soul' },
        { id: 'rock', name: 'Rock' },
        { id: 'grunge', name: 'Grunge' },
        { id: 'opera', name: 'Opera' },
        { id: 'k-pop', name: 'K-pop' },
        { id: 'rock-and-roll', name: 'Rock and roll' },
      ]
    }
  },
  computed: {
    displayedGenres() {
      // Filter genres based on search input, or return all if no input
      if (this.genreInput.trim() === '') {
        return this.genres;
      }
      return this.genres.filter(genre => 
        genre.name.toLowerCase().includes(this.genreInput.toLowerCase())
      );
    },
    
    formattedCurrentTime() {
      return this.formatTime(this.currentAudioTime);
    },
    
    formattedDuration() {
      return this.formatTime(this.audioDuration);
    },
    
    progressPercentage() {
      if (this.audioDuration === 0) return 0;
      return (this.currentAudioTime / this.audioDuration) * 100;
    }
  },
  mounted() {
    console.log('API URL:', this.apiUrl)
    this.checkApiHealth()
    // Check API health every 30 seconds
    setInterval(this.checkApiHealth, 30000)
  },
  methods: {
    selectGenre(genreId) {
      this.selectedGenre = genreId
    },
    
    handleFileUpload(file) {
      this.uploadedFile = file
      if (file) {
        console.log('File uploaded:', file.name)
        
        // If the file is a text file, we could extract text content for context
        if (file.type === 'text/plain' || file.name.endsWith('.txt')) {
          const reader = new FileReader()
          reader.onload = (e) => {
            const text = e.target.result
            console.log('Extracted text from file:', text.substring(0, 100) + '...')
            // This text could be used to enhance the learning context
            // In a real app, we might set this text as additional context for the API
          }
          reader.readAsText(file)
        }
      } else {
        console.log('File upload cleared')
      }
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
    
    async generateMusic() {
      if (!this.learningTopic.trim()) {
        alert('Please enter what you want to learn about!')
        return
      }
      
      this.isLoading = true
      
      try {
        // Use the API URL from environment variables
        const endpoint = `${this.apiUrl}/generate`.replace('//', '/')
        console.log('Making request to:', endpoint)
        
        // For file uploads, we need to use FormData instead of plain JSON
        if (this.uploadedFile) {
          const formData = new FormData()
          formData.append('file', this.uploadedFile)
          formData.append('learning_topic', this.learningTopic)
          formData.append('genre', this.selectedGenre)
          formData.append('model', 'beatoven') 
          
          console.log('Sending FormData with file:', this.uploadedFile.name)
          
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
          learning_topic: this.learningTopic,
          genre: this.selectedGenre,
          model: 'beatoven' // Always use beatoven for music
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
        alert(`Error: ${error.message}`)
      } finally {
        this.isLoading = false
      }
    },
    
    handleApiResponse(data) {
      // Handle the music generation response
      if (data.type === 'music') {
        this.audioUrl = data.output
        this.songTitle = data.title || `Song about ${this.learningTopic}`
        this.lyrics = data.lyrics || 'Lyrics not available for this song.'
        this.songDescription = data.description || 'The why, and how this will benefit you'
        
        // If album art was generated
        if (data.album_art) {
          this.albumArt = data.album_art
        }
        
        // Start playback when ready
        this.$nextTick(() => {
          const player = this.$refs.audioPlayer
          if (player) {
            player.load()
            
            // Auto-play after a short delay to ensure loading
            setTimeout(() => {
              this.isPlaying = true
              player.play().catch(err => {
                console.error('Error auto-playing:', err)
                this.isPlaying = false
              })
            }, 500)
          }
        })
      }
    },
    
    togglePlayback() {
      if (!this.audioUrl) {
        console.log('No audio source available')
        return
      }
      
      this.isPlaying = !this.isPlaying
      
      const player = this.$refs.audioPlayer
      if (player) {
        if (this.isPlaying) {
          player.play().catch(err => {
            console.error('Error playing audio:', err)
            this.isPlaying = false
          })
        } else {
          player.pause()
        }
      }
    },
    
    formatTime(seconds) {
      if (!seconds || isNaN(seconds)) return '0:00'
      
      const mins = Math.floor(seconds / 60)
      const secs = Math.floor(seconds % 60)
      return `${mins}:${secs.toString().padStart(2, '0')}`
    },
    
    updateProgress() {
      const player = this.$refs.audioPlayer
      if (player) {
        this.currentAudioTime = player.currentTime
      }
    },
    
    onAudioLoaded() {
      const player = this.$refs.audioPlayer
      if (player) {
        this.audioDuration = player.duration
        console.log('Audio duration:', this.audioDuration)
      }
    },
    
    onAudioEnded() {
      if (this.isLooping) {
        this.$refs.audioPlayer.play()
      } else {
        this.isPlaying = false
        this.currentAudioTime = 0
      }
    },
    
    onAudioError(error) {
      console.error('Audio playback error:', error)
      this.isPlaying = false
    },
    
    seekAudio(event) {
      const player = this.$refs.audioPlayer
      if (!player) return
      
      const trackRect = this.$refs.progressTrack.getBoundingClientRect()
      const clickPosition = event.clientX - trackRect.left
      const clickPercentage = clickPosition / trackRect.width
      
      player.currentTime = clickPercentage * player.duration
      this.currentAudioTime = player.currentTime
    },
    
    skipForward() {
      const player = this.$refs.audioPlayer
      if (player) {
        player.currentTime = Math.min(player.currentTime + 10, player.duration)
      }
    },
    
    skipBackward() {
      const player = this.$refs.audioPlayer
      if (player) {
        player.currentTime = Math.max(player.currentTime - 10, 0)
      }
    },
    
    toggleLoop() {
      this.isLooping = !this.isLooping
      if (this.$refs.audioPlayer) {
        this.$refs.audioPlayer.loop = this.isLooping
      }
    }
  }
}
</script>

<style>
/* Global styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}

body {
  background-color: #f8f8f8;
}

/* Header styles */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  border-bottom: 1px solid #e0e0e0;
  background-color: white;
}

.logo-container {
  display: flex;
  align-items: center;
}

.asu-logo {
  height: 40px;
  margin-right: 1rem;
}

.site-title {
  font-size: 1.5rem;
  color: #212121;
}

.login-button {
  padding: 0.5rem 1rem;
  border: 1px solid #212121;
  border-radius: 20px;
  background-color: white;
  cursor: pointer;
  font-weight: 500;
}

/* Hero section */
.hero-section {
  text-align: center;
  padding: 3rem 1rem;
}

.hero-title {
  font-size: 3rem;
  margin-bottom: 1rem;
  color: #212121;
}

.hero-tagline {
  font-size: 1.5rem;
  color: #424242;
}

/* How it works section */
.how-it-works {
  padding: 2rem 1rem;
}

.section-title {
  font-size: 2rem;
  margin-bottom: 2rem;
  color: #212121;
  text-align: center;
}

.steps-container {
  display: flex;
  justify-content: space-around;
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.step {
  flex: 1;
  padding: 1.5rem;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.step h3 {
  margin-bottom: 1rem;
  color: #212121;
}

.step p {
  color: #424242;
}

/* Create section */
.create-section {
  display: flex;
  gap: 2rem;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.input-section {
  flex: 1;
  padding: 2rem;
  background-color: #212121;
  border-radius: 12px;
  color: white;
}

.learning-input, .file-upload-section, .genre-section {
  margin-bottom: 2rem;
}

.learning-input label, .genre-section label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.learning-input input, .genre-search input {
  width: 100%;
  padding: 0.75rem 1rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
}

.file-upload-section {
  text-align: center;
  margin: 1.5rem 0;
}

.file-feedback {
  margin-top: 0.5rem;
  font-size: 0.9rem;
  color: white;
}

.file-success {
  color: #4caf50;
  font-weight: bold;
  margin-right: 0.5rem;
}

.genre-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1rem;
}

.genre-btn {
  padding: 0.5rem 1rem;
  background-color: white;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  color: #212121;
  font-size: 0.9rem;
  transition: all 0.2s ease-in-out;
}

.additional-genres {
  margin-top: 0.75rem;
  animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
}

.genre-btn.active {
  background-color: #8C1D40; /* ASU maroon */
  color: white;
}

.genre-btn.more-btn {
  background-color: #e0e0e0;
}

.compose-btn {
  width: 100%;
  padding: 0.75rem;
  background-color: #000000;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  margin-top: 1rem;
}

/* Output section */
.output-section {
  flex: 1;
  background-color: white;
  border-radius: 12px;
  padding: 2rem;
}

.song-recommendation {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
}

.song-controls {
  display: flex;
  flex-direction: column;
}

.control-btn {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  color: #212121;
  padding: 0.5rem;
}

.play-btn {
  background-color: #8C1D40; /* ASU maroon */
  color: white;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.song-info {
  flex: 1;
}

.song-title-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.duration {
  color: #757575;
  font-size: 0.9rem;
}

.song-description {
  color: #424242;
}

.album-art {
  width: 80px;
  height: 80px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

.album-art img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.album-image {
  display: block;
  max-width: 100%;
}

.lyrics-section {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 2rem;
  background-color: #FFF5D5; /* Light yellow to match design */
}

.lyrics-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.expand-btn {
  background: none;
  border: none;
  cursor: pointer;
}

.lyrics-content {
  white-space: pre-line;
  max-height: 150px;
  overflow-y: hidden;
  transition: max-height 0.3s ease;
}

.lyrics-expanded {
  max-height: 500px;
  overflow-y: auto;
}

.player-controls {
  padding: 1rem 0;
}

.control-buttons {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  margin-bottom: 1rem;
}

.progress-bar {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.current-time, .total-time {
  font-size: 0.9rem;
  color: #757575;
}

.progress-track {
  flex: 1;
  height: 4px;
  background-color: #e0e0e0;
  border-radius: 2px;
}

.progress-filled {
  width: 20%;
  height: 100%;
  background-color: #8C1D40; /* ASU maroon */
  border-radius: 2px;
}

/* Media queries */
@media (max-width: 992px) {
  .create-section {
    flex-direction: column;
  }
  
  .steps-container {
    flex-direction: column;
  }
}

/* Icon placeholders - would be replaced with actual icons */
.icon-shuffle:after { content: "⤨"; }
.icon-play:after { content: "▶"; }
.icon-pause:after { content: "⏸"; }
.icon-prev:after { content: "◀◀"; }
.icon-next:after { content: "▶▶"; }
.icon-repeat:after { content: "🔁"; }
.icon-expand:after { content: "▼"; }
.icon-collapse:after { content: "▲"; }

/* Active state for control buttons */
.control-btn.active {
  color: #8C1D40; /* ASU maroon */
}

/* Placeholder text styling */
.placeholder-text {
  color: #aaa;
  font-style: italic;
}
</style>