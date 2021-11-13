<template>
  <div class="home">
    <el-container>
      <el-header>
        <el-row>
          <el-col :span="8">
            <div class='title'>EasyFile</div>
          </el-col>
          <el-col :span="16" style="text-align: right; padding-right: 30px;">
            <el-button plain size="medium" @click="route2help">使用说明</el-button>
            <el-button plain size="medium" @click="route2login">登录</el-button>
            <el-button plain size="medium" @click="route2register">注册</el-button>
          </el-col>
        </el-row>
      </el-header>
      <el-main>
        <el-row>
            <br /><br />
            <br /><br />
            <br /><br />
            <br /><br />
            <el-button round style="width:35%;margin-bottom:15px;" @click="route2word">Word处理</el-button>
            <br /><br />
            <el-button round style="width:35%;margin-bottom:15px;" @click="route2pdf">Pdf处理</el-button>
            <br /><br />
            <el-button round style="width:35%;margin-bottom:15px;">待开发</el-button>
            <br /><br />
        </el-row>
      </el-main>
      <el-footer>
        Copyright &copy; 软件工程 - 2021. All rights reserved
      </el-footer>
    </el-container>
  </div>
</template>

<script>
  // import axios from 'axios'
  export default {
    name: "home",
  data() {
    return {
    };
  },
  methods: {
    route2login(){
      this.$router.push('/login')
    },
    route2register(){
      this.$router.push('/register')
    },
    route2help(){
      this.$router.push('/help')
    },
    route2word(){
      this.$router.push('/word')
    },
    route2pdf(){
      this.$router.push('/pdf')
    }
  }
  }
</script>


<style scope="this api replaced by slot-scope in 2.5.0+">
.home {
  height: 100%;
}

.title {
  background-color: #67bff1;
  width: 150px;
  padding-left: 30px;
}

.el-container {
  height: 100%;
  min-height: 100%;
  display: flex;
  flex-direction: column;
  justify-content:space-between;

}

.el-header {
  height: 60px;
  background-color: white;
  line-height: 60px;
  padding: 0!important;
}

.el-header > span,
.el-header .el-dropdown {
  font-size: 18px;
}

.el-footer { 
  background-color: #67bff1;
  color: #070707;
  text-align: center;
  line-height: 60px;
}

.el-main {
  color: rgb(7, 7, 7);
  min-height: calc(100vh - 130px);
  text-align: center;
}
</style>