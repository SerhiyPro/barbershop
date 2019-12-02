<template>
  <div id="app">

<Header></Header>


<router-view>
</router-view>

<Footer></Footer>

<Modal></Modal>
  </div>

</template>

<script>

// import Home from "@/components/Home";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
export default {
  name: 'app',
  components: {
    // Home,
    Header,
    Footer

  },

}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
