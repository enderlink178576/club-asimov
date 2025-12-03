fetch("../footer/footer.html")
  .then(response => response.text())
  .then(data => {
    document.getElementById("footer").innerHTML = data;
  })
  .catch(error => console.error("Erreur de chargement du footer :", error));
