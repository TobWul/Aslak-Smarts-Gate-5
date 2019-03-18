<template>
  <div id="app">
    <div id="nav">
      <Navigation></Navigation>
    </div>
    <router-view/>
  </div>
</template>
<script>
  import Navigation from '@/components/Navigation.vue'
  export default {
    components: {
      Navigation
    }
  }
</script>

<style lang="scss">
  #app {
    margin-left: $nav-width;
    padding: 4rem;
  }
</style>
