<template>
  <div id="app">
    <nav>
      <router-link to="/">
        <i class="el-icon-search"></i>
        Search</router-link>
      <span>&nbsp;&nbsp;</span>
      <span style="color: white">|</span>
      <span>&nbsp;&nbsp;</span>
      <router-link to="/favorite">
        <i class="el-icon-star-off"></i>
        My Favorite
      </router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  /*color: #;*/
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #ffffff;
}
body {
  background: #42b983;
}

nav a.router-link-exact-active {
  color: #4842b8;
}
</style>
<script>

</script>
