<template>
    <section id="services" class="service-area section-gap">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-12 text-center">
                    <div class="section-title">
                        <h1>Що ми можемо зробити для вас</h1>
                        <p>Потрібен весільний макіяж для головного свята в житті? Душа бажає нового яскравого манікюру? Ніяких проблем – звертайтеся до нас!</p>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-3 col-sm-6 col-md-3" v-for="(obj,key) in serviceJSON" :key="key">
                    <div class="single-service">
                        <img class="img-fluid" :src="obj.img" alt="">
                        <h4>{{obj.title}}</h4>
                    </div>
                </div>
            </div>
        </div>
    </section>

</template>

<script>
    export default {
        name: "Services",
        data:()=>({
            serviceJSON:[
                {
                    img:require('@/assets/img/services1.jpg'),
                    title:'SPA Процедури'
                },
                {
                    img:require('@/assets/img/services2.jpg'),
                    title:'Візажист'
                },
                {
                    img:require('@/assets/img/services3.jpg'),
                    title:'Нарощування Вій'
                },
                {
                    img:require('@/assets/img/services4.jpg'),
                    title:'Косметологія'
                },
            ]
        })
    }
</script>

<style scoped>

</style>
