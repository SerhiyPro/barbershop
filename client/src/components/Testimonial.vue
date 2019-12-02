<template>
    <div>
    <section class="testimonials-area section-gap-top">
        <div class="overlay overlay-bg"></div>
        <div class="container">
            <div class="text-center">
                <img class="quote-img" src="img/quote.png" alt="">
            </div>

            <div class="testi-slider">
                <div class="item">
                    <carousel :autoplay="true" :items="1" :dots="false" :nav="false" :navText="false">
                        <div class="testi-item">
                            <h4>Оксана Білик</h4>
                            <ul class="list">
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                            </ul>
                            <div class="wow fadeIn" data-wow-duration="1s">
                                <p>
                                    Очень приятный салон! Хожу сюда на чистку лица и маникюр.
                                    Мастера хорошие, умеют работать с кожей. Атмосфера приятная,
                                    помогает расслабиться. Салоном очень довольна, приятное место
                                </p>
                            </div>
                        </div>
                        <div class="testi-item">
                            <h4>Оксана Білик</h4>
                            <ul class="list">
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                            </ul>
                            <div class="wow fadeIn" data-wow-duration="1s">
                                <p>
                                    Очень приятный салон! Хожу сюда на чистку лица и маникюр.
                                    Мастера хорошие, умеют работать с кожей. Атмосфера приятная,
                                    помогает расслабиться. Салоном очень довольна, приятное место
                                </p>
                            </div>
                        </div>
                        <div class="testi-item">
                            <h4>Оксана Білик</h4>
                            <ul class="list">
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                            </ul>
                            <div class="wow fadeIn" data-wow-duration="1s">
                                <p>
                                    Очень приятный салон! Хожу сюда на чистку лица и маникюр.
                                    Мастера хорошие, умеют работать с кожей. Атмосфера приятная,
                                    помогает расслабиться. Салоном очень довольна, приятное место
                                </p>
                            </div>
                        </div>
                        <div class="testi-item">
                            <h4>Оксана Білик</h4>
                            <ul class="list">
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                            </ul>
                            <div class="wow fadeIn" data-wow-duration="1s">
                                <p>
                                    Очень приятный салон! Хожу сюда на чистку лица и маникюр.
                                    Мастера хорошие, умеют работать с кожей. Атмосфера приятная,
                                    помогает расслабиться. Салоном очень довольна, приятное место
                                </p>
                            </div>
                        </div>
                        <div class="testi-item">
                            <h4>Оксана Білик</h4>
                            <ul class="list">
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                                <li>
                                    <a href="#"><i class="fa fa-star"></i></a><br>
                                </li>
                            </ul>
                            <div class="wow fadeIn" data-wow-duration="1s">
                                <p>
                                    Очень приятный салон! Хожу сюда на чистку лица и маникюр.
                                    Мастера хорошие, умеют работать с кожей. Атмосфера приятная,
                                    помогает расслабиться. Салоном очень довольна, приятное место
                                </p>
                            </div>
                        </div>
                    </carousel>
                </div>

            </div>


            <div class="owl-thumbs d-flex justify-content-center" style="top: -30px" data-slider-id="1">
<!--                <carousel :autoplay="true" :items="1" :dots="false" :nav="false" :navText="false">-->
                <div v-for="(obj,key) in testimonJSON" :key="key">
                <div class="owl-thumb-item">
                    <div>
                        <img class="img-fluid" src="img/testimonials1.png" alt="">
                    </div>
                    <div class="overlay overlay-grad"></div>
                </div>
                </div>
<!--                </carousel>-->
            </div>
<!--            <button id="button" class="btn-o" @click="v-b-modal.modal-multi-1">Залишити відгук</button>-->
        </div>

    </section>
        <div class="modal-bottom">
            <b-button v-b-modal.modal-multi-1 class="btn-o" >Залишити відгук</b-button>

            <b-modal id="modal-multi-1" size="lg" ok-title=""  cancel-title="" ok-variant="none" cancel-variant="none"  >
                <form action="http://localhost:5000/api/comments" method="post" class="modal-form">
                    <label class="modal-title">Залиште свій відгук</label>
                    <textarea name="" class="modal-text text-center"></textarea>
                    <fieldset class="rating">
                        <input type="radio" id="star5" name="rating" value="5">
                        <label class="full" for="star5"></label>
                        <input type="radio" id="star4" name="rating" value="4">
                        <label class="full" for="star4"></label>
                        <input type="radio" id="star3" name="rating" value="3">
                        <label class="full" for="star3"></label>
                        <input type="radio" id="star2" name="rating" value="2">
                        <label class="full" for="star2"></label>
                        <input type="radio" id="star1" name="rating" value="1">
                        <label class="full" for="star1"></label>
                    </fieldset>
                    <b-button class="primary-btn" v-b-modal.modal-multi-2>Відправити</b-button>

<!--                    <a href="#" class="primary-btn">Відправити</a>-->

                </form>
<!--                <b-button v-b-modal.modal-multi-2>Open Second Modal</b-button>-->
            </b-modal>

            <div class="modal-success">

            <b-modal class="modal-success " size="lg" id="modal-multi-2"  ok-title=""  cancel-title="" ok-variant="none" cancel-variant="none" hide-footer hide-header content-class="myclass">
                <p>
                    Ви успішно записались на процедуру косметологія в салоні краси LaRose<br>
                    Дякуємо, що ви обрали нас.<br>
                    Наш оператор зв’яжеться з вами в найближчий час.
                </p>
            </b-modal>
            </div>


        </div>



    </div>

</template>



<script>

    import carousel from 'vue-owl-carousel'

    export default {

        components: {carousel},

        name: "Testimonial",

        data:()=>({
            myclass: ['myclass'],
            testimonJSON:[
                {
                img:require('@/assets/img/testimonials1.png')
                },
                {
                img:require('@/assets/img/testimonials1.png')
                },
                {
                img:require('@/assets/img/testimonials1.png')
                },
                {
                img:require('@/assets/img/testimonials1.png')
                }

            ]
        })


    }
</script>

<style scoped>
    .testimonials-area {
        padding-bottom: 160px;
    }

    .modal-bottom {
        z-index: 2;
        margin-top: -190px;
        position: absolute;
        width: 100%;
    }

    button {
        background: none;
    }

    button.btn-o {
        font-family: "Proxima Nova Bold";
        color: #000;
        border: 3px solid #f03f69;
        letter-spacing: .1em;
        padding: 13px 27px;
        margin: 0 auto;
        display: block;
        width: 230px;
        text-align: center;
        border-radius: 0px;
    }

    button.btn-o:hover {
        background: #f03f69;
        color: #fff;
    }

    .primary-btn:hover, .primary-btn {
        background: #f03f69;
        color: #fff;
        border-radius: 0px;
    }


</style>
