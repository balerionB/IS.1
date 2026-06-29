/*
==========================================
Analytics Dashboard
==========================================
*/

document.addEventListener("DOMContentLoaded", () => {

    loadDashboardSummary();

    loadMonthlyChart();

    loadDepartmentChart();

    loadCategoryChart();

    loadSLAChart();

    loadOfficerChart();

});

async function loadDashboardSummary(){

    try{

        const response = await fetch(

            "/analytics/api/summary"

        );

        const summary = await response.json();

        document.getElementById("totalRequests").textContent =

            summary.total_requests;

        document.getElementById("resolvedRequests").textContent =

            summary.resolved;

        document.getElementById("pendingRequests").textContent =

            summary.pending;

        document.getElementById("averageSLA").textContent =

            summary.average_sla;

        document.getElementById("customerSatisfaction").textContent =

            summary.satisfaction;

    }

    catch(error){

        console.error(

            "Dashboard failed to load.",

            error

        );

    }

}
async function loadMonthlyChart(){

    const response = await fetch(

        "/analytics/api/monthly"

    );

    const monthly = await response.json();

    const canvas = document.getElementById(

        "monthlyTrendChart"

    );

    if(!canvas){

        return;

    }

    new Chart(canvas,{

        type:"line",

        data:{

            labels:monthly.labels,

            datasets:[{

                label:"Requests",

                data:monthly.values,

                borderWidth:3,

                tension:0.4,

                fill:false

            }]

        },

        options:{

            responsive:true,

            maintainAspectRatio:false

        }

    });

}
async function loadDepartmentChart(){

    const response =
        await fetch("/analytics/api/departments");

    const data =
        await response.json();

    new Chart(

        document.getElementById("departmentChart"),

        {

            type:"bar",

            data:{

                labels:data.labels,

                datasets:[{

                    label:"Performance %",

                    data:data.values

                }]

            }

        }

    );

}
async function loadCategoryChart(){

    const response =
        await fetch("/analytics/api/categories");

    const data =
        await response.json();

    new Chart(

        document.getElementById("categoryChart"),

        {

            type:"pie",

            data:{

                labels:data.labels,

                datasets:[{

                    label:"Requests",

                    data:data.values

                }]

            }

        }

    );

}

async function loadOfficerChart(){

    const response =
        await fetch("/analytics/api/officers");

    const data =
        await response.json();

    new Chart(

        document.getElementById("officerChart"),

        {

            type:"bar",

            data:{

                labels:data.labels,

                datasets:[{

                    label:"Resolved Requests",

                    data:data.values

                }]

            }

        }

    );

}
const labels = [
    "Completed",
    "Late"
];

const values = [
    data.completed,
    data.late
];
createChart(
    "slaChart",
    "doughnut",
    labels,
    values,
    "SLA"
);
document
.getElementById("previewReport")
?.addEventListener("click", previewReport);

async function previewReport() {

    try {

        const response = await fetch(
            "/analytics/api/report"
        );

        const report = await response.json();

        let html = `

            <h5>Summary</h5>

            <table class="table table-bordered">

                <tr>

                    <th>Total Requests</th>

                    <td>${report.summary.total}</td>

                </tr>

                <tr>

                    <th>Resolved</th>

                    <td>${report.summary.resolved}</td>

                </tr>

                <tr>

                    <th>Pending</th>

                    <td>${report.summary.pending}</td>

                </tr>

                <tr>

                    <th>SLA Compliance</th>

                    <td>${report.summary.sla}</td>

                </tr>

            </table>

            <h5 class="mt-4">

                Department Summary

            </h5>

            <table class="table table-striped">

                <thead>

                    <tr>

                        <th>Department</th>

                        <th>Requests</th>

                    </tr>

                </thead>

                <tbody>

        `;

        report.departments.forEach(department => {

            html += `

                <tr>

                    <td>${department.name}</td>

                    <td>${department.requests}</td>

                </tr>

            `;

        });

        html += `

                </tbody>

            </table>

        `;

        document.getElementById(
            "reportPreview"
        ).innerHTML = html;

    }

    catch(error){

        console.error(
            "Unable to generate report.",
            error
        );

    }

}
document

.getElementById("exportPDF")

.addEventListener("click",()=>{

window.location="/analytics/export/pdf";

});
document

.getElementById("exportExcel")

.addEventListener(()=>{

window.location="/analytics/export/excel";

});
async function loadInsights(){

const response=

await fetch("/analytics/api/insights");

const insights=

await response.json();

const list=

document.getElementById("insightList");

list.innerHTML="";

insights.forEach(item=>{

list.innerHTML+=`

<li>${item}</li>

`;

});

}
catch(error){

document.getElementById(

"reportPreview"

).innerHTML=`

<div class="alert alert-danger">

Unable to load report data.

</div>

`;

}