<template>
    <div class="word">
        <el-container>
            <el-header>
                <el-row>
                    <el-col :span="8">
                        <div class="title">EasyFile</div>
                    </el-col>
                    <div v-if="getState()">
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
                            <el-button
                                plain
                                size="medium"
                                @click="route2register"
                                >注册</el-button
                            >
                        </el-col>
                    </div>
                    <div v-else>
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
                            <el-button plain size="medium" @click="logout"
                                >退出登录</el-button
                            >
                        </el-col>
                    </div>
                </el-row>
            </el-header>

            <!-- 
      action: 必选参数，上传的地址
    -->
            <el-main style="overflow:visible">
                <el-row>
                    <el-col :span="8" style="padding:50px">
                        <el-upload
                            class="upload-demo"
                            drag
                            action="http://localhost:5000/upload_file"
                            accept=".docx, application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                            :before-upload="onBeforeUpload"
                            multiple
                            :limit="10"
                            :headers="headerObj"
                            :on-success="save_fnames"
                            :file-list="fname_list"
                            :on-remove="remove_fnames"
                            :with-credentials="true"
                            style="background-color: #c7ede6; width: 400px; padding: 10px"
                        >
                            <img
                                src="../assets/word-logo-q2.png"
                                style="width: 150px; margin-top: 10px"
                            />
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
                        <el-button
                            type="primary"
                            style="background:rgb(50, 120, 220); border-color: rgb(50, 120, 220)"
                            @click="start"
                            >开始处理</el-button
                        >
                        <div>&emsp;</div>
                        <el-button
                            type="primary"
                            icon="el-icon-download"
                            style="background: rgb(50, 120, 220); border-color: rgb(50, 120, 220)"
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
            fpath_list: [],
            fname_list: [], //denote the files to be processed
            formatted_fname_list: [], //denote the processed files

            headerObj: {
                Authorization: "jwt " + localStorage.getItem("accessToken"),
            },

            options_color: [
                {
                    value: "_color",
                    label: "所有(转换前)/默认(转换后)",
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
                    label: "所有(转换前)/默认(转换后)",
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
                { value: 0, label: "所有(转换前)/默认(转换后)" },
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
        getState() {
            return (
                localStorage.getItem("accessToken") == null ||
                localStorage.getItem("accessToken") == ""
            );
        },
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
        logout() {
            localStorage.removeItem("accessToken");
            window.location.reload();
        },

        download() {
            for (var i = 0; i < this.formatted_fname_list.length; i++) {
                console.log(this.formatted_fname_list[i]);
                const filename = this.formatted_fname_list[i].split(
                    "-(&EF&)-"
                )[2];
                this.$axios
                    .get(
                        "http://localhost:5000/download/" +
                            this.formatted_fname_list[i],
                        {
                            headers: {
                                Authorization:
                                    "jwt " +
                                    localStorage.getItem("accessToken"),
                            },
                            responseType: "blob",
                        }
                    )
                    .then((response) => {
                        if (!response) {
                            return;
                        }
                        console.log(response.headers["content-type"]);
                        if (
                            response.headers["content-type"] ===
                            "application/json"
                        ) {
                            this.$message.error("下载列表为空或无下载权限!");
                            return;
                        }
                        const url = window.URL.createObjectURL(response.data);
                        const link = document.createElement("a");
                        link.style.display = "none";
                        link.href = url;
                        link.setAttribute("download", filename);
                        document.body.appendChild(link);
                        link.click();
                    })
                    .catch();
            }
            this.formatted_fname_list = [];
        },

        save_fnames(response) {
            console.log(response);
            for (var i = 0; i < response.length; i++) {
                if (response[i].state == 0) {
                    this.fname_list.push(
                        response[i].filename.split("-(&EF&)-")[2]
                    );
                    this.fpath_list.push(response[i].filename);
                    console.log(this.fname_list);
                } else {
                    alert(response[i].info);
                }
            }
        },

        remove_fnames(file, fileList) {
            console.log(file.name);
            this.fname_list.splice(this.fname_list.indexOf(file.name), 1);
        },

        onBeforeUpload(file) {
            console.log(file.type);
            const isDoc =
                file.type ===
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document";
            const isLt10M = file.size / 1024 / 1024 < 10;

            if (!isDoc) {
                this.$message.error("上传文件只能是docx文档格式!");
            }
            if (!isLt10M) {
                this.$message.error("上传文件大小不能超过 10MB!");
            }
            return isDoc && isLt10M;
        },

        start() {
            //console.log('line 245');
            var post_request = new FormData();
            post_request.append("file_names", this.fpath_list.join(","));

            post_request.append("src_str", this.string_before);
            if (this.font_style_before == "") {
                this.font_style_before = "_style";
            }
            post_request.append("src_typeface", this.font_style_before);
            if (this.font_size_before == "") {
                this.font_size_before = 0;
            }
            post_request.append("src_size", this.font_size_before);
            if (this.color_before == "") {
                this.color_before = "_color";
            }
            post_request.append("src_color", this.color_before);

            post_request.append("dst_str", this.string_after);
            if (this.font_style_after == "") {
                this.font_style_after = "_style";
            }
            post_request.append("dst_typeface", this.font_style_after);
            if (this.font_size_after == "") {
                this.font_size_after = 0;
            }
            post_request.append("dst_size", this.font_size_after);
            if (this.color_after == "") {
                this.color_after = "_color";
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
                    this.fpath_list = [];
                })
                .catch((response) => {
                    console.log(response);
                });
        },
    },
};
</script>

<style scoped>
.word {
    height: 100%;
}
.title {
    background-color: #78a0cf;
    width: 150px;
    text-align: center;
}

.el-container {
    min-width: 1100pt;
}

.el-header {
    height: 60px;
    color: white;
    line-height: 60px;
    padding: 0 !important;
    min-width: 1100pt;
}

.el-main {
    margin-top: 60px;
    min-width: 1100pt;
}

.el-footer {
    background-color: #78a0cf;
    color: white;
    text-align: center;
    line-height: 60px;
    min-width: 1100pt;
}
</style>
