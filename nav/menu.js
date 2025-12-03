// Charger le contenu de menu.html dans la div #menu
fetch("../nav/menu.html")
  .then(response => response.text())
  .then(data => {
    document.getElementById("menu").innerHTML = data;

    // Active le bouton hamburger
    const toggle = document.getElementById("menu-toggle");
    const menuList = document.getElementById("menu-list");

    toggle.addEventListener("click", () => {
      menuList.classList.toggle("show");
    });
  });