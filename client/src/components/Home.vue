<template>
    <div>
    <div class="hero">
        <div class="container">
            <div class="hero-cont col-7">
                <div class="offer">
                    <h1 class="offer__title">Салон Краси La Rose</h1>
                    <p class="offer__text">
                        Наші майстри беруть на себе всі турботи і складні завдання у сфері краси та догляду за собою. Потрібен весільний макіяж для головного свята в житті? Душа бажає нового яскравого манікюру? Ніяких проблем – звертайтеся до нас!
                    </p>
                    <router-link to="/register" class="primary-btn">Записатись Онлайн</router-link>
                </div>
                <div class="stats d-flex justify-content-between align-items-center">
                    <p class="stats__item">Сертифіковані <br> косметологи</p>
                    <p class="stats__item">Результат після<br> першої процедури</p>
                    <p class="stats__item">Без уколів <br> та ін'єкцій</p>
                </div>
            </div>
        </div>
    </div>

    <!-- / Hero -->



    <!-- About -->

    <About>
    </About>
    <!-- / About -->



    <!-- Services -->

    <Services></Services>
    <!-- / Services -->



    <!-- Team -->

    <Team></Team>
    <!-- / Team -->



    <!-- Testimonials -->

<Testimonial></Testimonial>
    <!-- / Testimonials -->


    </div>
</template>

<script>

    import About from "@/components/About";
    import Services from "@/components/Services";
    import Team from "@/components/Team";
    import Testimonial from "@/components/Testimonial";
    export default {
        name: 'Home',
        components: {
            Testimonial,
            Team,
            Services,
            About,

        },

    }
</script>


<style scoped>

</style>
