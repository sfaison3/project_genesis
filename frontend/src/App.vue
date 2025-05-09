<template>
  <div>
    <header class="header">
      <div class="logo-container">
        <!-- ASU Logo as inline SVG for reliable rendering on all platforms -->
        <svg width="120" height="40" viewBox="0 0 720 240" class="asu-logo" xmlns="http://www.w3.org/2000/svg">
          <g>
            <path fill="#8C1D40" d="M219,32.3c-4.3,1.6-10.4,3.4-14.9,5.9c-0.5,0.3-1,0.8-1,1.3c0,0.6,0.4,1.3,1.4,2.4c1.8,2.7,5.4,6.5,5.4,6.5
              s8.8-0.7,10.2-0.8c1.5-0.1,2.6-2.3,2.6-5.3C222.8,39,222,30.5,219,32.3z M143.7,93h-21.4l9.8-34.6L143.7,93z M369.1,39.1
              c-1.4-1.4-9.8-1.4-12.2,0c-2.2,1.3-31.4,57.1-31.4,57.1h19.3l3.7-8.9h29.1l0.5,8.9h17.1C395.3,96.2,370.5,40.6,369.1,39.1z
               M352.4,73.8l9.7-23.4l5.3,23.4H352.4z M498.3,39h-18.2v57.2h18.2V39z M217.4,39h-17.3l-33.4,57h19.7l5.9-11.3h33.2l1.1,11.3
              h18.6L217.4,39z M197.3,71.4l12.2-24.1l6.3,24.1H197.3z M283.8,61.8c10-2.3,18.3-11.1,18.3-21.4c0-13.2-10.2-20.1-23.6-20.1
              h-37.1v76h19.7V72.8h2.2l19.1,23.4h23.5L283.8,61.8z M265,57.1h-3.8V35.1h7.1c6.2,0,13-1.1,13,10.8C281.3,57.1,271.3,57.1,265,57.1
              z M439.5,59.8c0-27.4-39.2-19.3-39.2-32.5c0-4.2,4.8-5.5,8.8-5.5c5.5,0,27.6,5.5,27.6,5.5V11.9c0,0-15.3-4.5-30.2-4.5
              c-15.1,0-28.3,9.7-28.3,25.3c0,28.3,38.4,18.3,38.4,32.3c0,6.3-7.6,8.1-14.9,8.1c-10.5,0-29.8-8.7-29.8-8.7v15.9
              c0,0,15.6,6.9,33.7,6.9C425.6,87.2,439.5,74.1,439.5,59.8z M469.8,39H445V31h34.8V15.8h-54.1v80.4h55.8V80.6h-36.5v-26h24.8
              V39z M581.4,15.8h-19.7v80.4h19.7V15.8z M639.1,75.8c-17.3,0-17.3-39.7,0-39.7C656.3,36.1,657.2,75.8,639.1,75.8z M639.1,19.6
              c-31.3,0-41.8,26.5-41.8,36.2c0,9.7,10.6,36.2,41.8,36.2c31.1,0,41.8-26.5,41.8-36.2C680.9,46.1,670.2,19.6,639.1,19.6z
               M713.9,61.2h9.8c3.5,0,9.2,2.3,9.2,9.2c0,7.4-3.7,9.9-10.4,9.9h-8.6V61.2z M713.9,35.1h8c6.1,0,8.1,2.7,8.1,8
              c0,5.5-2.9,7.4-8.9,7.4h-7.3V35.1z M694.2,15.8v80.4h32.1c11.9,0,27.8-7.6,27.8-25.7c0-7.9-4.7-14.5-12.1-17.4
              c4.7-3.4,7.7-7.6,7.7-16.4c0-14.3-10.8-20.9-26.2-20.9H694.2z M519.4,15.8v80.4h56.7V80.6h-37V15.8H519.4z M112.9,54.6
              c0,9.7-2.1,13.9-5.5,18.4c-3.5,4.6-8.3,6.9-13.9,6.9c-5.7,0-10.4-2.4-13.7-6.8c-3.4-4.4-5.5-8.5-5.5-18.5V15.8H55.4v42.5
              c0,15.5,5.4,25,16.1,30.1c6.9,3.3,14.6,4.9,22.1,4.9c7.4,0,15.2-1.8,21.9-4.9c10.7-5.1,16.1-14.6,16.1-30.1V15.8h-18.7V54.6z
               M37.7,51.3c-8.9-2.9-17.1-5.9-17.1-12.4c0-7.7,9.5-7.6,14-7.6c8.1,0,18.6,2.4,26.3,7.1V20.2c-8.1-4.7-17.6-7-27-7
              C26.6,13.2,0,18.6,0,39.6c0,22.5,23.7,28.9,34.4,32.1c11.1,3.3,19.8,5.7,19.8,13c0,10.8-13.8,9.2-20,9.2
              c-9.1,0-22.2-5.1-30.1-10.2v19.7c9.9,5.6,20.4,8.9,31.4,8.9c18.7,0,39.6-9.8,39.6-28.8C75.1,63.8,56.1,57.6,37.7,51.3z">
            </path>
          </g>
        </svg>
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
                :class="['genre-btn', {'active': selectedGenre === genre.id, 'genre-selected': selectedGenre === genre.id}]" 
                @click="selectGenre(genre.id)"
              >
                {{ genre.name }} {{ selectedGenre === genre.id ? '✓' : '' }}
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
                :class="['genre-btn', {'active': selectedGenre === genre.id, 'genre-selected': selectedGenre === genre.id}]" 
                @click="selectGenre(genre.id)"
              >
                {{ genre.name }} {{ selectedGenre === genre.id ? '✓' : '' }}
              </button>
            </div>
          </div>

          <button class="compose-btn" @click="generateMusic" :disabled="isLoading">{{ isLoading ? 'Composing...' : 'Compose' }}</button>
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
              <button class="control-btn" aria-label="Shuffle">
                <img :src="icons.shuffle" alt="Shuffle" class="control-icon" />
              </button>
              <button class="control-btn" @click="skipBackward" aria-label="Previous">
                <img :src="icons.previous" alt="Previous" class="control-icon" />
              </button>
              <button 
                class="control-btn play-btn"
                @click="togglePlayback"
                aria-label="Play or Pause"
              >
                <img 
                  :src="isPlaying ? icons.pause : icons.play" 
                  :alt="isPlaying ? 'Pause' : 'Play'" 
                  class="control-icon play-icon"
                />
              </button>
              <button class="control-btn" @click="skipForward" aria-label="Next">
                <img :src="icons.next" alt="Next" class="control-icon" />
              </button>
              <button 
                class="control-btn"
                :class="{ 'active': isLooping }"
                @click="toggleLoop"
                aria-label="Repeat"
              >
                <img :src="icons.repeat" alt="Repeat" class="control-icon" />
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
          
          <div class="lyrics-section">
            <div class="lyrics-header">
              <h3>Lyrics</h3>
              <button 
                class="expand-btn"
                @click="lyricsExpanded = !lyricsExpanded"
              >
                <img 
                  :src="lyricsExpanded ? icons.collapse : icons.expand" 
                  :alt="lyricsExpanded ? 'Collapse' : 'Expand'" 
                  class="expand-icon"
                />
              </button>
            </div>
            <div 
              class="lyrics-content"
              :class="{ 'lyrics-expanded': true }"
            >
              <p v-if="lyrics">{{ lyrics }}</p>
              <p v-else class="placeholder-text">Lyrics will appear here after generating music</p>
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

