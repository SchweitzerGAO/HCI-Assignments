<template xmlns="">
  <div class="page">
    <div class="title">
       <h1>IMAGESO</h1>
    </div>
    <div class="subtitle">
      <h3>Image Search Engine</h3>
    </div>
    <div class="icon">
      <img src="../assets/icon.png" alt="icon" class="icon-img">
    </div>
    <div class="tips">
      Click
      <i class="el-icon-search"></i>
      to upload the image and search!
    </div>

    <div class="img-show" v-if="imgUrl">
      <img :src="imgUrl" class="avatar" alt="upload">
      <span class="actions">
		<!-- 放大 -->
		<span class="item">
			<i class="el-icon-zoom-in" @click="enlarge"></i>
		</span>
        <!-- 删除 -->
		<span class="item">
			<i class="el-icon-delete" @click="del"></i>
		</span>
	</span>
    </div>

    <div class="search-input" v-else>
      <el-upload
          action="#"
          class="uploader-avatar"
          list-type="picture-card"
          :before-upload="beforeUpload"
          :show-file-list="false"
          :http-request="search"
          :on-change="imgPreview">
        <i class="el-icon-search avatar-uploader-icon"></i>
      </el-upload>
    </div>
    <el-dialog :visible.sync="dialogVisible">
      <img width="100%" :src="dialogUrl" alt="">
    </el-dialog>

    <div class="searching" v-if="searching">
      <i class="el-icon-loading"></i>
      <h4>Searching...</h4>
    </div>

    <div class="result" v-if="this.lenResult!==0">
      <h2>{{this.lenResult}} Results Found</h2>
      <div v-for="(url,index) in this.searchResult" :key="url">
        <el-card :body-style="{ padding: '0px' }" style="background: #42b983">
          <img :src="url" alt="result">
          <div style="padding: 14px;">
            <span>{{url.split('/')[4]}}</span>
            <br/>
            <div class="bottom clearfix">
              <el-button type="primary" icon="el-icon-plus" @click="addToFavorite('./static/result/'+url)">
                Add to Favorite</el-button>
            </div>
          </div>
        </el-card>
        <br/><br/>
      </div>

    </div>

  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Search",
  data (){
    return {
      searchResult:[],
      lenResult:0,
      uploadPath:'',
      imgUrl:'',
      dialogUrl:'',
      dialogVisible:false,
      searching:false,
      image: new FormData(),
    }
  },
  methods:{
    search(){
      this.searching=true
      const img = this.image
      let config = {
        method: 'post',
        url: 'imgSearch',
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        data:img
      }
      axios(config)
      .then(
          (response) =>{
            this.searching=false
            if(response.data.code===400){
              this.$message({
                message:response.data.msg,
                showClose:true,
                type:'error'
              })
            }
            else{
              this.searchResult = response.data.data.searchResult
              this.lenResult = response.data.data.lenResult
              this.uploadPath = response.data.data.uploadPath
              console.log(this.searchResult)
              console.log(this.lenResult)
              console.log( this.uploadPath)
            }
          }
      )

    },
    addToFavorite(path){
      let config={
        method:'post',
        url:'addFavorite',
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        data: {
          path:path
        }
      }
        axios(config)
      .then(
          (response) =>{
            if(response.data.code === 400){
              this.$message({
                message:response.data.msg,
                showClose:true,
                type:'error'
              })
            }
            else{
              this.$message({
                message:'Added to Favorite Successfully',
                showClose:true,
                type:'success'
              })
            }
          }
      )
    },
    getPath(path){
      return path ? require('@/' + path) : '';
    },

    beforeUpload: function(file){
      this.image.append('file',file)
      // console.log(this.image.get('file'))
    },
    imgPreview: function(file){
      // console.log(file)
      // this.image.append('file',file)
      // console.log(this.image.get('file'))
      this.imgUrl =  URL.createObjectURL(file.raw);

    },
    enlarge: function(){
      this.dialogVisible = true;
      this.dialogUrl = this.imgUrl;
    },
    del: function(){
      this.image.delete('file')
      this.imgUrl =  '';
      this.dialogUrl = '';
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
.tips{
  color: white;
}
.search-input{
  position: absolute;
  left: 680px;
  top: 240px;
}
.uploader-avatar>>>.el-upload {
  background-color: #fbfdff;
  border: 1px dashed #c0ccda;
  border-radius: 6px;
  box-sizing: border-box;
  width: 148px;
  height: 148px;
  cursor: pointer;
  line-height: 146px;
  vertical-align: top;
  overflow: hidden;
}
.img-show{
  position: absolute;
  left: 680px;
  top: 240px;
  border: 1px solid #c0ccda;
  border-radius: 6px;
  box-sizing: border-box;
  width: 148px;
  height: 148px;
  cursor: pointer;
  overflow: hidden;
}
.uploader-avatar>>>.el-upload:hover {
  border-color: #409EFF;
}
.uploader-avatar>>>i {
  font-size: 28px;
  color: #8c939d;
}
.avatar{
  width: 148px;
  height: 148px;
  display: block;
}

.actions{
  position: absolute;
  width: 100%;
  height: 100%;
  line-height: 148px;
  left: 0;
  top: 0;
  cursor: default;
  text-align: center;
  color: #fff;
  opacity: 0;
  font-size: 20px;
  background-color: rgba(0,0,0,.5);
  transition: opacity .3s;
}
.actions:hover{
  opacity: 1;
}
.actions:hover span{
  display: inline-block;
}
.actions span{
  display: none;
  margin: 0 16px;
  cursor: pointer;
}

.searching{
  color: #4842b8;
  position: absolute;
  left: 705px;
  top: 410px;
  font-size: 20px;
}
.result{
  position: absolute;
  left: 500px;
  top: 470px;
  color: #4842b8;
}
</style>
