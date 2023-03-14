
// Confirm delete action
let confirmDelete = function (event) {
  event.preventDefault();
  if (confirm("Are you sure you want to delete this item?")) {
    // Delete the item
    window.location.href = this.getAttribute("href");
  }
};

// Add confirm delete to all delete buttons
let deleteButtons = document.querySelectorAll(".btn-delete");
deleteButtons.forEach((button) => {
  button.addEventListener("click", confirmDelete);
});
