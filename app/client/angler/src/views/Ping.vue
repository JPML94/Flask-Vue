<template>
  <div class="test">
    <h1>Backend Resources Demo</h1>
    <p>Click on the links below to fetch data from the Flask server</p>
    <a href="" @click.prevent="fetchPingResource">Fetch Ping Resource</a><br/>
    <h4>Results</h4>
    <p v-for="r in resources" :key="r.value">
      Server Response: {{r.value}}
    </p>
    <p>{{error}}</p>
  </div>
</template>

<script>
import $backend from "../backend";

export default {
  name: "test",
  data() {
    return {
      resources: [],
      error: ""
    };
  },
  methods: {
    fetchPingResource() {
      $backend
        .fetchPingResource()
        .then(responseData => {
          this.resources.push(responseData);
        })
        .catch(error => {
          this.error = error.message;
        });
    }
  }
};
</script>

<style lang="scss">
</style>
