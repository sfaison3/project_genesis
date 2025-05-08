<template>
  <div class="file-upload">
    <input 
      type="file" 
      ref="fileInput" 
      @change="handleFileChange" 
      class="hidden-input"
      accept=".pdf,.doc,.docx,.txt,.jpg,.png,.jpeg"
    />
    <button @click="triggerFileInput" class="upload-button">
      <slot>Upload</slot>
    </button>
  </div>
</template>

<script>
export default {
  name: 'FileUpload',
  emits: ['file-selected'],
  data() {
    return {
      selectedFile: null
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
    }
  }
}
</script>

<style scoped>
.file-upload {
  display: inline-block;
}

.hidden-input {
  display: none;
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

.upload-button:hover {
  background-color: #6a3de8;
}
</style>