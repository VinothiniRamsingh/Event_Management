const API_URL = "http://127.0.0.1:8000/events";

//  LOAD BOOKINGS 
function loadBookings() {
    const tbody = document.getElementById("booking-body");
    tbody.innerHTML = "";

    fetch(API_URL)
        .then(res => res.json())
        .then(data => {
            data.forEach(item => {
                const row = createReadOnlyRow(item);
                tbody.appendChild(row);
            });
        })
        .catch(err => console.error("Load error:", err));
}

//  READ ONLY ROW 
function createReadOnlyRow(item) {
    const row = document.createElement("tr");

    row.innerHTML = `
        <td>${item.booking_id}</td>
        <td>${item.user_name}</td>
        <td>${item.city}</td>
        <td>${item.phone}</td>
        <td>${item.event_type}</td>
        <td>${item.event_date}</td>
        <td>${item.location}</td>
        <td>${item.budget}</td>
        <td>
            <button class="deleteBtn" data-id="${item.booking_id}">⛔</button>
        </td>
    `;
    return row;
}

//  ADD NEW ROW 
function addNewBookingRow() {
    const tbody = document.getElementById("booking-body");
    const row = document.createElement("tr");

    row.innerHTML = `
        <td>Auto</td>
        <td><input class="user_name" placeholder="User Name"></td>
        <td><input class="city" placeholder="City"></td>
        <td><input class="phone" placeholder="Phone"></td>
        <td><input class="event_type" placeholder="Event Type"></td>
        <td><input type="date" class="event_date"></td>
        <td><input class="location" placeholder="Location"></td>
        <td><input type="number" class="budget" placeholder="Budget"></td>
        <td>
            <button class="saveBtn">💾</button>
            <button class="deleteBtn">⛔</button>
        </td>
    `;

    tbody.appendChild(row);
}

//  SAVE NEW BOOKING 
function saveBooking(row) {
    const user_name  = row.querySelector(".user_name").value.trim();
    const city       = row.querySelector(".city").value.trim();
    const phone      = row.querySelector(".phone").value.trim();
    const event_type = row.querySelector(".event_type").value.trim();
    const event_date = row.querySelector(".event_date").value;
    const location   = row.querySelector(".location").value.trim();
    const budgetVal  = row.querySelector(".budget").value;

    // Required fields validation
    if (!user_name || !event_type || !event_date) {
        alert("Please fill all required fields: User Name, Event Type, Event Date");
        return;
    }

    const budget = budgetVal ? Number(budgetVal) : 0; 

    // Build request body
    const data = {
        user_name,
        city,
        phone,
        event_type,
        event_date,   // YYYY-MM-DD
        location,
        budget
    };

    console.log("Saving booking:", data); 

    fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(async res => {
        if (!res.ok) {
            const text = await res.text();
            console.error("Save failed response:", text);
            throw new Error("Save failed");
        }
        return res.json();
    })
    .then(() => {
        alert("Booking saved successfully!");
        loadBookings(); // refresh table
    })
    .catch(err => {
        console.error(err);
        alert("Save failed. Check console for details.");
    });
}

//  DELETE BOOKING 
function deleteBooking(id, row) {
    if (!id) {
        row.remove(); // unsaved row
        return;
    }

    fetch(`${API_URL}/${id}`, { method: "DELETE" })
        .then(res => {
            if (!res.ok) throw new Error("Delete failed");
            loadBookings();
        })
        .catch(err => {
            console.error(err);
            alert("Delete failed");
        });
}

//  EVENT LISTENERS 
document.addEventListener("DOMContentLoaded", () => {
    loadBookings();

    document.getElementById("addRowBtn").onclick = addNewBookingRow;

    document.getElementById("booking-body").onclick = e => {
        const row = e.target.closest("tr");
        if (!row) return;

        if (e.target.classList.contains("saveBtn")) {
            saveBooking(row);
        }

        if (e.target.classList.contains("deleteBtn")) {
            const id = e.target.dataset.id;
            deleteBooking(id, row);
        }
    };
});
