<template>
  <div class="home">
    <el-container>
      <el-header>
        <el-row>
          <el-col :span="8">
            <div class='title'>EasyFile</div>
          </el-col>
          <el-col :span="16" style="text-align: right; padding-right: 30px;">
            <el-button plain size="medium" @click="route2home">首页</el-button>
            <el-button plain size="medium" @click="route2help">使用说明</el-button>
            <el-button plain size="medium" @click="route2login">登录</el-button>
            <el-button plain size="medium" @click="route2register">注册</el-button>
          </el-col>
        </el-row>
      </el-header>
      <el-main>
        
        <div> TBD </div>

      </el-main>
      <el-footer>
        Copyright &copy; 软件工程 - 2021. All rights reserved
      </el-footer>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: "pdf",
    data(){
      return {
      };
    },

    methods:{
      route2home(){
        this.$router.replace('/')
      },
      route2login(){
        this.$router.replace('/login')
      },
      route2register(){
        this.$router.replace('/register')
      },
      route2help(){
        this.$router.replace('/help')
      },
      route2word(){
        this.$router.replace('/word')
      },
      route2pdf(){
        this.$router.replace('/pdf')
      },

    }
  }

</script>

<style scoped>

.title {
  background-color: #c7ede6;
  width: 150px;
  padding-left: 45px;
}

.el-main {
  color: rgb(7, 7, 7);
  min-height: calc(100vh - 280px);
  text-align: center;
  margin: 80px 20px; 
}

</style>