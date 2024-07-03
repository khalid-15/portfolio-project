<template>
  <v-container>
    <v-row>
      <v-col>
        <section id="home">
          <h1>Welcome to HRZen</h1>
          <p>This is the landing page of HRZen. Here are some screenshots of our app and documentation on how to navigate it.</p>
        </section>

        <section id="features">
          <h2>Features</h2>
          <div v-for="feature in features" :key="feature.id">
            <v-img :src="feature.image" aspect-ratio="1.7"></v-img>
            <h3>{{ feature.name }}</h3>
            <p>{{ feature.description }}</p>
          </div>
        </section>

        <section id="about">
          <h2>About</h2>
          <p>This project was inspired by ...</p>
          <p>Links: 
            <a href="https://github.com/your-profile" target="_blank">GitHub</a>, 
            <a href="https://linkedin.com/in/your-profile" target="_blank">LinkedIn</a>
          </p>
        </section>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      features: [
        { id: 1, image: 'path/to/image1.jpg', name: 'Feature 1', description: 'Description of Feature 1' },
        { id: 2, image: 'path/to/image2.jpg', name: 'Feature 2', description: 'Description of Feature 2' },
        { id: 3, image: 'path/to/image3.jpg', name: 'Feature 3', description: 'Description of Feature 3' },
      ]
    };
  }
};
</script>

<style scoped>
h1, h2, h3 {
  margin-bottom: 16px;
}
v-img {
  margin-bottom: 16px;
}
</style>
