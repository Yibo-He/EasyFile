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

                <!--
      <a-menu-item key="login">
        <a href="/login" target="_blank" rel="noopener noreferrer">
        登录
        </a>
      </a-menu-item>

      <a-menu-item key="register">
        <a href="/register" target="_blank" rel="noopener noreferrer">
        注册
        </a>
      </a-menu-item>
    -->
            </a-menu>
        </div>

        <div id="login-container">
            <div class="ms-title">登录</div>

            <el-form
                :model="loginParam"
                status-icon
                :rules="rules"
                ref="loginParam"
                label-width="100px"
                class="demo-ruleForm"
            >
                <el-form-item label="账号" prop="user">
                    <el-input
                        type="text"
                        v-model="loginParam.username"
                        autocomplete="off"
                    ></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="pass">
                    <el-input
                        type="password"
                        v-model="loginParam.password"
                        autocomplete="off"
                        show-password
                    ></el-input>
                </el-form-item>

                <el-form-item>
                    <el-button type="primary" @click="submitForm('loginParam')"
                        >提交</el-button
                    >
                    <el-button @click="gotoReg()">注册</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script>
//import axios from "axios";
export default {
    name: "login",

    data() {
        return {
            loginParam: {
                user: "",
                pass: "",
            },
            rules: {
                username: [
                    {
                        required: true,
                        message: "请输入用户名",
                        trigger: "blur",
                    },
                ],
                password: [
                    { required: true, message: "请输入密码", trigger: "blur" },
                ],
            },
        };
    },

    methods: {
        submitForm(formName) {
            var post_request = new FormData();
            post_request.append("username", this.loginParam.username);
            post_request.append("password", this.loginParam.password);

            this.$axios
                .post("http://localhost:5000/auth/login", post_request, {
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded",
                    },
                })
                .then((response) => {
                    //document.write('line 107')
                    console.log(response);

                    if (response.data.state == 0) {
                        alert("登陆成功");

                        localStorage.setItem(
                            "ms_username",
                            this.loginParam.username
                        );
                        localStorage.setItem(
                            "accessToken",
                            response.data.tokenInfo["access_token"]
                        );
                        localStorage.setItem(
                            "refreshToken",
                            response.data.tokenInfo["refresh_token"]
                        );
                        localStorage.setItem(
                            "accessTokenExpiryTime",
                            response.data.tokenInfo["access_token_expire_in"]
                        );
                        localStorage.setItem(
                            "refreshTokenExpiryTime",
                            response.data.tokenInfo["refresh_token_expire_in"]
                        );
                        this.$router.push("/home");
                        this.$axios.defaults.headers["Authorization"] =
                            "jwt " + localStorage.getItem("accessToken");
                    } else {
                        alert("登陆失败");
                    }
                })
                .catch((response) => {
                    console.log(response);
                });
        },

        gotoReg() {
            this.$router.replace("/register");
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
    height: 290px;
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
