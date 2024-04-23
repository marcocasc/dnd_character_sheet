<script setup>
import { ref } from 'vue'

defineProps({
  skill: Object,
})

const count = ref(0)
</script>

<template>
  <div class="skill-tag-wrapper">
    <span
      class="tag is-info is-lowercase"
      :style="{ 'background-color': skill.color }"
    >
      <span
        class="circle icon is-large lighter"
        :style="{ 'background-color': skill.color }"
      >
        <i 
          class="fas fa-2x"
          :class="skill.icon"
        ></i>
      </span>
      <span
        class="circle icon is-large skill-value"
        :class="[skill.value > 1 ? 'has-text-success' : skill.value < 0 ? 'has-text-danger' : 'has-text-black'	]"
        :style="{ 'border-color': skill.color }"
      >
        {{ skill.value }}
      </span>
      {{ skill.name }}
    </span>
  </div>
</template>

<style lang="scss" scoped>
.skill-tag-wrapper {
  margin: 15px;
  display: inline-block;
}
.tag {
  padding: 16px 16px 16px 100px;
  position: relative;
  min-width: 230px;
  border-radius: 20px;
}
.circle {
  border-radius: 24px;
}
.circle.icon {
  position: absolute;
  left: -10px;

  &.lighter {
    filter: brightness(1.1);
  }

  &.skill-value {
    left: 40px;
    background-color: #ffffff;
    border: 5px solid;
    font-size: 16px;
    font-weight: 800;
    i {
      font-size: 34px;
    }
  }

  .fa {
    color: #ffffff;
  }
}

.circle.value-wrapper {
  width: 3rem;
  height: 3rem;
}
</style>
