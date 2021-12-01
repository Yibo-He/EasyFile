<template>
    <div>
        <el-container>
            <el-header>
                <el-row>
                    <el-col :span="8">
                        <div class="title">EasyFile</div>
                    </el-col>
                    <el-col
                        :span="16"
                        style="text-align: right; padding-right: 30px;"
                    >
                        <el-button plain size="medium" @click="route2home"
                            >首页</el-button
                        >
                        <el-button plain size="medium" @click="route2help"
                            >关于</el-button
                        >
                        <el-button plain size="medium" @click="route2login"
                            >登录</el-button
                        >
                        <el-button plain size="medium" @click="route2register"
                            >注册</el-button
                        >
                    </el-col>
                </el-row>
            </el-header>

            <!-- 
      action: 必选参数，上传的地址
    -->
            <el-main>
                <el-row>
                    <el-col :span="8" style="padding-top: 100px">
                        <el-upload
                            class="upload-demo"
                            drag
                            action="http://localhost:5000/upload_doc"
                            multiple
                            :headers="headerObj"
                            :on-success="save_fnames"
                            :with-credentials="true"
                            style="background: rgba(128,128,128,.5); padding: 10px"
                        >
                            <i class="el-icon-upload"></i>
                            <div class="el-upload__text">
                                将文件拖到此处，或<em>点击上传</em>
                            </div>
                            <div class="el-upload__tip" slot="tip">
                                注意: 只能上传doc/docx文件
                            </div>
                        </el-upload>
                    </el-col>

                    <el-col :span="16">
                        <el-row>
                            <el-col :span="10">
                                <div style="font-size: 1.5em">转换前</div>
                                <br />
                                <el-input
                                    v-model="string_before"
                                    placeholder="转换前的字符串"
                                ></el-input
                                ><br /><br />

                                <el-select
                                    v-model="color_before"
                                    clearable
                                    placeholder="字体颜色"
                                >
                                    <el-option
                                        v-for="item in options_color"
                                        :key="item.value"
                                        :label="item.label"
                                        :value="item.value"
                                    >
                                    </el-option> </el-select
                                ><br /><br />

                                <el-select
                                    v-model="font_style_before"
                                    clearable
                                    placeholder="字体样式"
                                >
                                    <el-option
                                        v-for="item in options_font_style"
                                        :key="item.value"
                                        :label="item.label"
                                        :value="item.value"
                                    >
                                    </el-option> </el-select
                                ><br /><br />

                                <el-select
                                    v-model="font_size_before"
                                    clearable
                                    placeholder="字体大小"
                                >
                                    <el-option
                                        v-for="item in options_size"
                                        :key="item.value"
                                        :label="item.label"
                                        :value="item.value"
                                    >
                                    </el-option> </el-select
                                ><br /><br />
                            </el-col>

                            <el-col :span="10" offset="4">
                                <div style="font-size: 1.5em">转换后</div>
                                <br />
                                <el-input
                                    v-model="string_after"
                                    placeholder="请输入转换后的字符串"
                                ></el-input
                                ><br /><br />

                                <el-select
                                    v-model="color_after"
                                    clearable
                                    placeholder="字体颜色"
                                >
                                    <el-option
                                        v-for="item in options_color"
                                        :key="item.value"
                                        :label="item.label"
                                        :value="item.value"
                                    >
                                    </el-option> </el-select
                                ><br /><br />

                                <el-select
                                    v-model="font_style_after"
                                    clearable
                                    placeholder="字体样式"
                                >
                                    <el-option
                                        v-for="item in options_font_style"
                                        :key="item.value"
                                        :label="item.label"
                                        :value="item.value"
                                    >
                                    </el-option> </el-select
                                ><br /><br />

                                <el-select
                                    v-model="font_size_after"
                                    clearable
                                    placeholder="字体大小"
                                >
                                    <el-option
                                        v-for="item in options_size"
                                        :key="item.value"
                                        :label="item.label"
                                        :value="item.value"
                                    >
                                    </el-option> </el-select
                                ><br /><br />
                            </el-col>
                        </el-row>

                        <br />
                        <el-button type="primary" @click="start"
                            >开始处理</el-button
                        >
                        <div>&emsp;</div>
                        <el-button
                            type="primary"
                            icon="el-icon-download"
                            round
                            size="medium"
                            @click="download"
                            >下载处理后文件</el-button
                        >
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
    name: "word",
    data() {
        return {
            string_before: "",
            color_before: "",
            font_style_before: "",
            font_size_before: "",
            string_after: "",
            color_after: "",
            font_style_after: "",
            font_size_after: "",
            fname_list: [], //denote the files to be processed
            formatted_fname_list: [], //denote the processed files

            headerObj: {
                Authorization: "jwt " + localStorage.getItem("accessToken"),
            },

            options_color: [
                {
                    value: "_color",
                    label: "-(所有)",
                },
                {
                    value: "000000",
                    label: "黑色",
                },
                {
                    value: "ff0000",
                    label: "红色",
                },
                {
                    value: "00ff00",
                    label: "绿色",
                },
                {
                    value: "0000ff",
                    label: "蓝色",
                },
                {
                    value: "ffff00",
                    label: "黄色",
                },
                {
                    value: "ffffff",
                    label: "白色",
                },
            ],

            options_font_style: [
                {
                    value: "_style",
                    label: "-(所有)",
                },
                {
                    value: "宋体",
                    label: "宋体",
                },
                {
                    value: "黑体",
                    label: "黑体",
                },
                {
                    value: "等线",
                    label: "等线",
                },
                {
                    value: "楷体",
                    label: "楷体",
                },
                {
                    value: "Times New Roman",
                    label: "Times New Roman",
                },
                {
                    value: "微软雅黑",
                    label: "微软雅黑",
                },
            ],

            options_size: [
                { value: 0, label: "-(所有)" },
                { value: 42, label: "初号" },
                { value: 36, label: "小初" },
                { value: 26, label: "一号" },
                { value: 24, label: "小一" },
                { value: 22, label: "二号" },
                { value: 18, label: "小二" },
                { value: 16, label: "三号" },
                { value: 15, label: "小三" },
                { value: 14, label: "四号" },
                { value: 12, label: "小四" },
                { value: 10.5, label: "五号" },
                { value: 9, label: "小五" },
                { value: 7.5, label: "六号" },
                { value: 6.5, label: "小六" },
            ],
        };
    },

    methods: {
        route2home() {
            this.$router.replace("/");
        },
        route2login() {
            this.$router.replace("/login");
        },
        route2register() {
            this.$router.replace("/register");
        },
        route2help() {
            this.$router.replace("/help");
        },
        route2word() {
            this.$router.replace("/word");
        },
        route2pdf() {
            this.$router.replace("/pdf");
        },
        download() {
            //console.log('line 230')
            //console.log(this.formatted_fname_list)
            for (var i = 0; i < this.formatted_fname_list.length; i++) {
                console.log(this.formatted_fname_list[i]);
                this.$axios
                    .get(
                        "http://localhost:5000/download/" +
                            this.formatted_fname_list[i],
                        {
                            responseType: "blob",
                            headers: {
                                Authorization:
                                    "jwt " +
                                    localStorage.getItem("accessToken"),
                            },
                        }
                    )
                    .then((response) => {
                        if (!response) {
                            return;
                        }
                        const filename = this.formatted_fname_list[i];
                        const url = window.URL.createObjectURL(response.data);
                        const link = document.createElement("a");
                        link.style.display = "none";
                        link.href = url;
                        link.setAttribute("download", filename);
                        document.body.appendChild(link);
                        link.click();
                    })
                    .catch();

                this.formatted_fname_list = [];
            }
        },

        save_fnames(response) {
            console.log(response);
            for (var i = 0; i < response.length; i++) {
                if (response[i].state == 0) {
                    this.fname_list.push(response[i].filename);
                    console.log(this.fname_list);
                    //console.log('['+this.fname_list.join(',')+']')
                } else {
                    alert(response[i].info);
                }
            }
        },
        start() {
            //console.log('line 245');
            var post_request = new FormData();
            post_request.append("file_names", this.fname_list.join(","));
            post_request.append("src_str", this.string_before);
            if (this.font_style_before == "_style") {
                this.font_style_before = "";
            }
            post_request.append("src_typeface", this.font_style_before);
            post_request.append("src_size", this.font_size_before);
            if (this.color_before == "_color") {
                this.color_before = "";
            }
            post_request.append("src_color", this.color_before);
            post_request.append("dst_str", this.string_after);
            if (this.font_style_after == "_style") {
                this.font_style_after = "";
            }
            post_request.append("dst_typeface", this.font_style_after);
            post_request.append("dst_size", this.font_size_after);
            if (this.color_after == "_color") {
                this.color_after = "";
            }
            post_request.append("dst_color", this.color_after);

            //TODO: add requirements
            let _this = this;
            this.$axios
                .post("http://localhost:5000/run_formatter", post_request, {
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded",
                        Authorization:
                            "jwt " + localStorage.getItem("accessToken"),
                    },
                })
                .then((response) => {
                    //console.log('line 256');
                    console.log(response);
                    for (var i = 0; i < response.data.length; i++) {
                        /*this.$message({
                    message: response.data[i].info+'\torigin_name:'+response.data[i].original_name+'\tformatted_name:'+response.data[i].formatted_name,
                  });*/
                        this.formatted_fname_list.push(
                            response.data[i].formatted_name
                        );
                        this.$message({ message: "处理完成！" });
                    }
                    this.fname_list = [];
                })
                .catch((response) => {
                    console.log(response);
                });
        },
    },
};
</script>

<style scoped>
.title {
    background-color: #67bff1;
    width: 150px;
    padding-left: 30px;
}

.el-main {
    color: rgb(7, 7, 7);
    min-height: calc(100vh - 320px);
    text-align: center;
    margin: 100px 20px;
}
</style>
