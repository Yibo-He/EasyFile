import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";

import VueParticles from "vue-particles";
import axios from "axios";
axios.defaults.withcredentials = true;
Vue.prototype.$axios = axios;

Vue.use(VueParticles);
Vue.use(ElementUI);

Vue.config.productionTip = false;

new Vue({
    router,
    store,
    render: (h) => h(App),
}).$mount("#app");