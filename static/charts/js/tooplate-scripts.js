// let ctxLine,
// ctxBar,
// ctxPie,
// optionsLine,
// optionsBar,
// optionsPie,
// configLine,
// configBar,
// configPie,
// lineChart;
// barChart, pieChart;
// // DOM is ready
// $(function () {
// updateChartOptions();
// drawBarChart(); // Bar Chart
// drawPieChart(); // Pie Chart

// $(window).resize(function () {
//     updateChartOptions();
//     updateLineChart();
//     updateBarChart();
//     reloadPage();
// });
// })

// const width_threshold = 480;

// function drawBarChart() {
// if ($("#pieChart").length) {
// ctxBar = document.getElementById("barChart").getContext("2d");

// optionsBar = {
// responsive: true,
// scales: {
// yAxes: [
// {
// ticks: {
//   beginAtZero: true
// },
// scaleLabel: {
//   display: true,
//   labelString: "Count"
// }
// }
// ]
// }
// };

// optionsBar.maintainAspectRatio = $(window).width() < width_threshold ? false : true;

// configBar = {
// type: "bar",
// data: {
// labels: {{ age_labels|safe }},
// datasets: [
// {
// label: {{ age_labels|safe }},
// data: {{ age_data|safe }},
// backgroundColor: [
//   "rgba(255, 99, 132, 0.2)",
//   "rgba(54, 162, 235, 0.2)",
//   "rgba(255, 206, 86, 0.2)",
//   "rgba(75, 192, 192, 0.2)",
//   "rgba(153, 102, 255, 0.2)",
//   "rgba(255, 159, 64, 0.2)"
// ],
// borderColor: [
//   "rgba(255,99,132,1)",
//   "rgba(54, 162, 235, 1)",
//   "rgba(255, 206, 86, 1)",
//   "rgba(75, 192, 192, 1)",
//   "rgba(153, 102, 255, 1)",
//   "rgba(255, 159, 64, 1)"
// ],
// borderWidth: 1
// }
// ]
// },
// options: optionsBar
// };

// barChart = new Chart(ctxBar, configBar);
// }
// }

// function drawPieChart() {
// if ($("#ageChart").length) {
// ctxPie = document.getElementById("ageChart").getContext("2d");
// optionsPie = {
// responsive: true,
// maintainAspectRatio: false
// };

// configPie = {
// type: "pie",
// data: {
// datasets: [
// {
// data: {{ age_data|safe }},
// backgroundColor: [
//   window.chartColors.purple,
//   window.chartColors.green
// ],
// label: "Storage"
// }
// ],
// labels: {{ age_labels|safe }}
// },
// options: optionsPie
// };

// pieChart = new Chart(ctxPie, configPie);
// }

// }

// function updateChartOptions() {
// if ($(window).width() < width_threshold) {
// if (optionsLine) {
// optionsLine.maintainAspectRatio = false;
// }
// if (optionsBar) {
// optionsBar.maintainAspectRatio = false;
// }
// } else {
// if (optionsLine) {
// optionsLine.maintainAspectRatio = true;
// }
// if (optionsBar) {
// optionsBar.maintainAspectRatio = true;
// }
// }
// }

// function updateBarChart() {
// if (barChart) {
// barChart.options = optionsBar;
// barChart.update();
// }
// }

// function reloadPage() {
// setTimeout(function() {
// window.location.reload();
// }); // Reload the page so that charts will display correctly
// }
