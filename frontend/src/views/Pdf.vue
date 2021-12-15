<template>
    <div class="pdf">
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
                        <el-button plain size="medium" @click="route2register"
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

            <el-main style="overflow:visible">
                <el-row>
                    <el-col :span="24" align="middle" style="padding: 20px">
                        <el-upload
                            class="upload-demo"
                            drag
                            action="http://localhost:5000/upload_file"
                            multiple
                            :headers="headerObj"
                            :on-success="save_fnames"
                            :with-credentials="true"
                            style="background-color: #f0c8cd; width: 500px; padding: 20px; margin-left:40px"
                        >
                            <img
                                src="../assets/pdf-logo-q.png"
                                style="width: 150px;margin-top: 5px"
                            />
                            <div class="el-upload__text">
                                将文件拖到此处，或<em style="color: #eb3f3f"
                                    >点击上传</em
                                >
                            </div>
                            <div class="el-upload__tip" slot="tip">
                                注意: 只能上传pdf文件
                            </div>
                        </el-upload>
                    </el-col>

                    <el-col :span="24" align="middle" style="padding: 20px">
                        <br /><br />
                        <el-select
                            v-model="functionality"
                            placeholder="请选择PDF处理功能"
                            style="margin-left:50px"
                        >
                            <el-option
                                v-for="item in func_options"
                                :key="item.value"
                                :label="item.label"
                                :value="item.value"
                                :disabled="item.disabled"
                            >
                            </el-option>
                        </el-select>
                        <br /><br />

                        <el-input
                            v-model="pages"
                            placeholder="请输入处理的页码，例如1-5、8、11-13"
                            style="width: 400px; margin-left: 50px"
                        ></el-input>
                        <br /><br />

                        <el-button
                            type="primary"
                            style="background: #e93b50; border-color: #eb3f3f; margin-left: 50px"
                            @click="start_pdf"
                            >开始处理</el-button
                        >
                        <div>&emsp;</div>
                        <el-button
                            type="primary"
                            style="background: #e93b50; border-color: #eb3f3f; margin-left: 50px"
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
    name: "pdf",
    data() {
        return {
            functionality: "",
            pages: "",
            fname_list: [], //denote the files to be processed
            formatted_fname_list: [], //denote the processed files

            headerObj: {
                Authorization: "jwt " + localStorage.getItem("accessToken"),
            },

            func_options: [
                {
                    value: "表格提取",
                    label: "表格提取",
                },
                {
                    value: "待开发",
                    label: "待开发",
                    disabled: true,
                },
            ],
        };
    },

    methods: {
        getState(){
            return localStorage.getItem('accessToken') == null || localStorage.getItem('accessToken') == '';
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
        logout(){
            localStorage.removeItem('accessToken');
            window.location.reload();
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
            }
            this.formatted_fname_list = [];
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
        start_pdf() {
            //console.log('line 245');
            var post_request = new FormData();
            post_request.append("file_names", this.fname_list.join(","));

            post_request.append("src_func", this.functionality);
            post_request.append("src_pages", this.pages);

            //TODO: add requirements
            let _this = this;
            this.$axios
                .post("http://localhost:5000/run_pdf2chart", post_request, {
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
.pdf {
    height: 100%;
}

.el-header {
    height: 60px;
    color: white;
    line-height: 60px;
    padding: 0 !important;
}

.title {
    background-color: #f15b6c;
    width: 150px;
    text-align: center;
}

.el-footer {
    background-color: #f15b6c;
    color: white;
    text-align: center;
    /* margin-top: -60px; */
    line-height: 60px;
}
</style>
