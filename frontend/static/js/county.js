/*
==========================================
County Portal JavaScript
==========================================
*/

document.addEventListener("DOMContentLoaded", () => {

    console.log("County Portal Loaded");

    // Planned enhancements:
    // - Auto-refresh work queue
    // - SLA countdown timers
    // - Desktop notifications
    // - Live assignment updates
});
/*
=========================================
County Calendar
=========================================
*/

document.addEventListener("DOMContentLoaded", function () {

    const calendarElement =
        document.getElementById("countyCalendar");

    if (!calendarElement) return;

    const calendar = new FullCalendar.Calendar(calendarElement, {

        initialView: "dayGridMonth",

        height: "auto",

        selectable: true,

        editable: false,

        nowIndicator: true,

        headerToolbar: {

            left: "prev,next today",

            center: "title",

            right: "dayGridMonth,timeGridWeek,timeGridDay"

        },

        events: [

            {

                title: "Water Supply Inspection",

                start: "2026-07-03",

                url: "/county/request/24"

            },

            {

                title: "Road Repair Deadline",

                start: "2026-07-08",

                url: "/county/request/28"

            },

            {

                title: "Business Permit Review",

                start: "2026-07-11",

                url: "/county/request/41"

            }

        ],

        eventClick: function(info){

            info.jsEvent.preventDefault();

            window.location = info.event.url;

        }

    });

    calendar.render();

});
events: "/county/api/calendar-events"
/*
====================================
Performance Charts
====================================
*/

const monthlyCanvas =
document.getElementById("monthlyChart");

if(monthlyCanvas){

new Chart(monthlyCanvas,{

type:"line",

data:{

labels:["Jan","Feb","Mar","Apr","May","Jun"],

datasets:[{

label:"Requests",

data:[44,58,62,70,81,94]

}]

}

});

}