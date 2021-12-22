<template>
    <div class="home">
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
                <el-row>
                    <el-col :span="12" style>
                        <img
                            src="../assets/word-logo-q.png"
                            style="width: 320px; margin-top:80px; margin-left: 90px; margin-bottom: 70px"
                        />
                    </el-col>

                    <el-col :span="12">
                        <img
                            src="../assets/pdf-logo-q2.png"
                            style="width: 320px; margin-top:80px; margin-right: 90px; margin-bottom: 70px"
                        />
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="12" style>
                        <el-button
                            round
                            style="width:300px;padding:30px;margin-left: 90px;margin-bottom:80px;color:rgb(0, 60, 145);background-color:#fdfcef;border-color:rgb(0, 60, 145);"
                            @click="route2word"
                            >Word处理</el-button
                        >
                    </el-col>

                    <el-col :span="12">
                        <el-button
                            round
                            style="width:300px;padding:30px;margin-right: 90px;margin-bottom:80px;color:rgb(150, 40, 0);background-color:#fdfcef;border-color:rgb(150, 40, 0);"
                            @click="route2pdf"
                            >Pdf处理</el-button
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
// import axios from 'axios'
export default {
    name: "home",
    data() {
        return {
            initflag: 0,
            nickname: "",
            userID: 0,
        };
    },
    methods: {
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

<style scope>
.home {
    height: 100%;
    background-color: rgb(255, 255, 255);
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
}

.el-footer {
    background-color: #c7ede6;
    color: black;
    text-align: center;
    line-height: 60px;
    min-width: 740pt;
}
</style>
