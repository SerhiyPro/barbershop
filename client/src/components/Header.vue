<template>
    <header id="header" class="header header-fixed">
        <div class="container">
            <div class="nav navbar-expand-lg">
                <div class="logo col-2">
                    <a href="">
                        <img src="../assets/img/logo.png" alt="La Rose">
                    </a>
                </div>
                <div class="menu col-7">

                    <router-link to="/">Головна</router-link>
                    <router-link to="/about">Про нас</router-link>
                    <a href="#services">Послуги</a>
                    <a href="#team">Працівники</a>
                </div>
<!--                <router-view></router-view>-->

                <div class="col-3 ml-auto menu-tel">
                    <a href="tel:380993568581" class="tel">
                        <i class="fas fa-phone-alt"></i>
                        <p>+380 99 356 8581</p>
                    </a>
                </div>

                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
                    <span class="burger-menu__line"></span>
                    <span class="burger-menu__line"></span>
                    <span class="burger-menu__line"></span>
                </button>

            </div>

        </div>
    </header>

</template>

<script>
    export default {
        name: "Header",

    }
</script>

<style scoped>

</style>
