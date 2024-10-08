<script setup>

defineProps({
  color: String,
  icon: Object,
  value: Number,
})

</script>

<template>
  <span
    class="circle icon is-large lighter"
    :class="[icon ? 'lighter' : 'value']"
    :style="{ 'background-color': icon ? color : '#ffffff', 'color': color }"
  >
    <i
      v-if="icon"
      class="fas fa-2x"
      :class="icon"
    ></i>
    <span v-else>
      {{ value }}
    </span>
  </span>
</template>

<style lang="scss" scoped>
.circle {
  border-radius: 24px;
}
.circle.icon {

  &.lighter {
    filter: brightness(1.1);
  }

  &.value {
    left: 40px;
    border: 5px solid;
    font-size: 16px;
    font-weight: 800;
    i {
      font-size: 34px;
    }
  }

  .fas {
    color: #ffffff;
  }
}

.circle.value-wrapper {
  width: 3rem;
  height: 3rem;
}
</style>
