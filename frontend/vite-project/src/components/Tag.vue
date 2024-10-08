<script setup>
import CircleElement from './CircleElement.vue'

defineProps({
  backgroundColor: String,
  circles: Array,
  leftName: String,
  rightName: String,
})

</script>

<template>
  <div class="tag-wrapper">
    <span
      class="tag is-info is-lowercase"
      :style="{ 'background-color': backgroundColor }"
    >
      <span v-if="leftName">{{ leftName }}</span>
      <circle-element
        v-for="circle in circles"
        :color="circle.color"
        :icon="circle.icon"
        :value="circle.value"
      >
      </circle-element>
      
      <span
        v-if="rightName"
        class="right-name"
      >
        {{ rightName }}
      </span>
    </span>
  </div>
</template>

<style lang="scss" scoped>
.right-name {
  margin-left: auto;
  margin-right: 20px;
}
.tag-wrapper {
  margin: 15px;
  display: inline-block;
}
.tag {
  padding: 16px 0px 16px 0px;
  position: relative;
  min-width: 230px;
  border-radius: 20px;
  gap: 10px;
}
</style>
