document.addEventListener("DOMContentLoaded", () => {
  const tabButtons = document.querySelectorAll(".tab-button-homepage");
  const tabContents = document.querySelectorAll(".tab-content-homepage");

  tabButtons.forEach(button => {
    button.addEventListener("click", () => {
      // Aktiven Button entfernen
      tabButtons.forEach(btn => btn.classList.remove("active"));
      // Aktiven Inhalt entfernen
      tabContents.forEach(content => content.classList.remove("active"));

      // Geklickten Button aktivieren
      button.classList.add("active");
      // Passenden Content aktivieren
      const tabId = button.getAttribute("data-tab");
      const tabContent = document.getElementById(tabId);
      if (tabContent) tabContent.classList.add("active");
    });
  });
});
