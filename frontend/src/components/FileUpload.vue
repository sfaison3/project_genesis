<template>
  <div class="file-upload">
    <div 
      class="drop-area" 
      @dragover.prevent="onDragOver" 
      @dragleave.prevent="onDragLeave" 
      @drop.prevent="onDrop"
      :class="{ 'active-drop': isDragging }"
    >
      <div v-if="selectedFile" class="file-info">
        <span class="file-name">{{ selectedFile.name }}</span>
        <button @click.prevent="clearFile" class="clear-button">×</button>
      </div>
      <div v-else class="upload-prompt">
        <!-- No folder icon -->
        <p class="drop-text">Drop your file here or</p>
        <button @click="triggerFileInput" class="upload-button">
          <slot>Upload</slot>
        </button>
      </div>
    </div>
    <input 
      type="file" 
      ref="fileInput" 
      @change="handleFileChange" 
      class="hidden-input"
      accept=".pdf,.doc,.docx,.txt,.jpg,.png,.jpeg"
    />
  </div>
</template>

<script>
export default {
  name: 'FileUpload',
  emits: ['file-selected'],
  data() {
    return {
      selectedFile: null,
      isDragging: false
    }
  },
  methods: {
    triggerFileInput() {
      this.$refs.fileInput.click()
    },
    handleFileChange(event) {
      this.selectedFile = event.target.files[0]
      if (this.selectedFile) {
        this.$emit('file-selected', this.selectedFile)
      }
    },
    onDragOver(event) {
      this.isDragging = true
      event.dataTransfer.dropEffect = 'copy'
    },
    onDragLeave() {
      this.isDragging = false
    },
    onDrop(event) {
      this.isDragging = false
      const files = event.dataTransfer.files
      if (files.length > 0) {
        this.selectedFile = files[0]
        this.$emit('file-selected', this.selectedFile)
      }
    },
    clearFile() {
      this.selectedFile = null
      this.$emit('file-selected', null)
      this.$refs.fileInput.value = ''
    }
  }
}
</script>

<style scoped>
.file-upload {
  width: 100%;
}

.drop-area {
  border: 2px dashed #ccc;
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
  transition: all 0.3s ease;
  cursor: pointer;
  min-height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  background-color: #f9f9f9;
}

.active-drop {
  background-color: rgba(255, 255, 255, 0.1);
  border-color: #7c4dff;
  transform: scale(1.02);
}

.upload-prompt {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.upload-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.drop-text {
  margin-bottom: 0.5rem;
}

.hidden-input {
  display: none;
}

.upload-button {
  background-color: #8C1D40; /* ASU maroon */
  color: white;
  border: none;
  border-radius: 20px;
  padding: 8px 25px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.upload-button:hover {
  background-color: #6a0c2d; /* Darker ASU maroon */
}

.file-info {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  width: 100%;
}

.file-name {
  word-break: break-all;
  max-width: 80%;
}

.clear-button {
  background: none;
  border: none;
  color: #212121;
  font-size: 1.5rem;
  cursor: pointer;
  padding: 0;
  line-height: 1;
}
</style>