<template>


    <!-- Meta -->


    <body class="register-body">

    <!-- Register -->

    <section class="register">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <h2 class="section-title text-center">Запишіться на процедури онлайн</h2>
                </div>
            </div>
            <div class="row">
                <div class="col-12 mb-25">
                    <h4 class="title">Виберіть процедуру:</h4>
                </div>
            </div>
            <div class="row">
                <div class="col-5 procedure-col">
                    <ul class="procedure">
                        <li>
                            <label class="checkbox" for="checkbox1">
                                <input id="checkbox1" type="checkbox">
                                <p class="checkbox__text">Візажист</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox2">
                                <input id="checkbox2" type="checkbox">
                                <p class="checkbox__text">Візажист</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox3">
                                <input id="checkbox3" type="checkbox">
                                <p class="checkbox__text">Spa-процедури</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox4">
                                <input id="checkbox4" type="checkbox">
                                <p class="checkbox__text">Spa-процедури</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox5">
                                <input id="checkbox5" type="checkbox">
                                <p class="checkbox__text">Манікюр</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox6">
                                <input id="checkbox6" type="checkbox">
                                <p class="checkbox__text">Манікюр</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox7">
                                <input id="checkbox7" type="checkbox">
                                <p class="checkbox__text">Нарощування вій</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox8">
                                <input id="checkbox8" type="checkbox">
                                <p class="checkbox__text">Нарощування вій</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox9">
                                <input id="checkbox9" type="checkbox">
                                <p class="checkbox__text">Перукар</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox10">
                                <input id="checkbox10" type="checkbox">
                                <p class="checkbox__text">Перукар</p>
                            </label>
                        </li>

                    </ul>
                </div>
                <div class="col-7 register-text-col">
                    <p>
                        Робота візажиста складається з кількох етапів: по-перше, це коректування і зорове поліпшення
                        контуру обличчя людини; по-друге, поєднання класичних прийомів.<br><br>
                        Головне завдання візажиста – не лише створити певний образ, але підкреслити переваги обличчя
                        людини і приховати недоліки. Фахівець повинен знати, які кольори і текстури підходять даному
                        типу зовнішності, костюм, образ, доречні для певного періоду, року, події. Закінчити курси
                        візажистів не завадить кожній жінці.
                    </p>
                </div>
            </div>
            <div class="row">
                <div class="col-12">
                    <h4 class="title">Виберіть майстра:</h4>
                </div>
            </div>
            <div class="row specialist-row">

                <div class="col-2">
                    <div class="specialist">
                        <input id="radio1" class="radio" name="radio" type="radio">
                        <label for="radio1"></label>

                        <img src="img/specialist1.jpg" alt="">
                        <h5 class="specialist__name">Крістіна Самойлова</h5>
                    </div>
                </div>

                <div class="col-2">
                    <div class="specialist">
                        <input id="radio2" class="radio" name="radio" type="radio">
                        <label for="radio2"></label>

                        <img src="img/specialist2.jpg" alt="">
                        <h5 class="specialist__name">Ольга Вікторівна</h5>
                    </div>
                </div>

                <div class="col-2">
                    <div class="specialist">
                        <input id="radio3" class="radio" name="radio" type="radio">
                        <label for="radio3"></label>

                        <img src="img/specialist3.jpg" alt="">
                        <h5 class="specialist__name">Наталія Дрогобич</h5>
                    </div>
                </div>

                <div class="col-2">
                    <div class="specialist">
                        <input id="radio4" class="radio" name="radio" type="radio">
                        <label for="radio4"></label>

                        <img src="img/specialist4.jpg" alt="">
                        <h5 class="specialist__name">Оксана Семанів</h5>
                    </div>
                </div>

                <div class="col-2">
                    <div class="specialist">
                        <input id="radio5" class="radio" name="radio" type="radio">
                        <label for="radio5"></label>

                        <img src="img/specialist5.jpg" alt="">
                        <h5 class="specialist__name">Оксана Семанів</h5>
                    </div>
                </div>

                <div class="col-2">
                    <div class="specialist">
                        <input id="radio6" class="radio" name="radio" type="radio">
                        <label for="radio6"></label>

                        <img src="img/specialist6.jpg" alt="">
                        <h5 class="specialist__name">Оксана Семанів</h5>
                    </div>
                </div>

            </div>
            <div class="row">
                <div class="col-12">
                    <h4 class="title mt-70 mb-25">Виберіть зручний для вас час:</h4>
                </div>
            </div>
            <div class="row align-items-center">
                <div class="col-4 calendar-col">
                    <div id="calendar" class="vanilla-calendar"></div>
                </div>
                <div class="col-5 work-col">
                    <ul class="work-time">

                        <li>
                            <label class="checkbox" for="checkbox11">
                                <input id="checkbox11" type="radio" name="work-radio">
                                <p class="checkbox__text">07:00</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox12">
                                <input id="checkbox12" type="radio" name="work-radio">
                                <p class="checkbox__text">08:30</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox13">
                                <input id="checkbox13" type="radio" name="work-radio">
                                <p class="checkbox__text">09:30</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox14">
                                <input id="checkbox14" type="radio" name="work-radio">
                                <p class="checkbox__text">10:30</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox checkbox_disabled" for="checkbox15">
                                <input id="checkbox15" type="radio" name="work-radio" disabled>
                                <p class="checkbox__text">11:00</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox16">
                                <input id="checkbox16" type="radio" name="work-radio">
                                <p class="checkbox__text">12:00</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox17">
                                <input id="checkbox17" type="radio" name="work-radio">
                                <p class="checkbox__text">13:00</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox18">
                                <input id="checkbox18" type="radio" name="work-radio">
                                <p class="checkbox__text">13:40</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox19">
                                <input id="checkbox19" type="radio" name="work-radio">
                                <p class="checkbox__text">14:00</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox checkbox_disabled" for="checkbox20">
                                <input id="checkbox20" type="radio" name="work-radio" disabled>
                                <p class="checkbox__text">14:40</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox21">
                                <input id="checkbox21" type="radio" name="work-radio">
                                <p class="checkbox__text">15:30</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox22">
                                <input id="checkbox22" type="radio" name="work-radio">
                                <p class="checkbox__text">16:30</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox" for="checkbox23">
                                <input id="checkbox23" type="radio" name="work-radio">
                                <p class="checkbox__text">17:00</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox checkbox_disabled" for="checkbox24">
                                <input id="checkbox24" type="radio" name="work-radio" disabled>
                                <p class="checkbox__text">18:00</p>
                            </label>
                        </li>

                        <li>
                            <label class="checkbox checkbox_disabled" for="checkbox25">
                                <input id="checkbox25" type="radio" name="work-radio" disabled>
                                <p class="checkbox__text">19:00</p>
                            </label>
                        </li>

                    </ul>
                </div>
                <div class="register-btn col-3 text-right">
                    <b-button v-b-modal.modal-multi-1 class="btn-o" >Залишити відгук</b-button>
                    <b-modal class="modal-success " size="lg" id="modal-multi-1"  ok-title=""  cancel-title="" ok-variant="none" cancel-variant="none" hide-footer hide-header content-class="myclass">
                        <p>
                            Ви успішно записались на процедуру косметологія в салоні краси LaRose<br>
                            Дякуємо, що ви обрали нас.<br>
                            Наш оператор зв’яжеться з вами в найближчий час.
                        </p>
                    </b-modal>
                </div>
            </div>
        </div>
    </section>

    <!-- / Register -->


    </body>


</template>

<script>
    export default {
        name: "Register",
        mounted() {
            new window.vanillaCalendar({
                selector: "#calendar",
                months: ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень"],
                shortWeekday: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Нд',],
            });

        }

    }
</script>

<style scoped>
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
