<template>
    <div>
        <div>
            <a-menu
                v-model="current"
                mode="horizontal"
                style="text-align: right"
            >
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
        </div>

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
                .post("http://39.104.16.83:3001/auth/register", post_request, {
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
    },
};
</script>

<style scoped>
.ms-title {
    text-align: center;
    height: 50px;
}
body {
    margin: 0;
}
#login-container {
    width: 400px;
    height: 350px;
    background: #e5e9f2;
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
