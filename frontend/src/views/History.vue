<template>
    <div class="history">
        <el-container>
            <el-header>
                <el-row :align="top">
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
                        <el-button plain size="medium" @click="logout"
                            >注销</el-button
                        >
                    </el-col>
                </el-row>
            </el-header>
            <el-main style="overflow:visible">
                <el-table
                    :data="
                        gettableData(initflag).slice(
                            (currentPage - 1) * pagesize,
                            currentPage * pagesize
                        )
                    "
                    :current-page.sync="currentPage"
                    style="width: 100%"
                >
                    <el-table-column
                        type="index"
                        :index="indexMethod"
                        width="50"
                    >
                    </el-table-column>
                    <el-table-column
                        :prop="item.porp"
                        :label="item.label"
                        width="400"
                        v-for="item in dataprop"
                        :key="item.key"
                    >
                    </el-table-column>
                    <el-table-column align="right">
                        <template slot-scope="scope">
                            <el-button
                                size="mini"
                                @click="handleDownload(scope.row)"
                                >下载
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>
                <el-pagination
                    @current-change="handleCurrentChange"
                    :page-size="pagesize"
                    layout="total, prev, pager, next, jumper"
                    :total="total"
                >
                </el-pagination>
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
    name: "history",
    data() {
        return {
            dataprop: [
                { label: "时间", porp: "timestamp" },
                { label: "文件名", porp: "filename" },
                { label: "处理类型", porp: "processor" },
            ],
            tableData: [],
            currentPage: 1,
            pagesize: 10,
            total: 0,
            userID: 0,
            nickname: "",
            initflag: 0,
        };
    },
    methods: {
        logout() {
            localStorage.removeItem("accessToken");
            this.$router.push("/");
        },
        route2home() {
            this.$router.push("/");
        },
        indexMethod(index) {
            return index + 10 * (this.currentPage - 1) + 1;
        },
        handleCurrentChange(val) {
            this.currentPage = val;
        },
        gettableData(initflag) {
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
                            this.$axios
                                .get(
                                    "http://localhost:5000/homepage/history_file/0",
                                    {
                                        headers: {
                                            Authorization:
                                                "jwt " +
                                                localStorage.getItem(
                                                    "accessToken"
                                                ),
                                        },
                                    }
                                )
                                .then((response) => {
                                    console.log(response);
                                    if (!response.data.state) {
                                        this.tableData = response.data.data;
                                        this.total = this.tableData.length;
                                    } else {
                                        console.log(response); //TODO
                                    }
                                });
                        } else {
                            console.log(response); //TODO
                        }
                    });
                this.initflag += 1;
            }
            return this.tableData;
        },
        handleDownload(row) {
            // console.log(row);
            this.$axios
                .get("http://localhost:5000/download/" + row.path, {
                    headers: {
                        Authorization:
                            "jwt " + localStorage.getItem("accessToken"),
                    },
                    responseType: "blob",
                })
                .then((response) => {
                    const filename = row.filename;
                    const url = window.URL.createObjectURL(
                        new Blob([response.data])
                    );
                    const link = document.createElement("a");
                    link.style.display = "none";
                    link.href = url;
                    link.setAttribute("download", filename);
                    document.body.appendChild(link);
                    link.click();
                })
                .catch();
        },
    },
};
</script>

<style scope>
.history {
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
    min-width: 1030pt;
}

.el-header {
    height: 60px;
    background-color: #fdfcef;
    color: black;
    line-height: 60px;
    padding: 0 !important;
    min-width: 1030pt;
}

/* .el-header > span,
.el-header .el-dropdown {
  font-size: 18px;
} */

.el-main {
    color: rgb(7, 7, 7);
    height: 100%;
    min-width: 1030pt;
    text-align: center;
}

.el-footer {
    background-color: #c7ede6;
    color: black;
    text-align: center;
    line-height: 60px;
    min-width: 1030pt;
}
</style>
