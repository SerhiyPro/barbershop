<template>


    <section class="about">
        <div class="container">
            <div class="single-about row align-items-center">
                <div class="col-lg-4 col-md-6 no-padding about-left">
                    <div class="about-content">
                        <h1>
                            Про салон краси La Rose
                        </h1>
                        <p>Салон краси La Rose у Чернівцях належить до числа ексклюзивних експерт-салонів "Loreal Salon Expert" i відзначається високою професійністю майстрів та використанням у роботі креативних ідей.</p>
                        <router-link to="/about" class="btn-o">Дізнатись більше</router-link>
                    </div>
                </div>
                <div class="col-lg-7 col-md-6 text-center no-padding about-right">
                    <div class="about-thumb">
                        <img src="img/about1.jpg" class="img-fluid info-img" alt="">
                    </div>
                </div>
                <div class="bordered-img">
                    <img src="img/about2.jpg" class="img-fluid info-img" alt="">
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    export default {
        name: "About"
    }
</script>

<style scoped>

</style>
