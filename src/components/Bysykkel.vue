<template>
  <div id="bysykkel">{{ info }}</div>
</template>

<script>
import axios from "axios";

const lademoparkenId = 6;

export default {
  name: "bysykkel",
  data: function() {
    return {
      sykler: 0,
      plass: "",
      info: ""
    };
  },
  mounted() {
    axios
      .get(
        "https://gbfs.urbansharing.com/trondheimbysykkel.no/station_status.json"
      )
      .then(response => (this.info = response));
  },
  methods: {}
};
</script>

<style lang="scss" scoped>
</style>