/*
==========================================
Notifications Module
==========================================
*/

document.addEventListener("DOMContentLoaded", () => {

    loadNotifications();

});
async function loadNotifications(){

    try{

        const response = await fetch(

            "/notifications/api/list"

        );

        const notifications = await response.json();

        renderNotifications(notifications);

        updateNotificationBadge(notifications);

    }

    catch(error){

        console.error(

            "Unable to load notifications.",

            error

        );

    }

}
function renderNotifications(notifications){

    const container = document.getElementById(

        "notificationsContainer"

    );

    const dropdown = document.getElementById(

        "notificationList"

    );

    if(!container && !dropdown){

        return;

    }

    let html = "";

    notifications.forEach(notification=>{

        html += `

        <div class="notification-item ${notification.is_read ? "" : "notification-unread"}">

            <div class="notification-title">

                ${notification.title}

            </div>

            <div class="notification-message">

                ${notification.message}

            </div>

            <div class="notification-date">

                ${notification.created_at}

            </div>

        </div>

        `;

    });

    if(container){

        container.innerHTML = html;

    }

    if(dropdown){

        dropdown.innerHTML = html;

    }

}
function updateNotificationBadge(notifications){

    const badge = document.getElementById(

        "notificationCount"

    );

    if(!badge){

        return;

    }

    const unread = notifications.filter(

        n=>!n.is_read

    ).length;

    badge.textContent = unread;

    badge.style.display = unread>0 ? "inline-block" : "none";

}
async function loadTimeline(requestId){

    const response =
        await fetch(`/requests/api/${requestId}/timeline`);

    const timeline =
        await response.json();

    let html="";

    timeline.forEach(item=>{

        html+=`

        <div class="timeline-item">

            <strong>${item.time}</strong>

            <br>

            ${item.event}

        </div>

        `;

    });

    document.getElementById(
        "timelineContainer"
    ).innerHTML=html;

}