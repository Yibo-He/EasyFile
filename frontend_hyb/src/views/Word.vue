<template>
<div>

  <el-container>
    <el-header>
      <el-row>
      
        <el-col :span="8">
          <div class='title'>EasyFile</div>
        </el-col>

        <el-col :span="16">
        <a-menu v-model="current" mode="horizontal" style="text-align: right">
          <a-menu-item key="home">
            <router-link to="/">
            首页
            </router-link>
          </a-menu-item>

          <a-menu-item key="about">
            <router-link to="/">
            关于
            </router-link>
          </a-menu-item>

          <a-menu-item key="login">
            <router-link to="/login">
            登录
            </router-link>
          </a-menu-item>
          
          <a-menu-item key="register">
            <router-link to="/register">
            注册
            </router-link>
          </a-menu-item>
        </a-menu>
        </el-col>
    
      </el-row>
    </el-header>


    <!-- 
      action: 必选参数，上传的地址
    -->
    <el-main>
      <el-row>

      <el-col :span="8" :offset="4">
      <el-upload
        class="upload-demo"
        drag
        action="https://jsonplaceholder.typicode.com/posts/"
        multiple>
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        <div class="el-upload__tip" slot="tip">只能上传doc/docx文件</div>
      </el-upload>
      </el-col>

      <el-col :span="8">
      <el-button type="primary" icon="el-icon-download" round size="medium" @click="download">下载处理后文件</el-button>
      </el-col>

      </el-row>
    </el-main>

  </el-container>

</div>
</template>

<script>
  export default {
    name: "word",
    data(){
      return {

      };
    },

    methods:{
      download(){
        
      }
    }
  }

</script>

<style scoped>

.title {
  background-color: #67bff1;
  width: 150px;
  padding-left: 30px;
}

</style>