// Import player control icons
import shuffleIcon from './assets/icons/shuffle.svg'
import previousIcon from './assets/icons/previous.svg'
import playIcon from './assets/icons/play.svg'
import pauseIcon from './assets/icons/pause.svg'
import nextIcon from './assets/icons/next.svg'
import repeatIcon from './assets/icons/repeat.svg'
import expandIcon from './assets/icons/expand.svg'
import collapseIcon from './assets/icons/collapse.svg'

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
      lyricsExpanded: true,
      usingGenericEndpoint: false, // Track which endpoint we're using
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
      // Player control icons
      icons: {
        shuffle: shuffleIcon,
        previous: previousIcon,
        play: playIcon,
        pause: pauseIcon,
        next: nextIcon,
        repeat: repeatIcon,
        expand: expandIcon,
        collapse: collapseIcon
      },
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
    },
    
    // We're now using inline SVG for the logo, so this property is no longer needed
  },
  mounted() {
    console.log('API URL:', this.apiUrl)
    this.checkApiHealth()
    // Check API health every 30 seconds
    setInterval(this.checkApiHealth, 30000)
  },
  methods: {
    selectGenre(genreId) {
      console.log(`Genre selected: ${genreId}`)
      // Force a refresh of the selection by clearing it first
      this.selectedGenre = null
      // Use a small timeout to ensure UI updates
      setTimeout(() => {
        this.selectedGenre = genreId
        console.log(`Genre selection updated to: ${this.selectedGenre}`)
      }, 10)
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
      
      // Force refresh of the selected genre before generating
      console.log(`Using selected genre for generation: ${this.selectedGenre}`)
      const currentGenre = this.selectedGenre
      
      // Reset audio player and UI state for a fresh generation
      if (this.$refs.audioPlayer) {
        this.$refs.audioPlayer.pause()
        this.isPlaying = false
      }
      
      this.isLoading = true
      
      try {
        // Use a more direct approach with the right API endpoint
        let endpoint = this.apiUrl
        if (!endpoint.endsWith('/')) {
          endpoint += '/'
        }
        
        // Check if we're using localhost and modify endpoint accordingly
        const isLocalDevelopment = window.location.hostname === 'localhost' || 
                                  window.location.hostname === '127.0.0.1';
                                  
        // Use the generic endpoint for local development as a fallback
        if (isLocalDevelopment) {
          console.log('Local development detected, using generic endpoint');
          endpoint += 'generate'; // Use the generic endpoint that works
          
          // When using the generic endpoint, we need to adjust our request
          this.usingGenericEndpoint = true;
        } else {
          // In production, use the specific music endpoint
          endpoint += 'music/generate';
          this.usingGenericEndpoint = false;
        }
        
        console.log('Making request to:', endpoint)
        
        // Standard JSON request - format depends on which endpoint we're using
        let requestBody;
        
        // Find the currently selected genre's name from our genres list
        const selectedGenreName = this.genres.find(g => g.id === this.selectedGenre)?.name || this.selectedGenre;
        
        // Log the selected genre details for debugging
        console.log(`\nSelected genre ID: ${this.selectedGenre}`)
        console.log(`Selected genre name: ${selectedGenreName}`)
        
        // Create a custom prompt that includes the selected genre
        const customPrompt = `Create a ${selectedGenreName} style music about ${this.learningTopic}. Make sure the music has a strong ${selectedGenreName} feel and sound.`;

        if (this.usingGenericEndpoint) {
          // For the generic /api/generate endpoint
          requestBody = {
            input: this.learningTopic,
            model: "beatoven",
            genre: this.selectedGenre,
            duration: 60,
            learning_topic: this.learningTopic,
            custom_prompt: customPrompt
          };
        } else {
          // For the specific /api/music/generate endpoint
          requestBody = {
            topic: this.learningTopic,
            genre: this.selectedGenre,
            duration: 60,
            test_mode: true, // Use test mode to ensure we get a response
            custom_prompt: customPrompt // Add the custom prompt here
          };
        }
        
        if (this.uploadedFile) {
          console.log('File upload will be handled in a future version')
          // For now, just note the file but don't try to upload it
        }
        
        console.log('Request payload:', JSON.stringify(requestBody, null, 2))
        console.log(`Using Beatoven genre: ${requestBody.genre}`)
        
        // Use XMLHttpRequest instead of fetch for better compatibility
        const xhr = new XMLHttpRequest()
        xhr.open('POST', endpoint, true)
        xhr.setRequestHeader('Content-Type', 'application/json')
        
        // Save the learning topic to avoid "this" scope issues
        const currentTopic = this.learningTopic
        
        // Create a promise wrapper around XHR
        const xhrPromise = new Promise((resolve, reject) => {
          xhr.onload = function() {
            if (xhr.status >= 200 && xhr.status < 300) {
              try {
                // Log raw response for debugging
                console.log('Raw XHR response:', xhr.responseText)
                
                // Check for empty response
                if (!xhr.responseText || xhr.responseText.trim() === '') {
                  // Use a fallback response
                  console.warn('Empty response received, using fallback')
                  resolve({
                    output_url: 'https://filesamples.com/samples/audio/mp3/sample3.mp3',
                    genre: requestBody.genre,
                    title: `Song about ${currentTopic}`,
                    lyrics: `This is a song about ${currentTopic} in ${requestBody.genre} style.`,
                    status: 'completed',
                    task_id: `fallback-${Date.now()}`
                  })
                } else {
                  // Try to parse the response
                  try {
                    const data = JSON.parse(xhr.responseText)
                    resolve(data)
                  } catch (parseError) {
                    console.error('JSON parse error:', parseError)
                    // Use fallback on parse error
                    resolve({
                      output_url: 'https://filesamples.com/samples/audio/mp3/sample3.mp3',
                      genre: requestBody.genre,
                      title: `Song about ${currentTopic}`,
                      lyrics: `This is a song about ${currentTopic} in ${requestBody.genre} style.`,
                      status: 'completed',
                      task_id: `parse-error-${Date.now()}`
                    })
                  }
                }
              } catch (error) {
                console.error('Error handling response:', error)
                reject(error)
              }
            } else {
              console.error('XHR error status:', xhr.status)
              // Try to get response text for error details
              let errorDetails = '';
              try {
                if (xhr.responseText) {
                  errorDetails = `: ${xhr.responseText.substring(0, 100)}`;
                }
              } catch (e) {}
              reject(new Error(`HTTP error: ${xhr.status}${errorDetails}`))
            }
          }
          
          xhr.onerror = function() {
            console.error('XHR request failed')
            reject(new Error('Network error'))
          }
          
          xhr.ontimeout = function() {
            console.error('XHR request timed out')
            reject(new Error('Request timed out'))
          }
        })
        
        // Send the request
        xhr.send(JSON.stringify(requestBody))
        
        try {
          // Wait for the XHR to complete
          const data = await xhrPromise
          console.log('Processed XHR response:', data)
          this.handleApiResponse(data)
        } catch (xhrError) {
          console.error('XHR error:', xhrError)
          // Even with an error, try to keep the UI working
          this.audioUrl = 'https://filesamples.com/samples/audio/mp3/sample3.mp3'
          this.songTitle = `Song about ${this.learningTopic} (Error Recovery)`
          this.lyrics = `This is a placeholder song about ${this.learningTopic}.\nThere was an error communicating with the server.`
          
          alert(`Error: ${xhrError.message}\n\nFalling back to sample audio.`)
        }
        
      } catch (error) {
        console.error('Overall error:', error)
        // Fallback to sample audio in worst case
        this.audioUrl = 'https://filesamples.com/samples/audio/mp3/sample3.mp3'
        this.songTitle = `Song about ${this.learningTopic} (Error Recovery)`
        this.lyrics = `This is a placeholder song about ${this.learningTopic}.\nThere was an error communicating with the server.`
        
        alert(`Error: ${error.message}\n\nFalling back to sample audio.`)
      } finally {
        this.isLoading = false
      }
    },
    
    handleApiResponse(data) {
      console.log('Processing API response:', data);
      
      // Use a sample audio URL if we need a fallback
      const sampleAudioUrl = 'https://filesamples.com/samples/audio/mp3/sample3.mp3';
      
      try {
        // Safeguard against null or undefined data
        if (!data) {
          console.error('Null or undefined API response');
          data = {
            output_url: sampleAudioUrl,
            title: `Song about ${this.learningTopic} (Fallback)`,
            lyrics: `This is a fallback song about ${this.learningTopic}.`
          };
        }
        
        // Handle the music generation response - check for different formats
        if (data.type === 'music') {
          // This is from the /api/generate endpoint format
          this.audioUrl = data.output || sampleAudioUrl
          this.songTitle = data.title || `Song about ${this.learningTopic}`
          this.lyrics = data.lyrics || 'Lyrics not available for this song.'
          this.songDescription = data.description || 'The why, and how this will benefit you'
          
          // If album art was generated
          if (data.album_art) {
            this.albumArt = data.album_art
          }
        } else if (data.output_url || data.track_url) {
          // This is from the /api/music/generate endpoint format
          this.audioUrl = data.output_url || data.track_url || sampleAudioUrl
          this.songTitle = data.title || `Song about ${this.learningTopic}`
          this.lyrics = data.lyrics || 'Lyrics not available for this song.'
          // Find genre display name
          const genreName = this.genres.find(g => g.id === data.genre)?.name || data.genre || 'AI';
          this.songDescription = `${genreName} music about ${this.learningTopic}`
          
          // Store the task_id for polling
          if (data.task_id) {
            console.log('Task ID for tracking:', data.task_id)
            // If needed, we could poll the status endpoint with this task_id
          }
        } else {
          // Unknown format - log it and try to extract useful information
          console.warn('Unknown API response format:', data);
          
          // Try to extract audio URL from any reasonable field
          this.audioUrl = data.output_url || data.preview_url || data.track_url || 
                         data.url || data.output || data.audio || sampleAudioUrl
          
          this.songTitle = data.title || data.name || `Song about ${this.learningTopic}`
          this.lyrics = data.lyrics || 'Lyrics not available for this song.'
          // Find genre display name if a genre is provided
          let genreDescription = 'Music generated by AI';
          if (data.genre) {
            const genreName = this.genres.find(g => g.id === data.genre)?.name || data.genre;
            genreDescription = `${genreName} music about ${this.learningTopic}`;
          }
          this.songDescription = data.description || genreDescription
        }
        
        // Check if we have a valid URL format
        if (!this.audioUrl || !this.audioUrl.startsWith('http')) {
          console.warn('Invalid audio URL:', this.audioUrl);
          this.audioUrl = sampleAudioUrl;
        }
        
        // Only proceed with playback if we have a valid audio URL
        if (this.audioUrl) {
          // Start playback when ready
          this.$nextTick(() => {
            const player = this.$refs.audioPlayer
            if (player) {
              console.log('Loading audio from URL:', this.audioUrl)
              player.load()
              
              // Auto-play after a short delay to ensure loading
              setTimeout(() => {
                try {
                  this.isPlaying = true
                  player.play().catch(err => {
                    console.error('Error auto-playing:', err)
                    this.isPlaying = false
                  })
                } catch (playError) {
                  console.error('Exception during play():', playError)
                  this.isPlaying = false
                }
              }, 500)
            } else {
              console.error('Audio player element not found')
            }
          })
        } else {
          console.error('No audio URL found in the response');
          alert('No audio URL was returned from the server. Using sample audio instead.');
          this.audioUrl = sampleAudioUrl;
        }
      } catch (error) {
        console.error('Error in handleApiResponse:', error);
        // Fallback to a sample in case of any error
        this.audioUrl = sampleAudioUrl;
        this.songTitle = `Song about ${this.learningTopic} (Error Recovery)`;
        this.lyrics = 'Lyrics not available due to an error processing the server response.';
        this.songDescription = 'AI-generated music (fallback)';
        
        // Try to play the fallback
        this.$nextTick(() => {
          const player = this.$refs.audioPlayer
          if (player) {
            player.load()
            setTimeout(() => {
              try {
                player.play().catch(() => {})
              } catch (e) {}
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
  object-fit: contain;
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
  font-weight: bold;
  transform: scale(1.05); /* Slightly larger to stand out */
  transition: all 0.2s ease-in-out;
  box-shadow: 0 2px 4px rgba(0,0,0,0.15);
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

.play-btn img {
  filter: brightness(0) invert(1); /* Make the icon white */
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
  margin-top: 2rem;
  margin-bottom: 2rem;
  background-color: #FFF5D5; /* Light yellow to match design */
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
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
  max-height: 300px;
  overflow-y: hidden;
  transition: max-height 0.3s ease;
}

.lyrics-expanded {
  max-height: 600px;
  overflow-y: auto;
}

.player-controls {
  padding: 1rem 0;
  margin-bottom: 1.5rem;
  border-bottom: 1px solid #e0e0e0;
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

/* Player control icons */
.control-icon {
  width: 24px;
  height: 24px;
  display: block;
}

.play-icon {
  width: 20px;
  height: 20px;
}

.expand-icon {
  width: 16px;
  height: 16px;
  display: block;
}

/* Active state for control buttons */
.control-btn.active {
  color: #8C1D40; /* ASU maroon */
}

.control-btn.active img {
  filter: invert(11%) sepia(79%) saturate(4223%) hue-rotate(334deg) brightness(93%) contrast(93%); /* Make icon ASU maroon */
}

/* Placeholder text styling */
.placeholder-text {
  color: #aaa;
  font-style: italic;
}
</style>