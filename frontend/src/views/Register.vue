<template>
    <div class="login">
        <el-container>
            <el-header>
                <el-row :align="top">
                    <el-col :span="8">
                        <div class="title">EasyFile</div>
                    </el-col>
                    <div v-if="getState()">
                        <el-col
                            :span="16"
                            style="text-align: right; padding-right: 30px;"
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
                            <el-button plain size="medium" @click="route2help"
                                >关于</el-button
                            >
                            <el-button plain size="medium" @click="logout"
                                >注销</el-button
                            >
                            <el-button
                                plain
                                size="medium"
                                @click="route2history"
                                >个人主页</el-button
                            >
                            &#8194; 欢迎回来, {{ getName(initflag) }}!
                        </el-col>
                    </div>
                </el-row>
            </el-header>
            <el-main style="overflow:visible">
                <div id="login-container">
                    <div class="ms-title">注册</div>

                    <el-form
                        :model="param"
                        status-icon
                        :rules="rules"
                        ref="login"
                        label-width="100px"
                        class="demo-ruleForm"
                    >
                        <el-form-item label="昵称" prop="user">
                            <el-input
                                type="text"
                                v-model="param.nickname"
                                autocomplete="off"
                            ></el-input>
                        </el-form-item>

                        <el-form-item label="账号" prop="pass">
                            <el-input
                                type="text"
                                v-model="param.username"
                                autocomplete="off"
                            ></el-input>
                        </el-form-item>

                        <el-form-item label="密码" prop="pass">
                            <el-input
                                type="password"
                                v-model="param.password"
                                autocomplete="off"
                                show-password
                            ></el-input>
                        </el-form-item>

                        <el-form-item>
                            <el-button type="primary" @click="registerForm()"
                                >提交</el-button
                            >
                            <el-button @click="gotoLogin()">登录</el-button>
                        </el-form-item>
                    </el-form>
                </div>
            </el-main>
            <el-footer>
                Copyright &copy; 软件工程 - 2021. All rights reserved
            </el-footer>
        </el-container>
    </div>

</template>

<script>
// import axios from 'axios'
const sha256 = require("js-sha256").sha256;
export default {
    name: "register",
    data: function() {
        return {
            param: {
                username: "",
                password: "",
                email: "",
            },
            rules: {
                username: [
                    {
                        required: true,
                        message: "请输入用户名",
                        trigger: "blur",
                    },
                ],
                email: [
                    { required: true, message: "请输入邮箱", trigger: "blur" },
                ],
                password: [
                    { required: true, message: "请输入密码", trigger: "blur" },
                ],
            },
            initflag: 0,
            nickname: "",
            userID: 0,
        };
    },
    methods: {
        registerForm() {
            var post_request = new FormData();
            post_request.append("username", this.param.username);
            post_request.append("password", sha256(this.param.password));
            post_request.append("nickname", this.param.nickname);
            let _this = this;
            this.$axios
                .post("http://localhost:5000/auth/register", post_request, {
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded",
                    },
                })
                .then((response) => {
                    console.log(response);
                    if (response.data.state == 0) {
                        //alert("注册成功");
                        _this.$message({
                            message: response.data.info + "！请登录",
                            type: "success",
                        });
                        _this.$router.push("/login");
                    } else {
                        //alert(response.data.info);
                        _this.$message({
                            message: response.data.info,
                            type: "error",
                        });
                    }
                })
                .catch((response) => {
                    console.log(response);
                });
        },

        gotoLogin() {
            this.$router.replace("/login");
        },
        getState() {
            return (
                localStorage.getItem("accessToken") == null ||
                localStorage.getItem("accessToken") == ""
            );
        },
        getName(initflag) {
            if (!initflag) {
                this.$axios
                    .get("http://localhost:5000/homepage/", {
                        headers: {
                            Authorization:
                                "jwt " + localStorage.getItem("accessToken"),
                        },
                    })
                    .then((response) => {
                        console.log(response);
                        if (!response.data.state) {
                            this.userID = response.data.data.userID;
                            this.nickname = response.data.data.nickname;
                        } else {
                            console.log(response); //TODO
                        }
                    });
                this.initflag += 1;
            }
            return this.nickname;
        },
        route2login() {
            this.$router.push("/login");
        },
        route2register() {
            this.$router.push("/register");
        },
        route2help() {
            this.$router.push("/help");
        },
        route2word() {
            this.$router.push("/word");
        },
        route2pdf() {
            this.$router.push("/pdf");
        },
        route2history() {
            this.$router.push("/history");
        },
        logout() {
            localStorage.removeItem("accessToken");
            this.$router.push("/");
            window.location.reload();
        },
    },
};
</script>

<style scoped>
.login {
    background-color: rgb(255, 255, 255);
    height: 100%;
}

.title {
    background-color: #c7ede6;
    width: 150px;
    text-align: center;
}

.el-container {
    height: 100%;
    width: 100%;
    min-height: 500pt;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-width: 740pt;
    background-color: rgb(255, 255, 255);
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
    background-color: rgb(255, 255, 255);
    height: 100%;
    min-width: 740pt;
    text-align: center;
    margin-top: 80px;
}

.el-footer {
    background-color: #c7ede6;
    color: black;
    text-align: center;
    line-height: 60px;
    min-width: 740pt;
}
.ms-title {
    text-align: center;
    height: 50px;
}

#login-container {
    width: 400px;
    height: 290px;
    background: #d4ece7;
    position: absolute;
    left: 50%;
    top: 50%;
    margin-left: -220px;
    margin-top: -170px;
    border-radius: 5px;
    padding-top: 40px;
    padding-right: 40px;
}
</style>