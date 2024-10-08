<script setup>
import Tag from './components/Tag.vue'
import SKILLS from './constants'

</script>

<template>
    <div class="container">
        <div class="columns">
            <div class="column is-12">
              <section class="hero is-warning is-small">
                  <div class="hero-body">
                    <div class="media">
                      <figure class="media-left">
                          <img 
                            class="image is-128x128 rounded-pic"
                            src="./assets/nerebril.jpg">
                      </figure>
                      <div class="media-content">
                        <div class="content has-text-left">
                          <p>
                            <h2 class="is-size-3 has-text-weight-bold">{{ name }}</h2>
                          </p>
                          <h3 class="is-size-5 m-0 has-text-grey	">{{ classes }}</h3>
                          <h3 class="is-size-5 mt-2 has-text-grey	">Level {{ level }}</h3>
                        </div>
                      </div>
                    </div>
                  </div>
                </section>
                <section class="container has-background-white p-4">
                  <div class="columns">
                    <div v-for="stat in stats" class="column">
                      <div class="card has-background-light	">
                        {{ stat.name }}
                        <h3 class="is-size-3 has-text-weight-bold">{{ stat.value }}</h3>
                      </div>
                    </div>
                  </div>
                </section>
                <section class="container has-background-white p-4">
                  <div class="columns">
                    <div class="column is-3">
                      <div class="card has-background-light">
                        <div class="columns is-multiline">
                          <div v-for="stat in shortenedStats" class="column is-half">
                            {{ stat }}
                            <div class="rounded-pic">0</div>
                          </div>
                        </div>
                        <h4 class="is-size-5 has-text-weight-bold">Saving throws</h4>
                      </div>
                    </div>
                    <div class="column is-3">
                      <div class="card has-background-light">
                        <div class="columns">
                          <tag
                            :backgroundColor="deathSavesCircles[0].color"
                            :circles="deathSavesCircles"
                            :rightName="'successes'"
                          >
                          </tag>
                          <tag
                            :backgroundColor="deathSavesCircles[0].color"
                            :circles="deathSavesCircles"
                            :rightName="'failures'"
                          >
                          </tag>
                        </div>
                      </div>
                    </div>
                  </div>
                </section>
                <div class="columns">
                  <div class="column is-6">
                      <div class="card events-card">
                        <div class="skills-wrapper">
                          <tag 
                            v-for="skill in skills"
                            :backgroundColor="skill.color"
                            :circles="[
                              { color: skill.color, icon: skill.icon },
                              { color: skill.color, value: skill.value },
                            ]"
                            :rightName="skill.name"
                          >
                          </tag>
                        </div>
                      </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'CharacterSheet',

  data() {
    return {
      classes: 'Sorcerer',
      level: 3,
      name: 'Nerebril',
      stats: [
        { name: 'Strength', value: 10 },
        { name: 'Dexterity', value: 10 },
        { name: 'Constitution', value: 10 },
        { name: 'Intelligence', value: 10 },
        { name: 'Wisdom', value: 10 },
        { name: 'Charisma', value: 10 },
      ],
      skills: SKILLS,
      deathSavesCircles: [
        { color: '#3E526A' , value: 0 },
        { color: '#3E526A' , value: 0 },
        { color: '#3E526A' , value: 0 },
      ]
    };
  },

  computed: {
    shortenedStats() {
      return this.stats.map(stat => stat.name.slice(0, 3).toUpperCase());
    }
  }
}
</script>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}

.rounded-pic {
  border-radius: 64px;
}

.hero {
  border-radius: 10px 10px 0px 0px;
}

.skills-wrapper {
  border-left: dotted 3px;
  border-top: dotted 3px;
}

.skills-wrapper::before {
  content: 'SKILLS';
  left: -4px;
  top: 50px;
  font-weight: 800;
  font-size: 14px;
  position: absolute;
  rotate: 90°;
  transform: rotate(-90deg);
}
</style>
