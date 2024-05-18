const allSideMenu = document.querySelectorAll("#sidebar .side-menu.top li a");

allSideMenu.forEach((item) => {
  const li = item.parentElement;

  item.addEventListener("click", function () {
    allSideMenu.forEach((i) => {
      i.parentElement.classList.remove("active");
    });
    li.classList.add("active");
  });
});

// TOGGLE SIDEBAR
const menuBar = document.querySelector("#content nav .bx.bx-menu");
const sidebar = document.getElementById("sidebar");
const dashboard = document.getElementById("dashboard");

menuBar.addEventListener("click", function () {
  sidebar.classList.toggle("hide");
  dashboard.classList.toggle("expand");
});

const searchButton = document.querySelector(
  "#content nav form .form-input button"
);
const searchButtonIcon = document.querySelector(
  "#content nav form .form-input button .bx"
);
const searchForm = document.querySelector("#content nav form");

searchButton.addEventListener("click", function (e) {
  if (window.innerWidth < 576) {
    e.preventDefault();
    searchForm.classList.toggle("show");
    if (searchForm.classList.contains("show")) {
      searchButtonIcon.classList.replace("bx-search", "bx-x");
    } else {
      searchButtonIcon.classList.replace("bx-x", "bx-search");
    }
  }
});

if (window.innerWidth < 768) {
  sidebar.classList.add("hide");
} else if (window.innerWidth > 576) {
  searchButtonIcon.classList.replace("bx-x", "bx-search");
  searchForm.classList.remove("show");
}

window.addEventListener("resize", function () {
  if (this.innerWidth > 576) {
    searchButtonIcon.classList.replace("bx-x", "bx-search");
    searchForm.classList.remove("show");
  }
});

// Dashboard

var data = [
  {
    profilePhoto:
      "https://plus.unsplash.com/premium_photo-1690579805307-7ec030c75543?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fHByb2ZpbGUlMjBpY29ufGVufDB8fDB8fHww",
    name: "Daniel Smith",
    gender: "Male",
    weight: "75kg",
    disease: "cancer",
    date: "29 Jan",
    heartRate: "56 BPM",
    bloodType: "AB",
    status: "Outpatient",
    // Add profile photo URL here
  },
  {
    profilePhoto:
      "https://plus.unsplash.com/premium_photo-1690579805307-7ec030c75543?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fHByb2ZpbGUlMjBpY29ufGVufDB8fDB8fHww",
    name: "Daniel Smith",
    gender: "Male",
    weight: "75kg",
    disease: "cancer",
    date: "29 Jan",
    heartRate: "56 BPM",
    bloodType: "AB",
    status: "Outpatient",
    // Add profile photo URL here
  },
  {
    profilePhoto:
      "https://plus.unsplash.com/premium_photo-1690579805307-7ec030c75543?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fHByb2ZpbGUlMjBpY29ufGVufDB8fDB8fHww",
    name: "Daniel Smith",
    gender: "Male",
    weight: "75kg",
    disease: "cancer",
    date: "29 Jan",
    heartRate: "56 BPM",
    bloodType: "AB",
    status: "Outpatient",
    // Add profile photo URL here
  },
  {
    profilePhoto:
      "https://plus.unsplash.com/premium_photo-1690579805307-7ec030c75543?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fHByb2ZpbGUlMjBpY29ufGVufDB8fDB8fHww",
    name: "Daniel Smith",
    gender: "Male",
    weight: "75kg",
    disease: "cancer",
    date: "29 Jan",
    heartRate: "56 BPM",
    bloodType: "AB",
    status: "Outpatient",
    // Add profile photo URL here
  },
  {
    profilePhoto:
      "https://plus.unsplash.com/premium_photo-1690579805307-7ec030c75543?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fHByb2ZpbGUlMjBpY29ufGVufDB8fDB8fHww",
    name: "Daniel Smith",
    gender: "Male",
    weight: "75kg",
    disease: "cancer",
    date: "29 Jan",
    heartRate: "56 BPM",
    bloodType: "AB",
    status: "Outpatient",
    // Add profile photo URL here
  },
];

function generateTable(data) {
  var tbody = document.getElementById("recentBody");
  var headers = Object.keys(data[0]);

  data.forEach((item) => {
    var row = document.createElement("tr");

    // Create and append profile photo
    var profileCell = document.createElement("td");
    var profileImg = document.createElement("img");
    profileImg.src = item.profilePhoto;
    profileImg.alt = "Profile Photo";
    profileImg.className = "profileImg";
    profileCell.appendChild(profileImg);
    profileCell.appendChild(document.createTextNode(item.name)); // Add name alongside the image
    row.appendChild(profileCell);

    // Append other data
    headers.slice(2).forEach((key) => {
      // Start from index 1 to skip the name
      var cell = document.createElement("td");
      cell.textContent = item[key];
      row.appendChild(cell);
    });
    tbody.appendChild(row);
  });
}
generateTable(data);

const ctx = document.getElementById("myChart");

new Chart(ctx, {
  type: "bar",
  data: {
    labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    datasets: [
      {
        label: "Patients  ",
        data: [130, 155, 125, 135, 167, 138, 120],
        borderWidth: 1,
        backgroundColor: "#484cd9",
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});

// Get all <p> tags inside the task-list
const taskItems = document.querySelectorAll('.task-list p');

// Add click event listener to each <p> tag
taskItems.forEach(item => {
    item.addEventListener('click', function() {
        // Remove taskactive class from all <p> tags
        taskItems.forEach(item => {
            item.classList.remove('taskactive');
        });

        // Add taskactive class to the clicked <p> tag
        this.classList.add('taskactive');
    });
});