<template>
  <v-container>
    <v-row>
      <v-col>
        <section id="home" class="home-section">
          <v-img src="@/assets/images/cover-image-bg-trns.png" aspect-ratio="1.8" class="cover-image"></v-img>
          <h1 class="title">HRZen</h1>
          <p class="subtitle">Simplifying employee management and payroll for small to medium-sized businesses.</p>
        </section>

        <section id="features" class="features-section">
          <h2 class="section-title">Features</h2>
          <div v-for="feature in features" :key="feature.id" class="feature-item">
            <h3 class="feature-title">{{ feature.name }}</h3>
            <p>{{ feature.description }}</p>
            <v-img :src="feature.image" aspect-ratio="1.7" class="feature-image"></v-img>
            <template v-if="feature.additionalImages">
              <v-img v-for="(img, index) in feature.additionalImages" :key="index" :src="img" aspect-ratio="1.7" class="feature-image"></v-img>
            </template>
          </div>
        </section>

        <section id="about" class="about-section">
          <h2 class="section-title">About</h2>
          <p>
            Hello! I'm Kenza Dahhoum, a dedicated developer passionate about creating solutions that simplify everyday tasks. HRZen was born out of my desire to help small to medium-sized businesses efficiently manage their HR needs without the complexity and cost of traditional HR systems.
          </p>
          <h3 class="about-subtitle">Timeline</h3>
          <p>
            The development of HRZen started in June 2024. Over the next few months, I focused on building core features like attendance tracking, employee management, and event scheduling. Each phase of the project involved meticulous planning, coding, and testing to ensure a seamless user experience.
          </p>
          <h3 class="about-subtitle">Challenges</h3>
          <p>
            Working solo on HRZen, I faced several challenges. Being a beginner with Python and Flask, I had to spend considerable time learning and understanding these technologies. Balancing development with thorough testing was demanding, especially when ensuring data security and user authentication. Implementing role-based access control required careful consideration of permissions to prevent unauthorized access. Despite these hurdles, my determination and problem-solving skills helped me overcome these obstacles.
          </p>
          <h3 class="about-subtitle">About the App</h3>
          <p>
            HRZen is designed to streamline HR tasks for small to medium-sized businesses. It features attendance tracking, employee management, an event calendar, and secure login/registration. Each feature is crafted to be intuitive, ensuring that even those with minimal tech experience can use the app effectively. Additionally, more features like payroll management are planned for future updates to further enhance the application's capabilities.
          </p>
          <p>
            Links: 
            <a href="https://github.com/KenzaDahhoum/portfolio-project" target="_blank">GitHub Project</a>,
            <a href="https://github.com/KenzaDahhoum" target="_blank">GitHub Profile</a>,
            <a href="https://www.linkedin.com/in/dahhoum-kenza/" target="_blank">LinkedIn</a>,
            <a href="https://x.com/KDahhoum" target="_blank">Twitter</a>
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
        { id: 1, image: require('@/assets/images/attendance-track.png'), name: 'Attendance Tracking', description: 'Log check-ins and check-outs to manage attendance records efficiently for small to medium-sized businesses.' },
        { id: 2, image: require('@/assets/images/add-emp.png'), name: 'Employee Management', description: 'Manage employee details and positions all in one place, simplifying HR tasks for startups.' },
        { id: 3, image: require('@/assets/images/add-event.png'), name: 'Event Calendar', description: 'Organize and manage events, keeping track of important dates effortlessly.' },
        { id: 4, image: require('@/assets/images/login.png'), name: 'Login/Registration', description: 'Securely sign up and log in to the application, protecting user data with encrypted authentication.' },
        { id: 5, image: require('@/assets/images/managerRoles.png'), name: 'User Roles', description: 'Assign roles with specific permissions, ensuring secure and controlled access based on user roles. Managers can oversee all employee activities, while employees can manage their own records.', additionalImages: [require('@/assets/images/employeeRoles.png')] }
      ]
    };
  }
};
</script>

<style scoped>
.home-section {
  text-align: center;
  margin-top: 40px;
}

.cover-image {
  width: 100%;
  height: auto;
  margin-bottom: 20px;
}

.title {
  font-size: 48px;
  font-weight: 700;
  color: #1B263B;
  text-shadow: 2px 2px 4px #778DA9;
}

.subtitle {
  font-size: 24px;
  color: #415A77;
  margin-bottom: 20px;
}

.features-section {
  margin-top: 40px;
}

.feature-item {
  margin-bottom: 40px;
}

.feature-title {
  font-size: 24px;
  font-weight: bold;
  color: #415A77;
  margin-bottom: 10px;
}

.feature-image {
  margin-top: 0px;
  margin-bottom: 0px;
}

.section-title {
  font-size: 32px;
  font-weight: bold;
  color: #0D1B2A;
  margin-bottom: 20px;
}

.about-subtitle {
  font-size: 20px;
  font-weight: bold;
  color: #415A77;
  margin-top: 20px;
  margin-bottom: 10px;
}

.about-section {
  margin-top: 40px;
  font-size: 18px;
  color: #1B263B;
}
</style>
