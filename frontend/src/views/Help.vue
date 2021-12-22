<template>
  <div class="help">
    <el-container>
      <el-header>
        <el-row>
          <el-col :span="8">
            <div class='title'>EasyFile</div>
          </el-col>
          <el-col :span="16" style="text-align: right; padding-right: 30px;">
            <el-button plain size="medium" @click="route2home">首页</el-button>
          </el-col>
        </el-row>
      </el-header>
      <el-main style="overflow:visible;">
        <el-row>
          <el-col :span="10" offset="1">
            <el-card :body-style="{ padding: '0px' }">
              <img src="../assets/word-logo1.png" class="image">
              <div style="padding: 14px;">
                <span>Word处理</span>
                <div class="bottom clearfix">
                  <el-button type="text" class="button" @click="route2word">现在体验</el-button>
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col :span="10" offset="2">
            <el-card :body-style="{ padding: '0px' }">
              <img src="../assets/pdf-logo1.png" class="image">
              <div style="padding: 14px;">
                <span>Pdf处理</span>
                <div class="bottom clearfix">
                  <el-button type="text" class="button" @click="route2pdf">现在体验</el-button>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
      <el-footer>
        Copyright &copy; 软件工程 - 2021. All rights reserved
      </el-footer>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: "help",
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
.help {
    height: 100%;
    background-color: rgb(255,255,255);
}
.title {
  background-color: #c7ede6;
  width: 150px;
  padding-left: 45px;
}

.el-container {
    height: 100%;
    width: 100%;
    min-height: 500pt;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-width: 740pt;
}

.el-header {
    height: 60px;
    background-color: #fdfcef;
    color: black;
    line-height: 60px;
    padding: 0 !important;
    min-width: 740pt;
}

/* .el-header > span,
.el-header .el-dropdown {
  font-size: 18px;
} */

.el-main {
    color: rgb(7, 7, 7);
    height: 100%;
    min-width: 700pt;
    margin: 50px 20px;
    text-align: center;
}

.el-footer {
    background-color: #c7ede6;
    color: black;
    text-align: center;
    line-height: 60px;
    min-width: 740pt;
}

  .time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }
</style>