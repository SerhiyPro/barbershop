let vanillaCalendar = function(t) {
  function e(t, e, a) {
      t && (t.attachEvent ? t.attachEvent("on" + e, a) : t.addEventListener(e, a))
  }

  function a(t, e, a) {
      t && (t.detachEvent ? t.detachEvent("on" + e, a) : t.removeEventListener(e, a))
  }
  let n = {
      selector: null,
      datesFilter: !1,
      pastDates: !0,
      availableWeekDays: [],
      availableDates: [],
      date: new Date,
      todaysDate: new Date,
      button_prev: null,
      button_next: null,
      month: null,
      month_label: null,
      onSelect: (t, e) => {},
      months: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
      shortWeekday: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
  };
  for (let e in t) n.hasOwnProperty(e) && (n[e] = t[e]);
  let l = document.querySelector(n.selector);
  if (!l) return;
  const r = function(t) {
          let e = document.createElement("div"),
              a = document.createElement("span");
          a.innerHTML = t.getDate(), e.className = "vanilla-calendar-date", e.setAttribute("data-calendar-date", t);
          let l = n.availableWeekDays.filter(e => e.day === t.getDay() || e.day === void t.getDay()),
              r = n.availableDates.filter(e => e.date === "-" + String(t.getMonth() + 1).padStart("2", 0) + "-" + String(t.getDate()).padStart("2", 0));
          var d;
          1 === t.getDate() && (e.style.marginLeft = 14.28 * (d = t.getDay(), console.log("getMyDay"), 0 == d ? 6 : d - 1) + "%"), n.date.getTime() <= n.todaysDate.getTime() - 1 && !n.pastDates ? e.classList.add("vanilla-calendar-date--disabled") : n.datesFilter ? l.length ? (e.classList.add("vanilla-calendar-date--active"), e.setAttribute("data-calendar-data", JSON.stringify(l[0])), e.setAttribute("data-calendar-status", "active")) : r.length ? (e.classList.add("vanilla-calendar-date--active"), e.setAttribute("data-calendar-data", JSON.stringify(r[0])), e.setAttribute("data-calendar-status", "active")) : e.classList.add("vanilla-calendar-date--disabled") : (e.classList.add("vanilla-calendar-date--active"), e.setAttribute("data-calendar-status", "active")), t.toString() === n.todaysDate.toString() && e.classList.add("vanilla-calendar-date--today"), e.appendChild(a), n.month.appendChild(e)
      },
      d = function() {
          o();
          let t = n.date.getMonth();
          for (; n.date.getMonth() === t;) r(n.date), n.date.setDate(n.date.getDate() + 1);
          n.date.setDate(1), n.date.setMonth(n.date.getMonth() - 1), n.month_label.innerHTML = n.months[n.date.getMonth()], l.querySelectorAll("[data-calendar-status=active]").forEach(t => {
              t.addEventListener("click", function() {
                  document.querySelectorAll(".vanilla-calendar-date--selected").forEach(t => {
                      t.classList.remove("vanilla-calendar-date--selected")
                  });
                  let t = this.dataset,
                      e = {};
                  t.calendarDate && (e.date = t.calendarDate), t.calendarData && (e.data = JSON.parse(t.calendarData)), n.onSelect(e, this), this.classList.add("vanilla-calendar-date--selected")
              })
          })
      },
      s = function() {
          n.date.setMonth(n.date.getMonth() - 1), d()
      },
      i = function() {
          n.date.setMonth(n.date.getMonth() + 1), d()
      },
      o = function() {
          n.month.innerHTML = ""
      };
  this.init = function() {
      document.querySelector(n.selector).innerHTML = '\n            <div class="vanilla-calendar-header">\n                <button type="button" class="vanilla-calendar-btn" data-calendar-toggle="previous"><img src="img/arrow-left.svg" height="24" width="24" onerror="this.onerror=null; this.src="img/arrow-left.png"></button>\n                <div class="vanilla-calendar-header__label" data-calendar-label="month"></div>\n                <button type="button" class="vanilla-calendar-btn" data-calendar-toggle="next"><img src="img/arrow-right.svg" height="24" width="24" onerror="this.onerror=null; this.src="img/arrow-right.png"></button>\n            </div>\n            <div class="vanilla-calendar-week"></div>\n            <div class="vanilla-calendar-body-wrapper"><div class="vanilla-calendar-body" data-calendar-area="month"></div></div>\n            ', n.button_prev = document.querySelector(n.selector + " [data-calendar-toggle=previous]"), n.button_next = document.querySelector(n.selector + " [data-calendar-toggle=next]"), n.month = document.querySelector(n.selector + " [data-calendar-area=month]"), n.month_label = document.querySelector(n.selector + " [data-calendar-label=month]"), n.date.setDate(1), d(), document.querySelector(`${n.selector} .vanilla-calendar-week`).innerHTML = `\n                <span>${n.shortWeekday[0]}</span>\n                <span>${n.shortWeekday[1]}</span>\n                <span>${n.shortWeekday[2]}</span>\n                <span>${n.shortWeekday[3]}</span>\n                <span>${n.shortWeekday[4]}</span>\n                <span>${n.shortWeekday[5]}</span>\n                <span>${n.shortWeekday[6]}</span>\n            `, e(n.button_prev, "click", s), e(n.button_next, "click", i)
  }, this.destroy = function() {
      a(n.button_prev, "click", s), a(n.button_next, "click", i), o(), document.querySelector(n.selector).innerHTML = ""
  }, this.reset = function() {
      this.destroy(), this.init()
  }, this.set = function(t) {
      for (let e in t) n.hasOwnProperty(e) && (n[e] = t[e]);
      d()
  }, this.init()
};
window.vanillaCalendar = vanillaCalendar;