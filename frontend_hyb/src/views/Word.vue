<template>
<div>

  <el-container>
    <el-header>
        <el-row>
          <el-col :span="8">
            <div class='title'>EasyFile</div>
          </el-col>
          <el-col :span="16" style="text-align: right; padding-right: 30px;">
            <el-button plain size="medium" @click="route2home">首页</el-button>
            <el-button plain size="medium" @click="route2help">关于</el-button>
            <el-button plain size="medium" @click="route2login">登录</el-button>
            <el-button plain size="medium" @click="route2register">注册</el-button>
          </el-col>
        </el-row>
      </el-header>


    <!-- 
      action: 必选参数，上传的地址
    -->
    <el-main>
      <el-row >

      <el-col :span="8" style="padding-top: 100px">
      <el-upload
        class="upload-demo"
        drag
        action="https://jsonplaceholder.typicode.com/posts/"
        multiple>
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        <div class="el-upload__tip" slot="tip">注意: 只能上传doc/docx文件</div>
      </el-upload>
      </el-col>

      <el-col :span="16">
        <el-row >
          <el-col :span="10">
            <div style="font-size: 1.5em">转换前 </div><br />
            <el-input v-model="string_before" placeholder="转换前的字符串"></el-input><br /><br />

            <el-select v-model="color_before" clearable placeholder="字体颜色">
              <el-option
                v-for="item in options_color"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select><br /><br />

            <el-select v-model="font_style_before" clearable placeholder="字体样式">
              <el-option
                v-for="item in options_font_style"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select><br /><br />

            <el-select v-model="font_size_before" clearable placeholder="字体大小">
              <el-option
                v-for="item in options_size"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select><br /><br />

          </el-col>

          <el-col :span="10" offset="4">
            <div style="font-size: 1.5em">转换后 </div><br />
            <el-input v-model="string_after" placeholder="请输入转换后的字符串"></el-input><br /><br />

            <el-select v-model="color_after" clearable placeholder="字体颜色">
              <el-option
                v-for="item in options_color"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select><br /><br />

            <el-select v-model="font_style_after" clearable placeholder="字体样式">
              <el-option
                v-for="item in options_font_style"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select><br /><br />

            <el-select v-model="font_size_after" clearable placeholder="字体大小">
              <el-option
                v-for="item in options_size"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select><br /><br />

          </el-col>
        </el-row>

        <br />
        <el-button type="primary" @click="start">开始处理</el-button>
      </el-col>

      </el-row>

      <br /><br />
      <el-button type="primary" icon="el-icon-download" round size="medium" @click="download">下载处理后文件</el-button>

    </el-main>

    <el-footer>
      Copyright &copy; 软件工程 - 2021. All rights reserved
    </el-footer>
  </el-container>

</div>
</template>

<script>
  export default {
    name: "word",
    data(){
      return {
        string_before: '',
        color_before: '',
        font_style_before: '',
        font_size_before: '',
        string_after: '',
        color_after: '',
        font_style_after: '',
        font_size_after: '',

        options_color: [{
          value: '0',
          label: '-(所有)'
        }, {
          value: '1',
          label: '黑色'
        }, {
          value: '2',
          label: '红色'
        }, {
          value: '3',
          label: '绿色'
        }, {
          value: '4',
          label: '蓝色'
        },{
          value: '5',
          label: '黄色'
        },{
          value: '6',
          label: '白色'
        }],

        options_font_style: [{
          value: '0',
          label: '-(所有)'
        }, {
          value: '1',
          label: '宋体'
        }, {
          value: '2',
          label: '黑体'
        }, {
          value: '3',
          label: '等线'
        }, {
          value: '4',
          label: '楷体'
        },{
          value: '5',
          label: 'Times New Roman'
        },{
          value: '6',
          label: '微软雅黑'
        }],

        options_size: [
        {value: '0', label: '-(所有)'}
        ,{ value: '1', label: '初号'}
        ,{ value: '2', label: '小初'}
        ,{ value: '3', label: '一号'}
        ,{ value: '4', label: '小一'}
        ,{ value: '5', label: '二号'}
        ,{ value: '6', label: '小二'}
        ,{ value: '7', label: '三号'}
        ,{ value: '8', label: '小三'}
        ,{ value: '9', label: '四号'}
        ,{ value: '10', label: '小四'}
        ,{ value: '11', label: '五号'}
        ,{ value: '12', label: '小五'}
        ,{ value: '13', label: '六号'}
        ,{ value: '14', label: '小六'}
        ],

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

.el-main {
  color: rgb(7, 7, 7);
  text-align: center;
  margin: 20px 50px;
  padding: 70px 50px;
}

</style>
