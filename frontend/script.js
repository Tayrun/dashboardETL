fetch("http://localhost:8000/api/resultados")
    .then(res => res.json())
    .then(json => {
        const data = json.data;
        const tabla = document.getElementById("resultados");
        const thead = tabla.querySelector("thead");
        const tbody = tabla.querySelector("tbody");

        if (data.length > 0) {
            // Cabecera
            thead.innerHTML = "<tr>" + Object.keys(data[0]).map(col => `<th>${col}</th>`).join("") + "</tr>";

            // Filas
            tbody.innerHTML = data.map(row => {
                return "<tr>" + Object.values(row).map(val => `<td>${val}</td>`).join("") + "</tr>";
            }).join("");
        } else {
            tbody.innerHTML = "<tr><td colspan='100%'>No hay resultados</td></tr>";
        }
    })
    .catch(err => console.error("Error:", err));
