<template>
    <section id="team" class="team-area">
        <div class="container" style="overflow-x: hidden;">
            <div class="row justify-content-center">
                <div class="col-md-12 text-center">
                    <div class="section-title">
                        <h1>В нас працюють професіонали</h1>
                        <p>Потрібен весільний макіяж для головного свята в житті? Душа бажає нового яскравого манікюру?
                            Ніяких проблем – звертайтеся до нас!</p>
                    </div>
                </div>
            </div>
            <div class="row sl">
                <carousel :autoplay="true" :items="3" :dots="false" :nav="false" :navText="false">
                    <div v-for="(obj,key) in teamJSON " :key=key>
                        <div class="col team__person">
                            <div class="single-team-member">
                                <div class="member-img">
                                    <img class="img-fluid" :src="obj.img" alt="">
                                </div>
                                <div class="proff">
                                    <h4>{{obj.name}}</h4>
                                    <p>{{obj.specialty}}</p>
                                </div>
                            </div>
                        </div>
                    </div>

                </carousel>

            </div>
        </div>
    </section>

</template>

<script>
    import carousel from 'vue-owl-carousel'

    export default {
        components: {carousel},
        name: "Team",
        data: () => ({
            teamJSON: [
                {
                    img: require('@/assets/img/team1.jpg'),
                    name: 'Ольга Світлакова',
                    specialty: 'КОСМЕТОЛОГ'
                },
                {
                    img: require('@/assets/img/team1.jpg'),
                    name: 'Ольга Світлакова',
                    specialty: 'КОСМЕТОЛОГ'
                },
                {
                    img: require('@/assets/img/team1.jpg'),
                    name: 'Ольга Світлакова',
                    specialty: 'КОСМЕТОЛОГ'
                },
                {
                    img: require('@/assets/img/team1.jpg'),
                    name: 'Ольга Світлакова',
                    specialty: 'КОСМЕТОЛОГ'
                },
                {
                    img: require('@/assets/img/team1.jpg'),
                    name: 'Ольга Світлакова',
                    specialty: 'КОСМЕТОЛОГ'
                },
                {
                    img: require('@/assets/img/team1.jpg'),
                    name: 'Ольга Світлакова',
                    specialty: 'КОСМЕТОЛОГ'
                },

            ]
        })
    }


</script>

<style scoped>

</style>
