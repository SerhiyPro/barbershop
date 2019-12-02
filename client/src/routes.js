import Vue from 'vue';
import Router from 'vue-router';
// import About from "@/components/About";
// import Header from "@/components/Header";
// import App from "@/App";
import AboutMore from "@/components/AboutMore";
import Home from "@/components/Home";
import Register from "@/components/Register";

Vue.use(Router)

export default new Router({
    mode: 'history',

    routes:[
        { path: '/', component: Home },
        { path: '/about', component: AboutMore },
        { path: '/register', component: Register },
    ]

});


