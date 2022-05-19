<template>
  <div class="page">
    <div class="title">
      <h1>IMAGESO</h1>
    </div>
    <div class="subtitle">
      <h3>My Favorite</h3>
    </div>
    <div class="icon">
      <img src="../assets/icon.png" alt="icon" class="icon-img">
    </div>
    <div class="not-found" v-if="empty" style="color:#4842b8;">
      <h3>
        No Favorite Images Found
      </h3>
    </div>
    <div v-for="url in this.favoriteList" :key="url">
      <el-card :body-style="{ padding: '0px' }" style="background: #42b983">
        <img :src="url">
        <div style="padding: 14px;">
          <span>{{url.split('/')[4]}}</span>
          <br/>
          <div class="bottom clearfix">
            <el-button type="danger" icon="el-icon-delete" @click="deleteFromFavorite(url)">
              Delete</el-button>
          </div>
        </div>
      </el-card>
      <br/><br/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Favorite",
  data(){
    return{
      empty:true,
      favoriteList:[]

    }
  },
  mounted() {
    axios.get('viewFavorite')
    .then(
        (response)=>{
          // console.log(response)
          if(response.data.code === 200){
            this.favoriteList = response.data.favoriteList
            console.log(this.favoriteList)
            this.empty = false
            // console.log(this.favoriteList)
          }
        }
    )
  },
  methods:{
    deleteFromFavorite(path) {
      let config={
        method:'post',
        url:'deleteFavorite',
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        data: {
          path:path
        }
      }
      axios(config)
      .then(
          (response)=>{
            this.$message({
              message:'Deleted Successfully',
              showClose:true,
              type:'success'
            })
            location.reload()
          }
      )
    }
  }
}
</script>

<style scoped>
.title{
  color: white;
}
.subtitle{
  color: white;
}
.icon{
  position: absolute;
  left: 900px;
  top: 90px;
}
.icon-img{
  width: 100px;
  height: 100px;
}

</style>
